"""Settings dialog with live application logs."""
import logging
import sys
from datetime import datetime
from pathlib import Path

from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QComboBox,
    QSpinBox,
    QCheckBox,
    QGroupBox,
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt6.QtGui import QFont, QColor


class LogSignals(QObject):
    """Signals for log events."""

    new_log = pyqtSignal(str)


class QTextEditHandler(logging.Handler):
    """Custom logging handler that emits signals for log updates."""

    def __init__(self, signals: LogSignals):
        """Initialize the handler.

        Args:
            signals: LogSignals object to emit updates
        """
        super().__init__()
        self.signals = signals

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log record.

        Args:
            record: The log record to emit
        """
        try:
            msg = self.format(record)
            self.signals.new_log.emit(msg)
        except Exception:
            self.handleError(record)


class SettingsDialog(QDialog):
    """Settings dialog with live logs viewer and application settings."""

    def __init__(self, parent=None):
        """Initialize the settings dialog.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self.setWindowTitle("⚙️ Settings & Application Logs")
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowIcon(None)

        # Setup logging signals
        self.log_signals = LogSignals()
        self.log_signals.new_log.connect(self._on_new_log)

        # Setup custom log handler
        self._setup_log_handler()

        # Create UI
        self._create_ui()

        # Log initial message
        logger = logging.getLogger("scrapematrix")
        logger.info("🎯 Settings & Logs dialog opened")

    def _setup_log_handler(self) -> None:
        """Setup custom logging handler for live logs."""
        logger = logging.getLogger("scrapematrix")

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%H:%M:%S",
        )

        # Create and add handler
        self.log_handler = QTextEditHandler(self.log_signals)
        self.log_handler.setFormatter(formatter)
        logger.addHandler(self.log_handler)

    def _create_ui(self) -> None:
        """Create the UI components."""
        layout = QVBoxLayout()

        # Create tab widget
        self.tabs = QTabWidget()

        # Settings tab
        self._create_settings_tab()

        # Logs tab
        self._create_logs_tab()

        layout.addWidget(self.tabs)

        # Bottom buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        clear_logs_btn = QPushButton("🗑️ Clear Logs")
        clear_logs_btn.clicked.connect(self._clear_logs)
        button_layout.addWidget(clear_logs_btn)

        export_logs_btn = QPushButton("💾 Export Logs")
        export_logs_btn.clicked.connect(self._export_logs)
        button_layout.addWidget(export_logs_btn)

        close_btn = QPushButton("✕ Close")
        close_btn.clicked.connect(self.accept)
        button_layout.addWidget(close_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def _create_settings_tab(self) -> None:
        """Create the settings tab."""
        settings_widget = QWidget()
        settings_layout = QVBoxLayout()

        # Application Settings Group
        app_group = QGroupBox("📱 Application Settings")
        app_layout = QVBoxLayout()

        # Theme setting
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        theme_combo = QComboBox()
        theme_combo.addItems(["Light", "Dark", "Auto"])
        theme_layout.addWidget(theme_combo)
        theme_layout.addStretch()
        app_layout.addLayout(theme_layout)

        # Font size
        font_layout = QHBoxLayout()
        font_layout.addWidget(QLabel("Font Size:"))
        font_spin = QSpinBox()
        font_spin.setValue(10)
        font_spin.setRange(8, 16)
        font_layout.addWidget(font_spin)
        font_layout.addStretch()
        app_layout.addLayout(font_layout)

        app_group.setLayout(app_layout)
        settings_layout.addWidget(app_group)

        # Data & Logging Group
        data_group = QGroupBox("📊 Data & Logging")
        data_layout = QVBoxLayout()

        # Auto-update
        auto_update = QCheckBox("Enable automatic updates")
        auto_update.setChecked(True)
        data_layout.addWidget(auto_update)

        # Log level
        log_layout = QHBoxLayout()
        log_layout.addWidget(QLabel("Log Level:"))
        log_combo = QComboBox()
        log_combo.addItems(["DEBUG", "INFO", "WARNING", "ERROR"])
        log_combo.setCurrentText("INFO")
        log_combo.currentTextChanged.connect(self._set_log_level)
        log_layout.addWidget(log_combo)
        log_layout.addStretch()
        data_layout.addLayout(log_layout)

        # Enable file logging
        file_logging = QCheckBox("Enable file logging (~/scrapematrix/logs/)")
        file_logging.setChecked(False)
        file_logging.stateChanged.connect(self._toggle_file_logging)
        data_layout.addWidget(file_logging)

        data_group.setLayout(data_layout)
        settings_layout.addWidget(data_group)

        # Stock Viewer Settings Group
        stock_group = QGroupBox("📈 Stock Viewer Settings")
        stock_layout = QVBoxLayout()

        # Auto-refresh interval
        refresh_layout = QHBoxLayout()
        refresh_layout.addWidget(QLabel("Auto-refresh interval (seconds):"))
        refresh_spin = QSpinBox()
        refresh_spin.setValue(30)
        refresh_spin.setRange(5, 300)
        refresh_layout.addWidget(refresh_spin)
        refresh_layout.addStretch()
        stock_layout.addLayout(refresh_layout)

        stock_group.setLayout(stock_layout)
        settings_layout.addWidget(stock_group)

        settings_layout.addStretch()
        settings_widget.setLayout(settings_layout)
        self.tabs.addTab(settings_widget, "⚙️ Settings")

    def _create_logs_tab(self) -> None:
        """Create the logs tab."""
        logs_widget = QWidget()
        logs_layout = QVBoxLayout()

        # Logs info label
        info_label = QLabel(
            "📋 Real-time Application Logs\n"
            "Showing live log messages from all components"
        )
        info_label.setStyleSheet("color: #6B7280; font-size: 11px;")
        logs_layout.addWidget(info_label)

        # Log display
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setFont(QFont("Courier", 9))
        self.log_display.setStyleSheet(
            """
            QTextEdit {
                background-color: #1F2937;
                color: #E5E7EB;
                border: 1px solid #374151;
                border-radius: 4px;
                padding: 8px;
            }
        """
        )

        logs_layout.addWidget(self.log_display)

        # Log filter
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter by level:"))
        self.log_filter = QComboBox()
        self.log_filter.addItems(["All", "DEBUG", "INFO", "WARNING", "ERROR"])
        self.log_filter.currentTextChanged.connect(self._update_log_display)
        filter_layout.addWidget(self.log_filter)
        filter_layout.addStretch()
        logs_layout.addLayout(filter_layout)

        # Auto-scroll checkbox
        auto_scroll = QCheckBox("Auto-scroll to bottom")
        auto_scroll.setChecked(True)
        self.auto_scroll = auto_scroll
        logs_layout.addWidget(auto_scroll)

        logs_widget.setLayout(logs_layout)
        self.tabs.addTab(logs_widget, "📋 Logs")

        # Store logs for filtering
        self.all_logs = []

    def _on_new_log(self, message: str) -> None:
        """Handle new log message.

        Args:
            message: The log message to display
        """
        # Store the log
        self.all_logs.append(message)

        # Keep last 1000 logs to avoid memory issues
        if len(self.all_logs) > 1000:
            self.all_logs.pop(0)

        # Update display
        self._update_log_display()

        # Auto-scroll if enabled
        if self.auto_scroll.isChecked():
            self.log_display.verticalScrollBar().setValue(
                self.log_display.verticalScrollBar().maximum()
            )

    def _update_log_display(self) -> None:
        """Update the log display based on current filter."""
        filter_level = self.log_filter.currentText()

        filtered_logs = self.all_logs

        if filter_level != "All":
            filtered_logs = [
                log for log in self.all_logs if filter_level in log
            ]

        # Color code by level
        colored_logs = []
        for log in filtered_logs:
            if "ERROR" in log:
                colored_logs.append(f"<span style='color: #EF4444;'>{log}</span>")
            elif "WARNING" in log:
                colored_logs.append(f"<span style='color: #F59E0B;'>{log}</span>")
            elif "DEBUG" in log:
                colored_logs.append(f"<span style='color: #9CA3AF;'>{log}</span>")
            else:
                colored_logs.append(f"<span style='color: #10B981;'>{log}</span>")

        self.log_display.setText("<br>".join(colored_logs))

    def _clear_logs(self) -> None:
        """Clear all logs."""
        self.all_logs.clear()
        self.log_display.clear()
        logger = logging.getLogger("scrapematrix")
        logger.info("📋 Logs cleared by user")

    def _export_logs(self) -> None:
        """Export logs to file."""
        log_dir = Path.home() / ".scrapematrix" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"scrapematrix_{timestamp}.log"

        with open(log_file, "w") as f:
            f.write("\n".join(self.all_logs))

        logger = logging.getLogger("scrapematrix")
        logger.info(f"💾 Logs exported to {log_file}")

    def _set_log_level(self, level: str) -> None:
        """Set the logging level.

        Args:
            level: The logging level (DEBUG, INFO, WARNING, ERROR)
        """
        logger = logging.getLogger("scrapematrix")
        logger.setLevel(getattr(logging, level))
        logger.info(f"📊 Log level changed to {level}")

    def _toggle_file_logging(self, state: int) -> None:
        """Toggle file logging.

        Args:
            state: Checkbox state
        """
        logger = logging.getLogger("scrapematrix")

        if state:
            # Enable file logging
            log_dir = Path.home() / ".scrapematrix" / "logs"
            log_dir.mkdir(parents=True, exist_ok=True)

            log_file = log_dir / "scrapematrix.log"
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
                )
            )
            logger.addHandler(file_handler)
            logger.info(f"📁 File logging enabled: {log_file}")
        else:
            # Disable file logging
            logger.info("📁 File logging disabled")
