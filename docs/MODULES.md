# 📚 Module Documentation

Detailed documentation of ScrapeMatrix modules and components.

## 🗂️ Module Overview

```
scrapematrix/
├── core/               # Core functionality (future)
├── data/              # Data access layer
│   ├── loaders.py     # Stock data loading
│   └── ticker_suggestions.py  # Ticker database
├── gui/               # User interface layer
│   ├── main_window.py # Main application window
│   └── widgets/
│       └── stock_viewer.py  # Stock viewer widget
├── models/            # Data models (future)
└── scrapers/          # Web scrapers (future)
```

---

## 📦 Core Module (core/)

**Status:** Placeholder for future functionality

**Purpose:** Core business logic and shared utilities

**Future Components:**
- Configuration management
- Caching system
- Utility functions
- Constants and enums

---

## 🗄️ Data Module (data/)

The data layer handles all external data access and processing.

### loaders.py - Stock Data Loading

**Class: `StockDataLoader`**

Static class for loading stock data from Yahoo Finance.

#### Methods:

##### `fetch_stock_data(ticker, period, interval) -> Optional[pd.DataFrame]`

Fetch historical stock data for a symbol.

**Parameters:**
- `ticker` (str): Stock ticker symbol (e.g., 'AAPL')
- `period` (str): Time period ('1mo', '3mo', '6mo', '1y', '2y', '5y', 'max')
- `interval` (str): Data interval, default '1d' (daily)

**Returns:**
- DataFrame with columns: Date, Open, High, Low, Close, Volume
- None if fetch fails

**Example:**
```python
from scrapematrix.data import StockDataLoader
data = StockDataLoader.fetch_stock_data('AAPL', '1y')
print(data.head())
```

**Error Handling:**
- Returns None on API errors
- Logs errors for debugging
- No exceptions raised

---

##### `get_stock_info(ticker) -> dict`

Fetch company information and financial metrics.

**Parameters:**
- `ticker` (str): Stock ticker symbol

**Returns:**
- Dictionary with keys: name, sector, industry, market_cap, p_e_ratio, etc.
- Empty dict if fetch fails

**Example:**
```python
info = StockDataLoader.get_stock_info('AAPL')
print(f"Market Cap: ${info.get('market_cap'):,}")
```

---

### ticker_suggestions.py - Ticker Database

**Data Structures:**

#### `EXCHANGE_INFO` Dictionary
Contains information about 30 global exchanges.

**Structure:**
```python
EXCHANGE_INFO = {
    "NASDAQ": {
        "currency": "USD",
        "currency_symbol": "$",
        "country": "United States",
        "region": "North America",
        "timezone": "EST",
        "market_hours": "9:30-16:00",
        "sample_tickers": ["AAPL", "MSFT", "GOOGL", ...],
    },
    # ... 29 more exchanges
}
```

#### `ALL_TICKERS` List
Contains 750+ ticker symbols (updated periodically).

#### `POPULAR_TICKERS` List
Most popular/traded stocks (20 tickers).

---

**Class: `TickerSuggestions`**

Static class for ticker search and exchange information.

#### Methods:

##### `get_exchanges() -> List[str]`

Get all available exchanges.

**Returns:** List of exchange names

**Example:**
```python
exchanges = TickerSuggestions.get_exchanges()
print(f"Available: {len(exchanges)} exchanges")
```

---

##### `search(query, exchange=None) -> List[str]`

Search for matching tickers.

**Parameters:**
- `query` (str): Search string (ticker prefix)
- `exchange` (str, optional): Filter by exchange

**Returns:** List of matching tickers

**Example:**
```python
results = TickerSuggestions.search("AAP")
# Returns: ['AAPL', 'AAPP', ...]

results = TickerSuggestions.search("AAP", exchange="NASDAQ")
```

---

##### `get_currency(exchange) -> str`

Get currency name for exchange.

**Returns:** Currency code (e.g., 'USD', 'EUR', 'JPY')

---

##### `get_currency_symbol(exchange) -> str`

Get currency symbol for exchange.

**Returns:** Symbol (e.g., '$', '€', '¥')

---

##### `get_country(exchange) -> str`

Get country name for exchange.

**Returns:** Country name

---

##### `get_region(exchange) -> str`

Get geographic region for exchange.

**Returns:** Region (e.g., 'North America', 'Europe', 'Asia Pacific')

---

##### `get_timezone(exchange) -> str`

Get timezone for exchange.

**Returns:** Timezone code (e.g., 'EST', 'CET', 'JST')

---

##### `get_market_hours(exchange) -> str`

Get trading hours for exchange.

**Returns:** Hours string (e.g., '9:30-16:00')

---

##### `get_sample_tickers(exchange, count=5) -> List[str]`

Get sample tickers for an exchange.

**Parameters:**
- `exchange` (str): Exchange name
- `count` (int): Number of samples (default: 5)

**Returns:** List of sample ticker symbols

---

## 🎨 GUI Module (gui/)

The GUI layer implements the user interface using PyQt6.

### main_window.py - Main Application Window

**Class: `MainWindow(QMainWindow)`**

Main application window with tabbed interface.

#### Attributes:
- `home_tab` (QWidget): Home tab widget
- `stock_viewer_tab` (StockViewer): Stock viewer widget

#### Methods:

##### `__init__()`

Initialize main window.

