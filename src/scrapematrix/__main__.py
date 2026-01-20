#!/usr/bin/env python3
"""ScrapeMatrix Phase 1: Minimal runnable GUI."""
import sys
from PyQt6.QtWidgets import QApplication
from .gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
