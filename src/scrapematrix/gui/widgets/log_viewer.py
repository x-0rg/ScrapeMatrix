import logging
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QCheckBox
from PyQt6.QtCore import QObject, pyqtSignal, QSettings

class LogEmitter(QObject):
    """Emitter for log messages from the logging module to the UI."""
    log_signal = pyqtSignal(str)

class QLogHandler(logging.Handler):
    """Custom logging handler that emits log records to a PyQt signal."""
    def __init__(self):
        super().__init__()
        self.emitter = LogEmitter()
        self.history = []
        self.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    def emit(self, record):
        try:
            msg = self.format(record)
            self.history.append(msg)
            # Keep only last 1000 lines
            if len(self.history) > 1000:
                self.history.pop(0)
            self.emitter.log_signal.emit(msg)
        except Exception:
            self.handleError(record)

# Global log handler instance to attach to the root logger once
global_log_handler = QLogHandler()

class LogViewerDialog(QDialog):
    """Dialog window for live viewing of application logs."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Application Logs")
        self.resize(900, 500)
        self.settings = QSettings("ScrapeMatrix", "App")
        
        layout = QVBoxLayout(self)
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setStyleSheet("font-family: Consolas, monospace; font-size: 12px; background-color: #1e1e1e; color: #d4d4d4;")
        
        # Populate history
        if global_log_handler.history:
            self.text_edit.setText("\n".join(global_log_handler.history))
            
        layout.addWidget(self.text_edit)
        
        btn_layout = QHBoxLayout()
        
        self.startup_cb = QCheckBox("Automatically open logs at startup")
        open_at_startup = self.settings.value("open_logs_at_startup", False, type=bool)
        self.startup_cb.setChecked(open_at_startup)
        self.startup_cb.clicked.connect(self._on_startup_toggled)
        btn_layout.addWidget(self.startup_cb)
        
        btn_layout.addStretch()
        
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.text_edit.clear)
        btn_layout.addWidget(clear_btn)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        btn_layout.addWidget(close_btn)
        
        layout.addLayout(btn_layout)

    def _on_startup_toggled(self):
        self.settings.setValue("open_logs_at_startup", self.startup_cb.isChecked())

    def append_log(self, msg: str):
        self.text_edit.append(msg)
        # Force scroll to the bottom for trailing logs behavior
        scrollbar = self.text_edit.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