Sets up:
- Window title and size
- Tab widget
- Home tab with feature overview
- Stock Viewer tab

---

##### `_create_home_tab() -> QWidget`

Create home tab with feature overview.

**Returns:** Home tab widget

---

### widgets/stock_viewer.py - Stock Viewer Widget

**Classes:**

#### `DynamicTickerCompleter(QCompleter)`

Custom completer for dynamic ticker suggestions.

##### Methods:

`update_suggestions(text, exchange=None)`

Update suggestions based on input text and exchange.

**Parameters:**
- `text` (str): Input text
- `exchange` (str, optional): Filter by exchange

---

#### `StockDataFetcherThread(QThread)`

Background thread for fetching stock data.

##### Signals:
- `finished`: Emitted when operation complete
- `error`: Emitted on error with error message
- `data_fetched`: Emitted with data (DataFrame, info dict)

##### Methods:

`run()`

Fetch stock data in background.

**Process:**
1. Fetch historical data
2. Fetch company info
3. Emit appropriate signal

---

#### `StockViewer(QWidget)`

Main stock viewer widget.

##### Attributes:
- `stock_data` (DataFrame): Loaded stock data
- `stock_info` (dict): Company information
- `ticker_input` (QLineEdit): Ticker symbol input
- `exchange_combo` (QComboBox): Exchange selector
- `period_combo` (QComboBox): Time period selector
- `chart_canvas` (FigureCanvas): Matplotlib chart
- `info_table` (QTableWidget): Company info table
- `data_table` (QTableWidget): Historical data table

##### Key Methods:

`init_ui() -> None`

Initialize user interface components.

---

`fetch_stock() -> None`

Fetch stock data when button clicked.

**Process:**
1. Validate input
2. Show progress bar
3. Create fetcher thread
4. Start background fetch

---

`on_data_fetched(data: DataFrame, info: dict) -> None`

Handle successfully fetched data.

**Actions:**
1. Store data in memory
2. Plot chart
3. Update tables
4. Hide progress bar

---

`on_fetch_error(error_msg: str) -> None`

Handle fetch errors.

**Actions:**
1. Show error message
2. Update status bar
3. Display error dialog

---

`plot_chart() -> None`

Plot stock price chart.

**Uses:**
- Matplotlib for visualization
- Pandas DataFrame for data
- FigureCanvas for embedding

---

`update_info_table() -> None`

Populate company information table.

**Displays:**
- Company metrics
- Financial ratios
- Key statistics

---

`update_data_table() -> None`

Populate historical price data table.

**Displays:**
- Date
- OHLC prices (formatted with $)
- Last 50 trading days

---

## 🎯 Models Module (models/)

**Status:** Placeholder for future functionality

**Purpose:** Data models and transfer objects

**Planned Components:**
- Stock data model
- Company info model
- Portfolio model
- Trade model

---

## 🔪 Scrapers Module (scrapers/)

**Status:** Placeholder for future functionality

**Purpose:** Web scraping functionality

**Planned Components:**
- News scraper
- Earnings scraper
- Analyst scraper
- Economic data scraper

---

## 📊 Data Structures

### Stock DataFrame

Format returned by `StockDataLoader.fetch_stock_data()`:

```
                  Open      High       Low     Close      Volume
Date                                                              
2026-01-01  150.020004  152.080002  149.770004  151.929993  25109200
2026-01-02  152.100006  154.380005  152.050003  153.100006  30123500
...
```

**Columns:**
- **Date:** Index, trading date
- **Open:** Opening price
- **High:** Highest price of day
- **Low:** Lowest price of day  
- **Close:** Closing price
- **Volume:** Trading volume

---

### Stock Info Dictionary

Format returned by `StockDataLoader.get_stock_info()`:

```python
{
    'name': 'Apple Inc.',
    'sector': 'Technology',
    'industry': 'Consumer Electronics',
    'market_cap': 2800000000000,
    'p_e_ratio': 28.5,
    'dividend_yield': 0.005,
    'fifty_two_week_high': 165.0,
    'fifty_two_week_low': 125.0,
    'beta': 1.2,
    # ... more fields
}
```

---

## 🔄 Signal Flow

### Stock Fetching Flow

```
User clicks "Fetch Data"
    ↓
fetch_stock() validates input
    ↓
StockDataFetcherThread created & started
    ↓
Background: run() executes
    ↓
API calls made (2)
    ↓
data_fetched signal emitted
    ↓
Main thread: on_data_fetched() called
    ↓
plot_chart(), update_*_table() called
    ↓
UI updated with charts and tables
```

---

## 🔌 Dependency Diagram

```
__main__.py
    ↓
MainWindow
    ↓
StockViewer
    ├─→ StockDataFetcherThread
    │   ├─→ StockDataLoader
    │   └─→ yfinance (API)
    │
    └─→ DynamicTickerCompleter
        └─→ TickerSuggestions
```

---

## 📝 Type Hints

All modules use comprehensive type hints:

```python
from typing import Optional, List, Dict
import pandas as pd

def fetch_stock_data(
    ticker: str,
    period: str = "1y"
) -> Optional[pd.DataFrame]:
    """Fetch stock data."""
```

---

## 🎓 Module Responsibilities

| Module | Responsibility |
|--------|----------------|
| **core** | Core business logic |
| **data** | External data access |
| **gui** | User interface |
| **models** | Data representation |
| **scrapers** | Web scraping |

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
