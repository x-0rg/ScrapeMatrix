# 🏗️ Architecture Documentation

Comprehensive guide to ScrapeMatrix's architecture and design patterns.

## 📐 System Architecture

### High-Level System Design

```
┌──────────────────────────────────────────────────────────┐
│                 ScrapeMatrix Application                  │
├──────────────────────────────────────────────────────────┤
│                                                            │
│  ┌─────────────────────────────────────────────────────┐ │
│  │               GUI Layer (PyQt6)                      │ │
│  │  ┌─────────────┐      ┌──────────────────────────┐  │ │
│  │  │  MainWindow │      │  Stock Viewer Widget     │  │ │
│  │  ├─────────────┤      ├──────────────────────────┤  │ │
│  │  │ Home Tab    │      │ • Exchange Selector      │  │ │
│  │  │ Tabs Layout │      │ • Ticker Input          │  │ │
│  │  └─────────────┘      │ • Period Selector       │  │ │
│  │         ▲              │ • Chart Canvas          │  │ │
│  │         │              │ • Data Tables           │  │ │
│  │         │              └──────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────┘ │
│         │                                                 │
│         │ Signals & Slots                                │
│         ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐ │
│  │             Business Logic Layer                     │ │
│  │  ┌──────────────────────────────────────────────┐   │ │
│  │  │  Background Threading                         │   │ │
│  │  │  (StockDataFetcherThread)                     │   │ │
│  │  └──────────────────────────────────────────────┘   │ │
│  └─────────────────────────────────────────────────────┘ │
│         │                                                 │
│         ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐ │
│  │              Data Access Layer                      │ │
│  │  ┌──────────────────────────────────────────────┐   │ │
│  │  │  StockDataLoader                             │   │ │
│  │  │  • fetch_stock_data()                        │   │ │
│  │  │  • get_stock_info()                          │   │ │
│  │  └──────────────────────────────────────────────┘   │ │
│  │  ┌──────────────────────────────────────────────┐   │ │
│  │  │  TickerSuggestions                           │   │ │
│  │  │  • search()                                  │   │ │
│  │  │  • get_exchanges()                           │   │ │
│  │  └──────────────────────────────────────────────┘   │ │
│  └─────────────────────────────────────────────────────┘ │
│         │                                                 │
│         ▼                                                 │
│  ┌─────────────────────────────────────────────────────┐ │
│  │           External APIs & Services                  │ │
│  │  • Yahoo Finance API (yfinance)                      │ │
│  │  • Real-time Stock Data                             │ │
│  │  • Historical Data                                  │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## 📦 Module Structure

### Source Organization

```
src/scrapematrix/
│
├── __main__.py                  # Application entry point
│   ├─ Logging configuration
│   ├─ Application initialization
│   └─ Error handling
│
├── __init__.py                  # Package initialization
│   ├─ Version information
│   ├─ Author metadata
│   └─ Public exports
│
├── core/                        # Core functionality
│   └── __init__.py             # Core module
│
├── data/                        # Data layer
│   ├── __init__.py             # Data module exports
│   ├── loaders.py              # Stock data loading
│   │   ├─ StockDataLoader class
│   │   ├─ fetch_stock_data()
│   │   └─ get_stock_info()
│   │
│   └── ticker_suggestions.py   # Ticker search & exchange info
│       ├─ TickerSuggestions class
│       ├─ EXCHANGE_INFO dict
│       ├─ ALL_TICKERS list
│       └─ 30 global exchanges
│
├── gui/                         # GUI components
│   ├── __init__.py             # GUI exports
│   ├── main_window.py          # Main application window
│   │   ├─ MainWindow class
│   │   ├─ Home tab
│   │   └─ Stock Viewer tab
│   │
│   └── widgets/                # UI widgets
│       ├── __init__.py         # Widget exports
│       └── stock_viewer.py     # Stock viewer component
│           ├─ StockViewer widget
│           ├─ DynamicTickerCompleter
│           ├─ StockDataFetcherThread
│           └─ [All UI elements]
│
├── models/                      # Data models
│   └── __init__.py             # Models (future)
│
└── scrapers/                    # Web scrapers
    └── __init__.py             # Scrapers (future)
