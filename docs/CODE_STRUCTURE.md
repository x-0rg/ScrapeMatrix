# 📂 Code Structure Documentation

Detailed guide to ScrapeMatrix's codebase organization and file structure.

## 🗂️ Complete Directory Tree

```
ScrapeMatrix/
│
├── .git/                          # Git repository
├── .venv/                         # Virtual environment
├── .vs/                           # Visual Studio cache
├── .gitignore                     # Git ignore rules
├── LICENSE                        # MIT License
│
├── 📄 pyproject.toml              # Project configuration
├── 📄 README.md                   # Project readme
├── 📄 run.ps1                     # PowerShell launcher
│
├── docs/                          # Documentation (you are here!)
│   ├── README.md                 # Documentation index
│   ├── QUICKSTART.md             # Quick start guide
│   ├── INSTALLATION.md           # Installation guide
│   ├── PROJECT_OVERVIEW.md       # Project overview
│   ├── ARCHITECTURE.md           # Architecture guide
│   ├── CODE_STRUCTURE.md         # This file
│   ├── API_REFERENCE.md          # API documentation
│   ├── MODULES.md                # Module details
│   ├── USER_GUIDE.md             # User guide
│   ├── FEATURES.md               # Features overview
│   ├── EXCHANGES.md              # Exchanges reference
│   ├── DEVELOPMENT.md            # Development guide
│   ├── TESTING.md                # Testing guide
│   ├── STYLING_GUIDE.md          # Code style
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md        # Code of conduct
│   ├── DEPLOYMENT.md             # Deployment guide
│   ├── RELEASE_NOTES.md          # Version history
│   ├── ROADMAP.md                # Future roadmap
│   ├── FAQ.md                    # Frequently asked questions
│   ├── TROUBLESHOOTING.md        # Troubleshooting guide
│   └── snaps/                    # Screenshots and diagrams
│
├── src/                           # Source code
│   └── scrapematrix/             # Main package
│       │
│       ├── __init__.py           # Package initialization
│       ├── __main__.py           # Entry point
│       │
│       ├── core/                 # Core functionality
│       │   └── __init__.py      # Core module
│       │
│       ├── data/                 # Data layer
│       │   ├── __init__.py      # Data exports
│       │   ├── loaders.py       # Stock data loading
│       │   └── ticker_suggestions.py  # Ticker search & exchanges
│       │
│       ├── gui/                  # GUI components
│       │   ├── __init__.py      # GUI exports
│       │   ├── main_window.py   # Main window
│       │   └── widgets/         # GUI widgets
│       │       ├── __init__.py # Widget exports
│       │       └── stock_viewer.py  # Stock viewer
│       │
│       ├── models/               # Data models
│       │   └── __init__.py      # Models (future)
│       │
│       └── scrapers/             # Web scrapers
│           └── __init__.py      # Scrapers (future)
│
├── tests/                         # Test suite
│   ├── test_loaders.py          # Loader tests
│   ├── test_ticker_suggestions.py # Ticker tests
│   ├── test_stock_viewer.py     # UI tests
│   └── conftest.py              # Pytest configuration
│
├── requirements/                  # Dependency specifications
│   ├── base.txt                 # Core dependencies
│   ├── dev.txt                  # Development dependencies
│   └── prod.txt                 # Production dependencies
│
├── packaging/                     # Packaging files
│   ├── setup.py                 # Setup script
│   └── MANIFEST.in              # Package manifest
│
├── watchlists/                    # Watchlist data (future)
│   └── sample_watchlist.json    # Example watchlist
│
├── models/                        # ML models (future)
│   └── README.md               # Models info
│
├── extern/                        # External resources
│   └── README.md               # External resources info
│
└── .github/                       # GitHub files (future)
    ├── workflows/               # CI/CD workflows
    └── ISSUE_TEMPLATE/         # Issue templates
```

---

## 📄 File Descriptions

### Root Files

#### `pyproject.toml`
**Purpose:** Project configuration (PEP 517/518)

**Contents:**
- Build system configuration
- Project metadata (name, version, description)
- Dependencies specification
- Package discovery settings
- Entry points

**Key Sections:**
```toml
[build-system]       # Build tool configuration
[project]           # Project metadata
[project.scripts]   # CLI entry points
[tool.setuptools]   # Setuptools configuration
```

#### `README.md`
**Purpose:** Project overview and quick reference

**Contents:**
- Project description
- Key features
- Quick start
- Screenshots
- Links to documentation

#### `run.ps1`
**Purpose:** PowerShell launcher script

**Features:**
- Environment checking
- Dependency verification
- Application launching
- Error handling

---

### Source Code Files

#### `src/scrapematrix/__init__.py`
**Purpose:** Package initialization

