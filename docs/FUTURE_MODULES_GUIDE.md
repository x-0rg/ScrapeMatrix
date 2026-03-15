# Future Use Cases: When You'll Need These Modules

## 📊 Quick Overview

| Module | Needed? | Timeline | Priority | Use Cases |
|--------|---------|----------|----------|-----------|
| **models/** | ✅ YES | Soon (Phase 2) | High | Data validation & schemas |
| **scrapers/** | ✅ YES | Later (Phase 3) | Medium | News, technical analysis |
| **core/** | ✅ YES | Soon (Phase 2) | Medium | Config, caching, errors |

---

## 1️⃣ `models/` - DEFINITELY NEEDED

### Timeline: **Phase 2** (Next Sprint)

### Use Cases:

#### A) **Stock Data Schema** (Immediate)
```python
# models/stock_model.py
from pydantic import BaseModel
from datetime import datetime

class StockData(BaseModel):
    """Validated stock data from Yahoo Finance."""
    ticker: str
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "ticker": "AAPL",
                "date": "2024-01-15",
                "open": 150.0,
                "high": 152.5,
                "low": 149.5,
                "close": 151.0,
                "volume": 1000000
            }
        }
```

#### B) **Company Information Schema** (Immediate)
```python
# models/company_info.py
from pydantic import BaseModel
from typing import Optional

class CompanyInfo(BaseModel):
    """Validated company information."""
    ticker: str
    name: str
    sector: Optional[str] = None
    industry: Optional[str] = None
    market_cap: Optional[float] = None
    pe_ratio: Optional[float] = None
    dividend_yield: Optional[float] = None
```

#### C) **User Preferences** (Phase 2)
```python
# models/user_preferences.py
from pydantic import BaseModel
from typing import List

class UserPreferences(BaseModel):
    """User watchlist and preferences."""
    user_id: str
    favorite_tickers: List[str]
    default_period: str = "1y"
    theme: str = "light"
    notifications_enabled: bool = True
```

#### D) **API Request/Response Models** (For RAG Phase)
```python
# models/rag_models.py
from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    """RAG query request."""
    query: str
    max_results: int = 5
    
class QueryResponse(BaseModel):
    """RAG query response."""
    query: str
    results: List[str]
    confidence: float
```

### Benefits of Using `models/`:
- ✅ **Data Validation** - Catch bad data early
- ✅ **Type Safety** - IDE autocomplete and type checking
- ✅ **Documentation** - Schema docs auto-generated
- ✅ **API Documentation** - FastAPI generates Swagger docs
- ✅ **Serialization** - Easy JSON conversion

### When to Create:
**Right now, or in Phase 2 when you start:**
- [ ] Adding database persistence
- [ ] Building REST API endpoints
- [ ] Implementing user settings
- [ ] Adding RAG features

---

## 2️⃣ `scrapers/` - YES, BUT LATER

### Timeline: **Phase 3** (2-3 Sprints Away)

### Use Cases:

#### A) **News Scraper** (Future Feature)
```python
# scrapers/news_scraper.py
from typing import List
from datetime import datetime

class NewsScraper:
    """Fetch financial news for stocks."""
    
    def scrape_news(self, ticker: str, days: int = 7) -> List[dict]:
        """Get recent news articles for ticker."""
        # Implementation using NewsAPI, finnhub, or similar
        pass
```

#### B) **Technical Analysis Scraper** (Future Feature)
```python
# scrapers/technical_scraper.py
import pandas as pd

class TechnicalAnalyzer:
    """Calculate technical indicators."""
    
    def calculate_moving_average(self, data: pd.DataFrame, window: int):
        """Calculate moving average."""
        pass
    
    def calculate_rsi(self, data: pd.DataFrame, period: int = 14):
        """Calculate RSI indicator."""
        pass
    
    def calculate_macd(self, data: pd.DataFrame):
        """Calculate MACD indicator."""
        pass
```

#### C) **Market Data Scraper** (Future Feature)
```python
# scrapers/market_scraper.py
class MarketDataScraper:
    """Get broader market data."""
    
    def get_market_indices(self) -> dict:
        """Get S&P 500, Nasdaq, Dow Jones."""
        pass
    
    def get_sector_performance(self) -> dict:
        """Get sector performance data."""
        pass
    
    def get_economic_indicators(self) -> dict:
        """Get economic data."""
        pass
```

#### D) **Web Scraper** (Future Feature)
```python
# scrapers/web_scraper.py
from bs4 import BeautifulSoup
import requests

class WebScraper:
    """Scrape financial websites."""
    
    def scrape_earnings(self, ticker: str):
        """Get earnings calendar."""
        pass
    
    def scrape_analyst_ratings(self, ticker: str):
        """Get analyst recommendations."""
        pass
```

### Benefits of Using `scrapers/`:
- ✅ **Modular** - Each scraper is independent
- ✅ **Maintainable** - Easy to update or replace sources
- ✅ **Extensible** - Add new data sources easily
- ✅ **Testable** - Mock external APIs in tests

### When to Create:
**When you start Phase 3 (in 2-3 sprints):**
- [ ] User requests news integration
- [ ] Adding technical indicators to charts
- [ ] Building portfolio tracking features
- [ ] Implementing market comparison tools

---

## 3️⃣ `core/` - YES, SOON

### Timeline: **Phase 2** (Concurrent with models)

### Use Cases:

#### A) **Configuration Management** (Very Soon)
```python
# core/config.py
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class Config:
    """Application configuration."""
    
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    FINNHUB_API_KEY: str = os.getenv("FINNHUB_API_KEY", "")
    
    # Paths
    DATA_DIR: Path = Path("./data")
    CACHE_DIR: Path = Path("./cache")
    
    # Settings
    CACHE_TTL: int = 3600  # 1 hour
    MAX_RETRIES: int = 3
```

#### B) **Caching System** (Soon - For Performance)
```python
# core/cache.py
import pickle
from datetime import datetime, timedelta
from pathlib import Path

class CacheManager:
    """Simple file-based cache."""
    
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)
    
    def get(self, key: str):
        """Get cached value if not expired."""
        cache_file = self.cache_dir / f"{key}.pkl"
        if cache_file.exists():
            return pickle.loads(cache_file.read_bytes())
        return None
    
    def set(self, key: str, value, ttl: int = 3600):
        """Cache value with TTL."""
        cache_file = self.cache_dir / f"{key}.pkl"
        cache_file.write_bytes(pickle.dumps(value))
```

#### C) **Custom Exceptions** (Soon - For Error Handling)
```python
# core/exceptions.py

class ScrapeMatrixError(Exception):
    """Base exception for ScrapeMatrix."""
    pass

class StockDataError(ScrapeMatrixError):
    """Error fetching stock data."""
    pass

class InvalidTickerError(ScrapeMatrixError):
    """Invalid stock ticker symbol."""
    pass

class APIError(ScrapeMatrixError):
    """External API error."""
    pass

class CacheError(ScrapeMatrixError):
    """Cache operation error."""
    pass
```

#### D) **Logging Configuration** (Soon - For Better Debugging)
```python
# core/logging_config.py
import logging
from pathlib import Path

def setup_logging(level: str = "INFO"):
    """Configure application logging."""
    log_dir = Path("./logs")
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger("scrapematrix")
    handler = logging.FileHandler(log_dir / "app.log")
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    
    return logger
```

#### E) **Database Connection** (Future - If Adding DB)
```python
# core/database.py
from sqlalchemy import create_engine

class DatabaseManager:
    """Handle database connections."""
    
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
    
    def get_session(self):
        """Get database session."""
        pass
```

### Benefits of Using `core/`:
- ✅ **Centralized** - All config in one place
- ✅ **DRY** - No repeated utility code
- ✅ **Testable** - Easy to mock in tests
- ✅ **Maintainable** - Change config once, applies everywhere
- ✅ **Professional** - Industry standard practice

### When to Create:
**Start Phase 2 (this sprint):**
- [ ] Adding environment variable support
- [ ] Implementing caching for API calls
- [ ] Improving error handling
- [ ] Setting up logging config file
- [ ] Planning database integration

---

## 📅 Implementation Timeline

```
PHASE 1 (Current - DONE) ✅
├─ Stock viewer with charts
├─ Ticker suggestions
├─ Basic error handling
└─ README + documentation

PHASE 2 (Next Sprint - 1-2 weeks)
├─ models/ module (data validation)
├─ core/ module (config, cache, errors, logging)
├─ Unit tests
└─ Database setup (optional)

PHASE 3 (Following Sprint - 2-3 weeks)
├─ scrapers/ module (news, technical analysis)
├─ AI agent framework
├─ RAG integration
└─ Advanced features

PHASE 4+ (Future)
├─ Portfolio tracking
├─ Market comparison
├─ Advanced indicators
└─ Mobile app (maybe)
```

---

## 🎯 Decision: Keep or Delete Now?

### OPTION A: Delete Now, Recreate Later ❌➡️✅
```bash
rm src/scrapematrix/models/__init__.py
rm src/scrapematrix/scrapers/__init__.py
rm src/scrapematrix/core/__init__.py

# In 1-2 weeks when you start Phase 2:
# Recreate with actual implementations
```

**Pros:**
- Clean project now
- Forces you to think about structure when creating
- No confusing placeholders

**Cons:**
- Need to remember to create them
- One extra step when starting Phase 2

---

### OPTION B: Keep as Placeholders ✅
```python
# Keep current files with documentation
# They document what's coming
```

**Pros:**
- Clear roadmap in code
- Quick start in Phase 2
- Documents intentions

**Cons:**
- Project feels incomplete
- Confusing for new developers
- False sense of implementation

---

## 🏆 My Recommendation

### **DELETE NOW** ❌

Here's why:

1. **Phase 2 is Close** - You'll create these in 1-2 weeks anyway
2. **Clean is Better** - Current state should reflect reality
3. **Documentation Exists** - You have docs/INIT_CLEANUP_PLAN.md explaining what goes where
4. **Developers Understand** - README clearly states what's planned

When Phase 2 starts:
```python
# Create models/__init__.py with actual code:
"""Data models for ScrapeMatrix."""
from .stock_model import StockData
from .company_info import CompanyInfo
__all__ = ["StockData", "CompanyInfo"]

# Create core/__init__.py with actual code:
"""Core utilities for ScrapeMatrix."""
from .config import Config
from .cache import CacheManager
from .exceptions import ScrapeMatrixError
__all__ = ["Config", "CacheManager", "ScrapeMatrixError"]

# scrapers/ can wait for Phase 3
```

---

## 🗂️ Final Project State (After Cleanup)

```
src/scrapematrix/
├── __init__.py              ✅ KEEP (metadata)
├── __main__.py
├── core/                    (Will add __init__.py in Phase 2)
├── data/
│   ├── __init__.py          ✅ KEEP (exports)
│   ├── loaders.py
│   └── ticker_suggestions.py
├── gui/
│   ├── __init__.py          ✅ KEEP (exports)
│   ├── main_window.py
│   └── widgets/
│       ├── __init__.py      ✅ KEEP (exports)
│       └── stock_viewer.py
├── models/                  (Will add __init__.py in Phase 2)
└── scrapers/                (Will add __init__.py in Phase 3)
```

---

## ✅ What You Should Do

1. **Delete 3 placeholder `__init__.py` files now**
2. **Keep documentation** (docs/INIT_CLEANUP_PLAN.md explains what goes where)
3. **In Phase 2**: Create `models/__init__.py` and `core/__init__.py` with actual code
4. **In Phase 3**: Create `scrapers/__init__.py` with actual code

This keeps your project clean while maintaining clear roadmap for development.

---

## 📚 Reference

When you're ready to implement each module, you have:
- ✅ Code examples above
- ✅ Use cases documented
- ✅ Timeline established
- ✅ Clear integration points

Just follow the examples and timeline above!
