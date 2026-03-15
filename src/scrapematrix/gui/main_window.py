from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from .widgets import StockViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScrapeMatrix v0.1.0")
        self.setGeometry(100, 100, 1200, 700)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        # Create tabs
        self.tabs = QTabWidget()

        # Home tab
        home_widget = QWidget()
        home_layout = QVBoxLayout()
        home_label = QLabel(
            "🎯 ScrapeMatrix - Industrial Stock Analysis\n\n"
            "📈 Stock Viewer: Real-time stock data and charts\n"
            "🤖 Agents: AI-powered stock analysis (coming soon)\n"
            "🔍 RAG: Retrieval-augmented generation (coming soon)"
        )
        home_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        home_label.setStyleSheet("font-size: 14px; color: #10B981; line-height: 1.8;")
        home_layout.addWidget(home_label)
        home_layout.addStretch()
        home_widget.setLayout(home_layout)
        self.tabs.addTab(home_widget, "🏠 Home")

        # Stock Viewer tab
        self.stock_viewer = StockViewer()
        self.tabs.addTab(self.stock_viewer, "📊 Stock Viewer")

        main_layout.addWidget(self.tabs)
        central_widget.setLayout(main_layout)
