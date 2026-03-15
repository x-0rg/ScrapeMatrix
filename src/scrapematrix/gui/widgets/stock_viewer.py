"""Stock data viewer widget."""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
    QPushButton, QLabel, QComboBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QMessageBox, QProgressBar
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from typing import Optional

from ..data.loaders import StockDataLoader


class StockDataFetcherThread(QThread):
    """Background thread to fetch stock data without blocking UI."""
    
    finished = pyqtSignal()
    error = pyqtSignal(str)
    data_fetched = pyqtSignal(pd.DataFrame, dict)
    
    def __init__(self, ticker: str, period: str, interval: str):
        super().__init__()
        self.ticker = ticker.upper()
        self.period = period
        self.interval = interval
    
    def run(self):
        try:
            # Fetch historical data
            data = StockDataLoader.fetch_stock_data(
                self.ticker, 
                self.period, 
                self.interval
            )
            
            if data is None:
                self.error.emit(f"Could not fetch data for {self.ticker}")
                return
            
            # Fetch stock info
            info = StockDataLoader.get_stock_info(self.ticker)
            
            self.data_fetched.emit(data, info)
        except Exception as e:
            self.error.emit(f"Error: {str(e)}")
        finally:
            self.finished.emit()


class StockViewer(QWidget):
    """Widget for viewing stock data and charts."""
    
    def __init__(self):
        super().__init__()
        self.stock_data = None
        self.stock_info = {}
        self.fetch_thread = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI."""
        layout = QVBoxLayout()
        
        # Input section
        input_layout = QHBoxLayout()
        
        # Ticker input
        ticker_label = QLabel("Stock Ticker:")
        self.ticker_input = QLineEdit()
        self.ticker_input.setPlaceholderText("e.g., AAPL, GOOGL, MSFT")
        self.ticker_input.returnPressed.connect(self.fetch_stock)
        
        # Period selector
        period_label = QLabel("Period:")
        self.period_combo = QComboBox()
        self.period_combo.addItems(["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
        self.period_combo.setCurrentText("1y")
        
        # Fetch button
        self.fetch_button = QPushButton("Fetch Data")
        self.fetch_button.clicked.connect(self.fetch_stock)
        self.fetch_button.setStyleSheet(
            "QPushButton { background-color: #10B981; color: white; padding: 8px; border-radius: 4px; font-weight: bold; }"
        )
        
        input_layout.addWidget(ticker_label)
        input_layout.addWidget(self.ticker_input)
        input_layout.addWidget(period_label)
        input_layout.addWidget(self.period_combo)
        input_layout.addWidget(self.fetch_button)
        input_layout.addStretch()
        
        layout.addLayout(input_layout)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Status label
        self.status_label = QLabel("Enter a stock ticker and click 'Fetch Data'")
        self.status_label.setStyleSheet("color: #666; font-size: 12px;")
        layout.addWidget(self.status_label)
        
        # Tabs for Chart and Data
        self.tabs = QTabWidget()
        
        # Chart tab
        self.chart_canvas = FigureCanvas(Figure(figsize=(10, 6)))
        self.tabs.addTab(self.chart_canvas, "📈 Chart")
        
        # Data info tab
        self.info_widget = QWidget()
        info_layout = QVBoxLayout()
        self.info_table = QTableWidget()
        self.info_table.setColumnCount(2)
        self.info_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.info_table.horizontalHeader().setStretchLastSection(True)
        info_layout.addWidget(self.info_table)
        self.info_widget.setLayout(info_layout)
        self.tabs.addTab(self.info_widget, "📊 Stock Info")
        
        # Data tab
        self.data_widget = QWidget()
        data_layout = QVBoxLayout()
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(5)
        self.data_table.setHorizontalHeaderLabels(["Date", "Open", "High", "Low", "Close"])
        self.data_table.horizontalHeader().setStretchLastSection(True)
        data_layout.addWidget(self.data_table)
        self.data_widget.setLayout(data_layout)
        self.tabs.addTab(self.data_widget, "📋 Historical Data")
        
        layout.addWidget(self.tabs)
        
        self.setLayout(layout)
    
    def fetch_stock(self):
        """Fetch stock data in background thread."""
        ticker = self.ticker_input.text().strip()
        
        if not ticker:
            QMessageBox.warning(self, "Input Error", "Please enter a stock ticker")
            return
        
        self.fetch_button.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.status_label.setText(f"Fetching data for {ticker}...")
        
        period = self.period_combo.currentText()
        
        # Create and start background thread
        self.fetch_thread = StockDataFetcherThread(ticker, period, "1d")
        self.fetch_thread.data_fetched.connect(self.on_data_fetched)
        self.fetch_thread.error.connect(self.on_fetch_error)
        self.fetch_thread.finished.connect(self.on_fetch_finished)
        self.fetch_thread.start()
    
    def on_data_fetched(self, data: pd.DataFrame, info: dict):
        """Handle fetched stock data."""
        self.stock_data = data
        self.stock_info = info
        
        # Update chart
        self.plot_chart()
        
        # Update stock info table
        self.update_info_table()
        
        # Update historical data table
        self.update_data_table()
        
        ticker = self.ticker_input.text().upper()
        self.status_label.setText(f"✅ Successfully loaded data for {ticker}")
    
    def on_fetch_error(self, error_msg: str):
        """Handle fetch error."""
        self.status_label.setText(f"❌ {error_msg}")
        QMessageBox.critical(self, "Error", error_msg)
    
    def on_fetch_finished(self):
        """Handle fetch completion."""
        self.fetch_button.setEnabled(True)
        self.progress_bar.setVisible(False)
    
    def plot_chart(self):
        """Plot the stock price chart."""
        if self.stock_data is None or self.stock_data.empty:
            return
        
        # Clear previous plot
        self.chart_canvas.figure.clear()
        ax = self.chart_canvas.figure.add_subplot(111)
        
        # Plot closing price
        self.stock_data['Close'].plot(ax=ax, linewidth=2, color='#10B981')
        
        # Styling
        ax.set_title(
            f"{self.ticker_input.text().upper()} Stock Price",
            fontsize=14,
            fontweight='bold'
        )
        ax.set_xlabel("Date", fontsize=11)
        ax.set_ylabel("Price ($)", fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.figure.autofmt_xdate()
        
        self.chart_canvas.draw()
    
    def update_info_table(self):
        """Update stock information table."""
        self.info_table.setRowCount(len(self.stock_info))
        
        row = 0
        for key, value in self.stock_info.items():
            # Format key (snake_case to Title Case)
            key_display = key.replace("_", " ").title()
            
            # Format value
            if isinstance(value, float):
                value_display = f"{value:.2f}"
            elif isinstance(value, int) and key == "market_cap":
                value_display = f"${value:,.0f}"
            else:
                value_display = str(value)
            
            # Add to table
            key_item = QTableWidgetItem(key_display)
            value_item = QTableWidgetItem(value_display)
            
            key_item.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            
            self.info_table.setItem(row, 0, key_item)
            self.info_table.setItem(row, 1, value_item)
            row += 1
    
    def update_data_table(self):
        """Update historical data table."""
        if self.stock_data is None or self.stock_data.empty:
            return
        
        # Show last 50 rows
        display_data = self.stock_data.tail(50).iloc[::-1]  # Most recent first
        
        self.data_table.setRowCount(len(display_data))
        
        for row, (idx, data) in enumerate(display_data.iterrows()):
            date_str = idx.strftime("%Y-%m-%d") if hasattr(idx, 'strftime') else str(idx)
            
            self.data_table.setItem(row, 0, QTableWidgetItem(date_str))
            self.data_table.setItem(row, 1, QTableWidgetItem(f"${data['Open']:.2f}"))
            self.data_table.setItem(row, 2, QTableWidgetItem(f"${data['High']:.2f}"))
            self.data_table.setItem(row, 3, QTableWidgetItem(f"${data['Low']:.2f}"))
            self.data_table.setItem(row, 4, QTableWidgetItem(f"${data['Close']:.2f}"))