```

---

## 🔄 Data Flow

### Stock Data Fetching Flow

```
User Input
    │
    ├─ Selects Exchange
    ├─ Enters Ticker Symbol
    ├─ Selects Time Period
    │
    ▼
┌──────────────────────┐
│   fetch_stock()      │
│   (Main Thread)      │
└──────────────────────┘
    │
    ├─ Validate input
    │
    ▼
┌──────────────────────┐
│  StockDataFetcher    │
│  Thread.start()      │
│  (Background)        │
└──────────────────────┘
    │
    ├─ StockDataLoader.fetch_stock_data()
    ├─ StockDataLoader.get_stock_info()
    │
    ▼
┌──────────────────────┐
│   Yahoo Finance API  │
│   (External)         │
└──────────────────────┘
    │
    ├─ Return DataFrame
    ├─ Return Info Dict
    │
    ▼
┌──────────────────────┐
│   data_fetched       │
│   Signal (pyqtSignal)│
└──────────────────────┘
    │
    ▼
┌──────────────────────┐
│ on_data_fetched()    │
│ (Main Thread)        │
└──────────────────────┘
    │
    ├─ plot_chart()
    ├─ update_info_table()
    ├─ update_data_table()
    │
    ▼
┌──────────────────────┐
│   UI Updated         │
│   (Charts & Tables)  │
└──────────────────────┘
```

---

## 🧵 Threading Model

### Non-Blocking UI Design

```
┌─────────────────────────────────────────────┐
│         Main Thread (UI Thread)             │
├─────────────────────────────────────────────┤
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  User Interaction                  │     │
│  │  • Click buttons                   │     │
│  │  • Type text                       │     │
│  │  • Select items                    │     │
│  └────────────────────────────────────┘     │
│         │                                    │
│         ├─ Validate input                   │
│         │                                    │
│         ├─ Create worker thread             │
│         │                                    │
│         └─ Return immediately (UI responsive)
│                                              │
└─────────────────────────────────────────────┘
                │
                │ worker.start()
                │
┌─────────────────────────────────────────────┐
│    Background Thread (Worker Thread)        │
├─────────────────────────────────────────────┤
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  Long-Running Operations           │     │
│  │  • Fetch stock data                │     │
│  │  • API calls                       │     │
│  │  • Data processing                 │     │
│  └────────────────────────────────────┘     │
│         │                                    │
│         ├─ Process data                     │
│         │                                    │
│         └─ Emit signal with results         │
│                                              │
└─────────────────────────────────────────────┘
                │
                │ data_fetched.emit()
                │
         Main Thread
         (Qt Signal Slot)
         ├─ Thread-safe
         ├─ Automatic marshalling
         └─ UI update
```

---

## 🎯 Design Patterns Used

### 1. Model-View-Controller (MVC)

- **Model:** Data classes, TickerSuggestions, StockDataLoader
- **View:** PyQt6 widgets (MainWindow, StockViewer, tables, charts)
- **Controller:** Signal/slot connections, event handlers

### 2. Observer Pattern

```python
# Signal/Slot mechanism (PyQt6 Observer)
data_fetched = pyqtSignal(pd.DataFrame, dict)
data_fetched.connect(on_data_fetched)  # Observer
```

### 3. Thread Pool Pattern

```python
# Background worker threads
thread = StockDataFetcherThread(ticker, period)
thread.finished.connect(on_fetch_finished)
thread.start()
```

### 4. Strategy Pattern

```python
# Different data fetching strategies
StockDataLoader.fetch_stock_data()  # Yahoo Finance strategy
```

### 5. Singleton Pattern

```python
# Single instances (implicit)
MainWindow()  # Single main window
```

---

## 📊 Key Classes

### MainWindow
**File:** `gui/main_window.py`

```python
class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        """Initialize main window with home and stock viewer tabs."""
    
    def _create_home_tab(self) -> None:
        """Create home tab with feature overview."""
