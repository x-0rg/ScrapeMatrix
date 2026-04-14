"""Main application window."""
import logging
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

from .widgets import StockViewer, RAGChatWidget


class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("ScrapeMatrix v0.1.0")
        self.setGeometry(100, 100, 1200, 700)
        self.log_viewer = None

        # Add Menu Bar
        menu_bar = self.menuBar()
        settings_menu = menu_bar.addMenu("⚙️ Settings")
        
        logs_action = QAction("📋 View Live Logs", self)
        logs_action.triggered.connect(self.show_logs)
        settings_menu.addAction(logs_action)

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
        
        # Open the logs window automatically at startup based on user preference
        from PyQt6.QtCore import QSettings
        settings = QSettings("ScrapeMatrix", "App")
        if settings.value("open_logs_at_startup", False, type=bool):
            self.show_logs()

    def show_logs(self):
        """Show the live logs dialog."""
        if not self.log_viewer:
            from .widgets.log_viewer import LogViewerDialog, global_log_handler
            self.log_viewer = LogViewerDialog(self)
            global_log_handler.emitter.log_signal.connect(self.log_viewer.append_log)
            # Add to root logger if not already added
            root_logger = logging.getLogger()
            if global_log_handler not in root_logger.handlers:
                root_logger.addHandler(global_log_handler)
                
        self.log_viewer.show()
        self.log_viewer.raise_()
        self.log_viewer.activateWindow()

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
