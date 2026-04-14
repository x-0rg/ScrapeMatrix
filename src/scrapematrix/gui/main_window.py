"""Main application window."""
import logging
from PyQt6.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel,
    QToolBar, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from .widgets import StockViewer, RAGChatWidget
from .dialogs import SettingsDialog

# Setup logging
logger = logging.getLogger("scrapematrix")


class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("ScrapeMatrix v0.1.0")
        self.setGeometry(100, 100, 1200, 700)
        logger.info("🚀 MainWindow initializing")

        # Create toolbar
        self._create_toolbar()

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
        logger.info("✅ Stock Viewer tab loaded")

        # RAG Chat tab
        self.rag_chat = RAGChatWidget()
        self.tabs.addTab(self.rag_chat, "🤖 RAG Chat")
        logger.info("✅ RAG Chat tab loaded")

        main_layout.addWidget(self.tabs)
        central_widget.setLayout(main_layout)

        logger.info("🎯 MainWindow initialization complete")

    def _create_toolbar(self) -> None:
        """Create the application toolbar with settings button."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Add stretch to push buttons to the right
        spacer = QWidget()
        spacer.setMinimumWidth(400)
        toolbar.addWidget(spacer)

        # Settings button
        settings_btn = QPushButton("⚙️ Settings & Logs")
        settings_btn.setToolTip("Open settings and view application logs")
        settings_btn.clicked.connect(self._open_settings)
        toolbar.addWidget(settings_btn)

        # About button
        about_btn = QPushButton("ℹ️ About")
        about_btn.setToolTip("About ScrapeMatrix")
        about_btn.clicked.connect(self._show_about)
        toolbar.addWidget(about_btn)

        logger.debug("📊 Toolbar created")

    def _open_settings(self) -> None:
        """Open the settings dialog."""
        logger.info("🔧 Opening settings dialog")
        settings_dialog = SettingsDialog(self)
        settings_dialog.exec()
        logger.info("🔧 Settings dialog closed")

    def _show_about(self) -> None:
        """Show about dialog."""
        from PyQt6.QtWidgets import QMessageBox

        logger.info("ℹ️ Showing about dialog")
        QMessageBox.information(
            self,
            "About ScrapeMatrix",
            "ScrapeMatrix v0.1.0\n\n"
            "Industrial Stock Analysis & RAG Chat\n\n"
            "Features:\n"
            "📈 Real-time stock data (40+ exchanges)\n"
            "🤖 Document Q&A with knowledge base\n"
            "📊 Interactive charts and analysis\n\n"
            "© 2024 ScrapeMatrix Project",
        )

    def _create_home_tab(self) -> None:
        """Create and configure the home tab."""
        home_widget = QWidget()
        home_layout = QVBoxLayout()

        home_label = QLabel(
            "🎯 ScrapeMatrix - Industrial Stock Analysis\n\n"
            "📈 Stock Viewer: Real-time stock data and charts\n"
            "🤖 RAG Chat: Document upload & knowledge base Q&A\n"
            "🔍 Future: AI-powered stock analysis agents\n\n"
            "💡 Tip: Click ⚙️ Settings & Logs to view application logs"
        )
        home_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        home_label.setStyleSheet("font-size: 14px; color: #10B981; line-height: 1.8;")

        home_layout.addWidget(home_label)
        home_layout.addStretch()

        home_widget.setLayout(home_layout)

        self.tabs.addTab(home_widget, "🏠 Home")
