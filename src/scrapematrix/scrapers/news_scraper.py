import yfinance as yf
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from scrapematrix.scrapers.base_scraper import BaseScraper
from scrapematrix.data.db_session import get_db_session
from scrapematrix.models.stock_models import NewsArticle

class NewsScraper(BaseScraper):
    """Scrapes latest news for a given ticker and attempts full-text extraction."""

    def __init__(self):
        super().__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/119.0.0.0 Safari/537.36"
        }

    def scrape(self, ticker: str, max_articles: int = 15):
        """
        Scrapes news from Yahoo Finance for a ticker and stores in DB.
        """
        self.logger.info(f"Starting news scrape for {ticker}")
        stock = yf.Ticker(ticker)
        news_data = stock.news

        if not news_data:
            self.logger.warning(f"No news found for {ticker} via yfinance.")
            return []

        articles_processed = []

        with get_db_session() as session:
            for item in news_data[:max_articles]:
                link = item.get("link")
                title = item.get("title")
                publisher = item.get("publisher")
                provider_publish_time = item.get("providerPublishTime")

                if not link or not title:
                    continue

                # Check if article already exists
                existing = session.query(NewsArticle).filter_by(link=link).first()
                if existing:
                    self.logger.info(f"Article already exists: {title}")
                    articles_processed.append(existing)
                    continue

                published_at = None
                if provider_publish_time:
                    published_at = datetime.fromtimestamp(provider_publish_time)

                # Attempt full-text scrape
                content = self._scrape_article_text(link)

                article = NewsArticle(
                    ticker=ticker,
                    title=title,
                    publisher=publisher,
                    link=link,
                    published_at=published_at,
                    content=content
                )
                session.add(article)
                articles_processed.append(article)
                self.logger.info(f"Saved new article: {title}")

        return articles_processed

    def _scrape_article_text(self, url: str) -> str:
        """
        Attempts to fetch and parse the text content of an article URL.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Simple heuristic: find all paragraphs
            paragraphs = soup.find_all('p')
            text = "\n".join([p.get_text().strip() for p in paragraphs if len(p.get_text().strip()) > 20])
            return text if text else None
        except requests.exceptions.RequestException as e:
            self.logger.warning(f"Failed to fetch article text from {url}: {e}")
            return None
