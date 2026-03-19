"""Main application window."""
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

from .widgets import StockViewer, RAGChatWidget


class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("ScrapeMatrix v0.1.0")
        self.setGeometry(100, 100, 1200, 700)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        # Create tabbed interface
        self.tabs = QTabWidget()

        # Home tab
        self._create_home_tab()

        # Stock Viewer tab
        self.stock_viewer = StockViewer()
        self.tabs.addTab(self.stock_viewer, "📊 Stock Viewer")

        # RAG Chat tab
        self.rag_chat = RAGChatWidget()
        self.tabs.addTab(self.rag_chat, "🤖 RAG Chat")

        main_layout.addWidget(self.tabs)
        central_widget.setLayout(main_layout)

    def _create_home_tab(self) -> None:
        """Create and configure the home tab."""
        home_widget = QWidget()
        home_layout = QVBoxLayout()

        home_label = QLabel(
            "🎯 ScrapeMatrix - Industrial Stock Analysis\n\n"
            "📈 Stock Viewer: Real-time stock data and charts\n"
            "🤖 RAG Chat: Document upload & knowledge base Q&A\n"
            "🔍 Future: AI-powered stock analysis agents"
        )
        home_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        home_label.setStyleSheet("font-size: 14px; color: #10B981; line-height: 1.8;")

        home_layout.addWidget(home_label)
        home_layout.addStretch()

        home_widget.setLayout(home_layout)

        self.tabs.addTab(home_widget, "🏠 Home")