**Exports:**
```python
__version__ = "0.1.0"
__author__ = "ScrapeMatrix Contributors"
__all__ = ["__version__", "__author__"]
```

**Purpose:**
- Version definition
- Package metadata
- Module exports

---

#### `src/scrapematrix/__main__.py`
**Purpose:** Application entry point

**Key Functions:**
- `setup_logging()` - Configure logging
- `main()` - Application initialization and launch

**Features:**
- Logging configuration
- Exception handling
- Application initialization
- GUI launching

---

### Data Layer (`data/`)

#### `data/loaders.py`
**Purpose:** Stock data fetching and processing

**Classes:**
- `StockDataLoader` - Main data loading class

**Key Methods:**
```python
@staticmethod
def fetch_stock_data(ticker, period, interval) -> Optional[pd.DataFrame]:
    """Fetch historical stock data from Yahoo Finance."""

@staticmethod
def get_stock_info(ticker) -> dict:
    """Fetch stock metadata and financial information."""
```

**Dependencies:**
- `yfinance` - Yahoo Finance API
- `pandas` - Data processing

---

#### `data/ticker_suggestions.py`
**Purpose:** Ticker search and exchange information

**Classes:**
- `TickerSuggestions` - Ticker management

**Key Data:**
```python
EXCHANGE_INFO = {...}  # 30 global exchanges
ALL_TICKERS = [...]    # 750+ ticker symbols
POPULAR_TICKERS = [...] # Most popular stocks
```

**Key Methods:**
```python
@staticmethod
def get_exchanges() -> List[str]:
    """Get all available exchanges."""

@staticmethod
def search(query: str) -> List[str]:
    """Search for matching tickers."""

@staticmethod
def get_currency(exchange: str) -> str:
    """Get currency for exchange."""
```

---

### GUI Layer (`gui/`)

#### `gui/main_window.py`
**Purpose:** Main application window

**Classes:**
- `MainWindow` - Main application window (QMainWindow)

**Features:**
- Tabbed interface
- Home tab with feature overview
- Stock Viewer tab
- Window configuration

---

#### `gui/widgets/stock_viewer.py`
**Purpose:** Stock viewer widget and related components

**Classes:**

##### `DynamicTickerCompleter`
- Custom QCompleter with dynamic filtering
- Real-time ticker suggestions
- Exchange-specific filtering

##### `StockDataFetcherThread`
- Background worker thread
- Non-blocking data fetching
- Signal emission for UI updates

##### `StockViewer`
- Main stock viewer widget
- UI components (inputs, charts, tables)
- Data display and visualization
- Event handling

**Key Methods:**
```python
def init_ui(self) -> None:
    """Initialize user interface."""

def fetch_stock(self) -> None:
    """Fetch stock data."""

def plot_chart(self) -> None:
    """Plot price chart."""

def update_info_table(self) -> None:
    """Update company information table."""

def update_data_table(self) -> None:
    """Update historical data table."""
```

---

## 📊 Code Statistics

### File Counts
```
Python Files:        12
Documentation:       20
Config Files:        3
Test Files:          3
Total:              38
```

### Lines of Code (Approximate)
```
Source Code:        2000+
Tests:             500+
Documentation:     5000+
Comments:          300+
```

---

## 🔄 File Dependencies

### Import Dependency Graph

```
__main__.py
    ├─ gui.main_window
    │   └─ gui.widgets
    │       └─ data.loaders
    │       └─ data.ticker_suggestions
    │
    └─ PyQt6

gui/widgets/stock_viewer.py
    ├─ data.loaders
    ├─ data.ticker_suggestions
    ├─ pandas
    └─ PyQt6

data/loaders.py
    ├─ yfinance
    ├─ pandas
    └─ logging

data/ticker_suggestions.py
    ├─ typing
    └─ logging
```

---

## 📦 Module Organization

### `scrapematrix` Package Structure

```
scrapematrix (namespace package)
│
├─ __init__
│  └─ Package metadata
│
├─ core (core functionality)
│  └─ (Future functionality)
│
├─ data (data access layer)
│  ├─ loaders (Stock data fetching)
│  └─ ticker_suggestions (Ticker database)
│
├─ gui (presentation layer)
│  ├─ main_window (Main window)
│  └─ widgets (UI components)
│
├─ models (data models)
│  └─ (Future models)
│
└─ scrapers (web scrapers)
   └─ (Future scrapers)
```

---

## 🎯 Module Responsibilities

### Core Module (`core/`)
**Current Status:** Placeholder for future functionality

**Future Purpose:**
- Core business logic
- Shared utilities
- Common functions

---

### Data Module (`data/`)
**Responsibility:** Data access and processing

**Components:**
- **loaders.py** - Fetch data from external sources
- **ticker_suggestions.py** - Manage ticker information

