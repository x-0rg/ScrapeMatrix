import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

from scrapematrix.scrapers.base_scraper import BaseScraper
from scrapematrix.data.db_session import get_db_session, DATA_DIR
from scrapematrix.models.stock_models import SECRelease

class SECScraper(BaseScraper):
    """Scrapes SEC Edgar for 10-K and 10-Q filings, downloading metadata and full text."""

    def __init__(self):
        super().__init__()
        # SEC requires a specific User-Agent format: AppName ContactEmail
        self.headers = {
            "User-Agent": "ScrapeMatrix Desktop App (admin@scrapematrix.local)",
            "Accept-Encoding": "gzip, deflate"
        }
        self.tickers_map = None
        self.filings_dir = os.path.join(DATA_DIR, "filings")
        if not os.path.exists(self.filings_dir):
            os.makedirs(self.filings_dir)

    def _load_tickers_map(self):
        """Loads ticker to CIK mapping from SEC."""
        try:
            url = "https://www.sec.gov/files/company_tickers.json"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            # Invert the config to map Ticker -> CIK
            self.tickers_map = {item['ticker']: str(item['cik_str']).zfill(10) for _, item in data.items()}
        except Exception as e:
            self.logger.error(f"Failed to load SEC tickers map: {e}")
            self.tickers_map = {}

    def get_cik(self, ticker: str) -> str:
        if self.tickers_map is None:
            self._load_tickers_map()
        return self.tickers_map.get(ticker.upper())

    def scrape(self, ticker: str, limit: int = 5):
        """
        Scrapes recent 10-K and 10-Q forms for the given ticker.
        """
        cik = self.get_cik(ticker)
        if not cik:
            self.logger.error(f"Could not find CIK for ticker {ticker}")
            return []

        self.logger.info(f"Resolved {ticker} to CIK {cik}")
        
        submissions_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        
        try:
            response = requests.get(submissions_url, headers=self.headers, timeout=15)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch submissions for CIK {cik}: {e}")
            return []

        recent = data.get("filings", {}).get("recent", {})
        if not recent:
            return []

        accession_numbers = recent.get("accessionNumber", [])
        form_types = recent.get("form", [])
        filing_dates = recent.get("filingDate", [])
        primary_documents = recent.get("primaryDocument", [])

        processed = []

        with get_db_session() as session:
            count = 0
            for acc, f_type, f_date_str, doc in zip(accession_numbers, form_types, filing_dates, primary_documents):
                if count >= limit:
                    break
                    
                if f_type not in ["10-K", "10-Q"]:
                    continue

                # Prepare URLs
                acc_no_dashes = acc.replace("-", "")
                doc_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_no_dashes}/{doc}"
                
                # Check DB
                existing = session.query(SECRelease).filter_by(accession_number=acc).first()
                if existing:
                    self.logger.info(f"Filing already exists in DB: {f_type} {acc}")
                    processed.append(existing)
                    count += 1
                    continue

                f_date = datetime.strptime(f_date_str, "%Y-%m-%d")

                # Actively download and extract text
                local_path = self._download_and_extract_text(ticker, acc, doc_url)

                release = SECRelease(
                    ticker=ticker,
                    cik=cik,
                    form_type=f_type,
                    filing_date=f_date,
                    accession_number=acc,
                    primary_document_url=doc_url,
                    local_file_path=local_path
                )
                session.add(release)
                processed.append(release)
                self.logger.info(f"Saved new SEC filing: {f_type} {acc}")
                count += 1

        return processed

    def _download_and_extract_text(self, ticker: str, accession_number: str, url: str) -> str:
        """Downloads the HTM/TXT document, extracts text, and saves to file."""
        try:
            response = requests.get(url, headers=self.headers, timeout=20)
            response.raise_for_status()
            content = response.text

            # If HTML, parse and abstract text out
            if url.endswith(".htm") or url.endswith(".html"):
                soup = BeautifulSoup(content, "html.parser")
                text_content = soup.get_text(separator="\n", strip=True)
            else:
                text_content = content

            file_name = f"{ticker}_{accession_number}.txt"
            file_path = os.path.join(self.filings_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_content)
                
            return file_path
        except Exception as e:
            self.logger.warning(f"Failed to download/extract doc from {url}: {e}")
            return None
