#!/usr/bin/env python3
"""ScrapeMatrix Application Entry Point.

Run as: python -m scrapematrix
"""
import logging
import sys

from PyQt6.QtWidgets import QApplication

from .gui.main_window import MainWindow

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


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