```

**Responsibilities:**
- Application window management
- Tab organization
- Widget initialization

---

### StockViewer
**File:** `gui/widgets/stock_viewer.py`

```python
class StockViewer(QWidget):
    """Stock data viewer with chart and information."""
    
    def __init__(self):
        """Initialize stock viewer widget."""
    
    def fetch_stock(self) -> None:
        """Fetch stock data from Yahoo Finance."""
    
    def on_data_fetched(self, data, info) -> None:
        """Handle successfully fetched data."""
    
    def plot_chart(self) -> None:
        """Plot stock price chart."""
```

**Responsibilities:**
- Stock data UI
- Data fetching coordination
- Chart visualization
- Table updates

---

### StockDataFetcherThread
**File:** `gui/widgets/stock_viewer.py`

```python
class StockDataFetcherThread(QThread):
    """Background thread for fetching stock data."""
    
    finished = pyqtSignal()
    error = pyqtSignal(str)
    data_fetched = pyqtSignal(pd.DataFrame, dict)
    
    def run(self) -> None:
        """Fetch stock data in background."""
```

**Responsibilities:**
- Background data fetching
- Error handling
- Signal emission

---

### StockDataLoader
**File:** `data/loaders.py`

```python
class StockDataLoader:
    """Load stock data from Yahoo Finance."""
    
    @staticmethod
    def fetch_stock_data(ticker: str, period: str) -> Optional[pd.DataFrame]:
        """Fetch historical stock data."""
    
    @staticmethod
    def get_stock_info(ticker: str) -> dict:
        """Fetch stock metadata and financial info."""
```

**Responsibilities:**
- Yahoo Finance API communication
- Data retrieval
- Error handling

---

### TickerSuggestions
**File:** `data/ticker_suggestions.py`

```python
class TickerSuggestions:
    """Manage ticker suggestions and search."""
    
    @staticmethod
    def get_exchanges() -> List[str]:
        """Get list of available exchanges."""
    
    @staticmethod
    def search(query: str) -> List[str]:
        """Search for matching tickers."""
    
    @staticmethod
    def get_currency(exchange: str) -> str:
        """Get currency for exchange."""
```

**Responsibilities:**
- Ticker database management
- Exchange information
- Autocomplete support

---

## 🔌 Signal & Slot Connections

### Main Signal Flow

```python
# Initialization
self.fetch_button.clicked.connect(self.fetch_stock)
self.ticker_input.textChanged.connect(self.on_ticker_text_changed)
self.exchange_combo.currentIndexChanged.connect(self.on_exchange_changed)

# Threading
self.fetch_thread.data_fetched.connect(self.on_data_fetched)
self.fetch_thread.error.connect(self.on_fetch_error)
self.fetch_thread.finished.connect(self.on_fetch_finished)
```

---

## 🔐 Error Handling

### Multi-Level Error Handling

```
User Input
    │
    ├─ Validation Error ──► QMessageBox
    │
    ▼
API Call
    │
    ├─ Connection Error ──► Logging + UI Message
    │
    ├─ Data Error ──► Retry + Fallback
    │
    ▼
UI Update
    │
    ├─ Display Error ──► Logging + Graceful Degradation
    │
    ▼
Success
```

---

## 📈 Data Processing Pipeline

### From API to UI

```
1. Fetch (yfinance API)
   └─ DataFrame (OHLCV data)

2. Validate
   └─ Check data completeness
   └─ Handle missing values

3. Transform
   └─ Format for display
   └─ Calculate metrics

4. Display
   └─ Charts
   └─ Tables
   └─ Info panels
