#!/usr/bin/env python3
"""ScrapeMatrix Application Entry Point - Standalone executable version.

This script is used as the entry point when PyInstaller creates the executable.
It handles both relative and absolute imports properly.
"""
import sys
import logging
from pathlib import Path

# Add the src directory to the path for absolute imports
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# Now import the application
from PyQt6.QtWidgets import QApplication
from scrapematrix.gui.main_window import MainWindow

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
