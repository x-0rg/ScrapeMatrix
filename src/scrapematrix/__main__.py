#!/usr/bin/env python3
"""ScrapeMatrix Application Entry Point.

Run as: python -m scrapematrix
"""
import logging
import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

# Handle both relative imports (for python -m) and absolute imports
try:
    from .gui.main_window import MainWindow
except ImportError:
    # Fallback for PyInstaller or direct execution
    from scrapematrix.gui.main_window import MainWindow

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    # Attach our GUI log handler so we capture logs before the window opens
    from scrapematrix.gui.widgets.log_viewer import global_log_handler
    logging.getLogger().addHandler(global_log_handler)


def main() -> None:
    """Launch the ScrapeMatrix application."""
    try:
        setup_logging()
        logger.info("Starting ScrapeMatrix application...")

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()

        logger.info("Application window displayed")
        sys.exit(app.exec())
    except Exception as e:
        logger.exception("Fatal error during application startup")
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