```

---

## 🎨 UI Component Hierarchy

```
QApplication
    │
    └─ MainWindow (QMainWindow)
        │
        ├─ Central Widget (QWidget)
        │  │
        │  └─ QTabWidget
        │      │
        │      ├─ Home Tab (QWidget)
        │      │  └─ QLabel
        │      │
        │      └─ Stock Viewer Tab
        │         │
        │         ├─ StockViewer (QWidget)
        │         │  │
        │         │  ├─ Input Section (QHBoxLayout)
        │         │  │  ├─ Exchange Selector (QComboBox)
        │         │  │  ├─ Ticker Input (QLineEdit)
        │         │  │  ├─ Period Selector (QComboBox)
        │         │  │  └─ Fetch Button (QPushButton)
        │         │  │
        │         │  ├─ Progress Bar (QProgressBar)
        │         │  │
        │         │  ├─ Status Label (QLabel)
        │         │  │
        │         │  └─ QTabWidget (Data Tabs)
        │         │     │
        │         │     ├─ Chart Tab
        │         │     │  └─ FigureCanvas (matplotlib)
        │         │     │
        │         │     ├─ Stock Info Tab
        │         │     │  └─ QTableWidget
        │         │     │
        │         │     └─ Historical Data Tab
        │         │        └─ QTableWidget
        │         │
        │         └─ Completer (QCompleter)
        │            └─ Model (QStringListModel)
```

---

## 🔄 State Management

### Application State

```
┌──────────────────────┐
│   Idle State         │
│  (No data loading)   │
└──────────────────────┘
         │
         ├─ User clicks "Fetch Data"
         │
         ▼
┌──────────────────────┐
│   Loading State      │
│  (Data fetching)     │
│  • Progress bar on   │
│  • Button disabled   │
│  • Status: "Fetching │
└──────────────────────┘
         │
         ├─ Success
         │  └─ Data received
         │
         ├─ Error
         │  └─ Show error message
         │
         ▼
┌──────────────────────┐
│   Data State         │
│  (Data loaded)       │
│  • Charts displayed  │
│  • Tables populated  │
│  • Button enabled    │
└──────────────────────┘
```

---

## 🚀 Performance Considerations

### Optimization Strategies

1. **Threading**
   - UI remains responsive
   - No blocking operations

2. **Lazy Loading**
   - Data fetched on demand
   - Tables shown last 50 rows

3. **Caching** (Future)
   - Cache recent queries
   - Reduce API calls

4. **Batch Operations**
   - Multiple indicators calculated together
   - Minimal data copies

---

## 🔗 Dependencies & Imports

### Internal Dependencies

```
main_window.py
    ├─ gui/widgets (StockViewer)
    └─ gui/__init__ (exports)

stock_viewer.py
    ├─ data/loaders (StockDataLoader)
    ├─ data/ticker_suggestions (TickerSuggestions)
    └─ PyQt6 (GUI components)

__main__.py
    ├─ gui/main_window (MainWindow)
    └─ PyQt6 (Application)
```

### External Dependencies

```
PyQt6          ─► GUI framework
Pandas         ─► Data processing
Matplotlib     ─► Visualization
yfinance       ─► Stock data source
```

---

## 📝 Code Organization Principles

### S.O.L.I.D. Principles

- **Single Responsibility:** Each class has one purpose
- **Open/Closed:** Extensible for new features
- **Liskov Substitution:** Interfaces well-defined
- **Interface Segregation:** Focused interfaces
- **Dependency Inversion:** Depends on abstractions

### Best Practices

- ✅ Type hints throughout
- ✅ Comprehensive docstrings
- ✅ Error handling
- ✅ Logging
- ✅ PEP 8 compliance

---

## 🎯 Next Steps for Developers

1. **Understand the Flow**
   - Read this architecture doc
   - Trace a stock fetch through the code

2. **Explore the Code**
   - Start with `__main__.py`
   - Follow imports to understand structure

3. **Make Changes**
   - Follow existing patterns
   - Maintain threading model
   - Keep UI responsive

4. **Test Changes**
   - Test with different tickers
   - Test error scenarios
   - Check UI responsiveness

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
