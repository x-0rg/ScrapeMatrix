from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from scrapematrix.models.base_models import Base

class StockInfo(Base):
    __tablename__ = "stock_info"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(20), unique=True, index=True, nullable=False)
    company_name = Column(String(255), nullable=True)
    sector = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True)
    market_cap = Column(Float, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(20), index=True, nullable=False)
    title = Column(String(500), nullable=False)
    publisher = Column(String(100), nullable=True)
    link = Column(String(1000), unique=True, nullable=False)
    published_at = Column(DateTime, nullable=True)
    content = Column(Text, nullable=True)
    sentiment_score = Column(Float, nullable=True) # Optional future use
    created_at = Column(DateTime, default=datetime.utcnow)

class SECRelease(Base):
    __tablename__ = "sec_releases"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(20), index=True, nullable=False)
    cik = Column(String(20), index=True, nullable=False)
    form_type = Column(String(20), nullable=False) # e.g. 10-K, 10-Q
    filing_date = Column(DateTime, nullable=False)
    accession_number = Column(String(100), unique=True, nullable=False)
    primary_document_url = Column(String(1000), nullable=False)
    local_file_path = Column(String(500), nullable=True) # Path to downloaded HTM/TXT
    created_at = Column(DateTime, default=datetime.utcnow)
