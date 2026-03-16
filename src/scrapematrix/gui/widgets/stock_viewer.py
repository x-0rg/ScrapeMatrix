"""Stock viewer widget - refactored and cleaned up version."""
import logging
from typing import Optional

import pandas as pd
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QStringListModel
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QMessageBox, QProgressBar, QCompleter
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from ...data.loaders import StockDataLoader
from ...data.ticker_suggestions import TickerSuggestions

logger = logging.getLogger(__name__)


class DynamicTickerCompleter(QCompleter):
    """Dynamic ticker completer with real-time filtering."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.setMaxVisibleItems(10)
        self.setModel(QStringListModel(self))
        self.selected_exchange = None

    def update_suggestions(self, text: str, exchange: str = None) -> None:
        """Update suggestions based on input text and optional exchange filter.

        Args:
            text: Search text
            exchange: Optional exchange name to filter results
        """
        self.selected_exchange = exchange

        if not text.strip():
            # Get initial suggestions based on exchange
            if exchange:
                suggestions = TickerSuggestions.get_tickers_by_exchange(exchange)[:20]
            else:
                suggestions = TickerSuggestions.get_all_tickers()[:20]
        else:
            # Search with optional exchange filter
            suggestions = TickerSuggestions.search(text.upper(), exchange=exchange)

        self.model().setStringList(suggestions)


class StockDataFetcherThread(QThread):
    """Background thread for fetching stock data."""

    finished = pyqtSignal()
    error = pyqtSignal(str)
    data_fetched = pyqtSignal(pd.DataFrame, dict)

    def __init__(self, ticker: str, period: str, interval: str = "1d"):
        super().__init__()
        self.ticker = ticker.upper()
        self.period = period
        self.interval = interval

    def run(self):
        """Fetch stock data in background thread."""
        try:
            data = StockDataLoader.fetch_stock_data(
                self.ticker, self.period, self.interval
            )
            if data is None:
                self.error.emit(f"Could not fetch data for {self.ticker}")
                return

            info = StockDataLoader.get_stock_info(self.ticker)
            self.data_fetched.emit(data, info)

        except Exception as e:
            logger.exception(f"Error fetching stock data for {self.ticker}")
            self.error.emit(str(e))
        finally:
            self.finished.emit()


class StockViewer(QWidget):
    """Stock data viewer with chart and information displays."""

    def __init__(self):
        super().__init__()
        self.stock_data: Optional[pd.DataFrame] = None
        self.stock_info: dict = {}
        self.fetch_thread: Optional[StockDataFetcherThread] = None
        self.ticker_completer: Optional[DynamicTickerCompleter] = None
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize user interface."""
        layout = QVBoxLayout()
        layout.addLayout(self._create_input_section())

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel("🌍 Showing stocks from all countries")
        self.status_label.setStyleSheet("color: #666; font-size: 12px;")
        layout.addWidget(self.status_label)

        layout.addWidget(self._create_data_tabs())
        self.setLayout(layout)

    def _create_input_section(self) -> QHBoxLayout:
        """Create input controls layout with exchange selector."""
        layout = QHBoxLayout()

        # Exchange selector dropdown - sorted by region
        self.exchange_combo = QComboBox()
        self.exchange_combo.addItem("🌍 All Global Exchanges", None)  # Default: all exchanges

        # Sort exchanges by region for better organization
        exchanges = TickerSuggestions.get_exchanges()
        exchanges_by_region = {}

        for exchange in sorted(exchanges):
            region = TickerSuggestions.get_region(exchange)
            if region not in exchanges_by_region:
                exchanges_by_region[region] = []
            exchanges_by_region[region].append(exchange)

        # Add exchanges grouped by region
        for region in sorted(exchanges_by_region.keys()):
            for exchange in exchanges_by_region[region]:
                country = TickerSuggestions.get_country(exchange)
                display_text = f"{exchange} - {country}"
                self.exchange_combo.addItem(display_text, exchange)

        self.exchange_combo.currentIndexChanged.connect(self.on_exchange_changed)

        # Currency label (will be updated dynamically)
        self.currency_label = QLabel("Currency: --")
        self.currency_label.setStyleSheet("color: #666; font-size: 11px; font-weight: bold;")

        # Ticker input
        self.ticker_input = QLineEdit()
        self.ticker_input.setPlaceholderText("e.g., AAPL, GOOGL, MSFT (start typing)")
        self.ticker_input.returnPressed.connect(self.fetch_stock)
        self.ticker_input.textChanged.connect(self.on_ticker_text_changed)

        self.ticker_completer = DynamicTickerCompleter()
        self.ticker_input.setCompleter(self.ticker_completer)

        # Period selector
        self.period_combo = QComboBox()
        self.period_combo.addItems(["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
        self.period_combo.setCurrentText("1y")

        # Fetch button
        self.fetch_button = QPushButton("Fetch Data")
        self.fetch_button.clicked.connect(self.fetch_stock)
        self.fetch_button.setStyleSheet(
            "QPushButton { background-color: #10B981; color: white; padding: 8px; "
            "border-radius: 4px; font-weight: bold; }"
        )

        # Exchange info section (vertical layout)
        exchange_section = QVBoxLayout()
        exchange_row = QHBoxLayout()
        exchange_row.addWidget(QLabel("Exchange:"))
        exchange_row.addWidget(self.exchange_combo, 1)
        exchange_row.addWidget(self.currency_label)
        exchange_section.addLayout(exchange_row)

        # Ticker section (horizontal layout)
        ticker_section = QHBoxLayout()
        ticker_section.addWidget(QLabel("Stock Ticker:"))
        ticker_section.addWidget(self.ticker_input, 2)
        ticker_section.addWidget(QLabel("Period:"))
        ticker_section.addWidget(self.period_combo, 1)
        ticker_section.addWidget(self.fetch_button)

        # Combine sections
        layout.addLayout(exchange_section, 1)
        layout.addSpacing(20)
        layout.addLayout(ticker_section, 2)

        return layout

    def _create_data_tabs(self) -> QTabWidget:
        """Create tabbed data displays."""
        tabs = QTabWidget()

        # Chart tab
        self.chart_canvas = FigureCanvas(Figure(figsize=(10, 6)))
        tabs.addTab(self.chart_canvas, "Chart")

        # Info tab
        self.info_table = QTableWidget()
        self.info_table.setColumnCount(2)
        self.info_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.info_table.horizontalHeader().setStretchLastSection(True)
        tabs.addTab(self.info_table, "Stock Info")

        # Data tab
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(5)
        self.data_table.setHorizontalHeaderLabels(["Date", "Open", "High", "Low", "Close"])
        self.data_table.horizontalHeader().setStretchLastSection(True)
        tabs.addTab(self.data_table, "Historical Data")

        return tabs

    def on_exchange_changed(self, index: int) -> None:
        """Handle exchange selection change.

        Args:
            index: Index of selected exchange in combo box
        """
        selected_exchange = self.exchange_combo.currentData()

        # Update currency label and placeholder
        if selected_exchange:
            # Get exchange info
            currency = TickerSuggestions.get_currency(selected_exchange)
            currency_symbol = TickerSuggestions.get_currency_symbol(selected_exchange)
            country = TickerSuggestions.get_country(selected_exchange)
            region = TickerSuggestions.get_region(selected_exchange)
            timezone = TickerSuggestions.get_timezone(selected_exchange)
            market_hours = TickerSuggestions.get_market_hours(selected_exchange)

            # Update currency label
            self.currency_label.setText(f"💱 {currency_symbol} {currency}")

            # Get sample tickers for placeholder
            samples = TickerSuggestions.get_sample_tickers(selected_exchange, count=3)
            samples_text = ", ".join(samples) if samples else "start typing"

            # Update placeholder with dynamic examples
            self.ticker_input.setPlaceholderText(f"e.g., {samples_text}")

            # Update status with comprehensive exchange details
            exchange_name = self.exchange_combo.currentText()
            self.status_label.setText(
                f"📊 {selected_exchange} | 🌍 {country} ({region}) | 💱 {currency_symbol}{currency} | "
                f"🕐 {timezone} | ⏰ {market_hours}"
            )
        else:
            # All exchanges selected
            self.currency_label.setText("💱 Mixed")
            self.ticker_input.setPlaceholderText("e.g., AAPL, GOOGL, MSFT, 0700 (Hong Kong), SAP (Germany)")
            self.status_label.setText("🌍 Showing stocks from all global exchanges (40+ exchanges)")

        # Clear ticker input and reset suggestions
        self.ticker_input.clear()
        self.on_ticker_text_changed("")

    def on_ticker_text_changed(self, text: str) -> None:
        """Update suggestions when ticker input changes.

        Args:
            text: Current text in ticker input field
        """
        selected_exchange = self.exchange_combo.currentData()
        self.ticker_completer.update_suggestions(text, exchange=selected_exchange)

    def fetch_stock(self) -> None:
        """Fetch stock data from Yahoo Finance."""
        ticker = self.ticker_input.text().strip()
        if not ticker:
            QMessageBox.warning(self, "Input Error", "Please enter a stock ticker")
            return

        self.fetch_button.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.status_label.setText(f"Fetching data for {ticker}...")

        self.fetch_thread = StockDataFetcherThread(ticker, self.period_combo.currentText())
        self.fetch_thread.data_fetched.connect(self.on_data_fetched)
        self.fetch_thread.error.connect(self.on_fetch_error)
        self.fetch_thread.finished.connect(self.on_fetch_finished)
        self.fetch_thread.start()

    def on_data_fetched(self, data: pd.DataFrame, info: dict) -> None:
        """Handle successfully fetched data."""
        self.stock_data = data
        self.stock_info = info

        self.plot_chart()
        self.update_info_table()
        self.update_data_table()

        ticker = self.ticker_input.text().upper()
        self.status_label.setText(f"Successfully loaded data for {ticker}")

    def on_fetch_error(self, error_msg: str) -> None:
        """Handle fetch errors."""
        self.status_label.setText(f"Error: {error_msg}")
        QMessageBox.critical(self, "Error", error_msg)

    def on_fetch_finished(self) -> None:
        """Handle fetch completion."""
        self.fetch_button.setEnabled(True)
        self.progress_bar.setVisible(False)

    def plot_chart(self) -> None:
        """Plot stock price chart."""
        if self.stock_data is None or self.stock_data.empty:
            return

        self.chart_canvas.figure.clear()
        ax = self.chart_canvas.figure.add_subplot(111)

        self.stock_data["Close"].plot(ax=ax, linewidth=2, color="#10B981")

        ticker = self.ticker_input.text().upper()
        ax.set_title(f"{ticker} Stock Price", fontsize=14, fontweight="bold")
        ax.set_xlabel("Date", fontsize=11)
        ax.set_ylabel("Price ($)", fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.figure.autofmt_xdate()

        self.chart_canvas.draw()

    def update_info_table(self) -> None:
        """Update stock information table."""
        self.info_table.setRowCount(len(self.stock_info))

        for row, (key, value) in enumerate(self.stock_info.items()):
            key_display = key.replace("_", " ").title()

            if isinstance(value, float):
                value_display = f"{value:.2f}"
            elif isinstance(value, int) and key == "market_cap":
                value_display = f"${value:,.0f}"
            else:
                value_display = str(value)

            key_item = QTableWidgetItem(key_display)
            value_item = QTableWidgetItem(value_display)
            key_item.setFont(QFont("Arial", 10, QFont.Weight.Bold))

            self.info_table.setItem(row, 0, key_item)
            self.info_table.setItem(row, 1, value_item)

    def update_data_table(self) -> None:
        """Update historical data table."""
        if self.stock_data is None or self.stock_data.empty:
            return

        display_data = self.stock_data.tail(50).iloc[::-1]
        self.data_table.setRowCount(len(display_data))

        for row, (idx, data) in enumerate(display_data.iterrows()):
            date_str = idx.strftime("%Y-%m-%d") if hasattr(idx, "strftime") else str(idx)

            self.data_table.setItem(row, 0, QTableWidgetItem(date_str))
            self.data_table.setItem(row, 1, QTableWidgetItem(f"${data['Open']:.2f}"))
            self.data_table.setItem(row, 2, QTableWidgetItem(f"${data['High']:.2f}"))
            self.data_table.setItem(row, 3, QTableWidgetItem(f"${data['Low']:.2f}"))
            self.data_table.setItem(row, 4, QTableWidgetItem(f"${data['Close']:.2f}"))
