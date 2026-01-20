from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ScrapeMatrix v0.1.0 - Phase 0.1")
        self.setGeometry(100, 100, 800, 600)  # x,y,width,height
        
        # Central widget + label
        central_widget = QLabel("ScrapeMatrix Phase 1 Complete!\n\nMinimal PyQt6 Window ✅")
        central_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central_widget.setStyleSheet("font-size: 24px; color: #10B981;")
        self.setCentralWidget(central_widget)