**Key Responsibilities:**
- API communication
- Data validation
- Error handling
- Caching (future)

---

### GUI Module (`gui/`)
**Responsibility:** User interface components

**Components:**
- **main_window.py** - Main application window
- **widgets/stock_viewer.py** - Stock viewer component

**Key Responsibilities:**
- UI layout and design
- Event handling
- User interaction
- Data visualization

---

### Models Module (`models/`)
**Current Status:** Placeholder for future functionality

**Future Purpose:**
- Data transfer objects
- Business entities
- Data validation models

---

### Scrapers Module (`scrapers/`)
**Current Status:** Placeholder for future functionality

**Future Purpose:**
- Web scraping functionality
- Data collection
- News aggregation

---

## 🔐 Access Patterns

### Public Interfaces

#### Data Module
```python
from scrapematrix.data import StockDataLoader, TickerSuggestions

# Usage
data = StockDataLoader.fetch_stock_data("AAPL", "1y")
tickers = TickerSuggestions.search("AA")
```

#### GUI Module
```python
from scrapematrix.gui import MainWindow

# Usage
window = MainWindow()
window.show()
```

---

## 📈 Code Quality Metrics

### Current Status
```
Type Hints:         85%+ coverage
Docstrings:         95%+ coverage
PEP 8 Compliance:   ✅ Full
Import Organization: ✅ Proper
Circular Dependencies: ❌ None
```

---

## 🔄 Naming Conventions

### Python Naming
```python
# Modules: lowercase_with_underscores
stock_viewer.py
ticker_suggestions.py

# Classes: PascalCase
class StockDataLoader:
    pass

class StockViewer(QWidget):
    pass

# Functions/Methods: lowercase_with_underscores
def fetch_stock_data():
    pass

def update_info_table():
    pass

# Constants: UPPERCASE_WITH_UNDERSCORES
EXCHANGE_INFO = {...}
ALL_TICKERS = [...]

# Private: _lowercase_with_underscore
def _validate_input():
    pass
```

---

## 🔗 Circular Dependency Prevention

### Dependency Flow (Unidirectional)
```
GUI
  ↓ (depends on)
Data
  ↓ (depends on)
External APIs

(No circular dependencies)
```

---

## 📝 Documentation Locations

### Code Documentation
- **Docstrings:** In each module/class/method
- **Type Hints:** Function signatures
- **Comments:** Complex logic sections

### External Documentation
- **User Guide:** `/docs/USER_GUIDE.md`
- **API Docs:** `/docs/API_REFERENCE.md`
- **Architecture:** `/docs/ARCHITECTURE.md`

---

## 🚀 Adding New Files

### Guidelines

1. **Location**
   - Determine appropriate module
   - Follow existing structure

2. **Naming**
   - Use snake_case for filenames
   - Use PascalCase for class names
   - Use lowercase_underscore for functions

3. **Structure**
   - Module docstring at top
   - Imports organized (stdlib, third-party, local)
   - Class/function definitions
   - __all__ for public exports

4. **Documentation**
   - Docstring for module
   - Docstring for each class
   - Docstring for public methods

---

## 🎓 Understanding the Codebase

### Reading Order
1. **Entry Point:** `__main__.py`
2. **Main Window:** `gui/main_window.py`
3. **Stock Viewer:** `gui/widgets/stock_viewer.py`
4. **Data Loaders:** `data/loaders.py`
5. **Ticker Suggestions:** `data/ticker_suggestions.py`

### Key Concepts to Understand
1. Threading model
2. Signal/slot connections
3. Pandas DataFrames
4. Matplotlib charts
5. PyQt6 widgets

---

## 🔍 Finding Things

### Common Searches
```
# Find class definition
grep -r "class ClassName" src/

# Find function
grep -r "def function_name" src/

# Find import
grep -r "from module import" src/

# Find constant
grep -r "CONSTANT_NAME" src/
```

---

## 📊 Module Relationships

```
┌─────────────────┐
│  __main__.py    │
│  (Entry Point)  │
└────────┬────────┘
         │
    creates
         │
         ▼
┌─────────────────────────┐
│  MainWindow             │
│  (Main Application)     │
└────────┬────────────────┘
         │
    contains
         │
         ▼
┌─────────────────────────┐
│  StockViewer Widget     │
│  (Data Viewer)          │
└────────┬────────────────┘
         │
    uses
         │
         ▼
┌──────────────────────────────────┐
│  StockDataLoader                 │
│  TickerSuggestions               │
│  (Data Layer)                    │
└──────────────────────────────────┘
         │
    communicates with
         │
         ▼
┌──────────────────────────────────┐
│  Yahoo Finance API               │
│  (External Data)                 │
└──────────────────────────────────┘
```

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
