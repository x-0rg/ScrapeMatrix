import os
import sys

# Ensure src in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from scrapematrix.data.db_session import init_db
from scrapematrix.scrapers.news_scraper import NewsScraper
from scrapematrix.scrapers.sec_scraper import SECScraper

def main():
    print("Initializing Database...")
    init_db()
    print("Database initialized successfully.")

    ticker = "AAPL"
    
    print(f"\nTesting News Scraper for {ticker}...")
    news_scraper = NewsScraper()
    articles = news_scraper.scrape(ticker, max_articles=2)
    for a in articles:
        print(f"Title: {a.title}")
        print(f"Link: {a.link}")
        print(f"Content Length: {len(a.content) if a.content else 0} chars")

    print(f"\nTesting SEC Scraper for {ticker}...")
    sec_scraper = SECScraper()
    filings = sec_scraper.scrape(ticker, limit=2)
    for f in filings:
        print(f"Form: {f.form_type} on {f.filing_date}")
        print(f"URL: {f.primary_document_url}")
        print(f"Local text file: {f.local_file_path}")

if __name__ == "__main__":
    main()
