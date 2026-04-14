from abc import ABC, abstractmethod
import logging

class BaseScraper(ABC):
    """Abstract base class for all scrapers."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        # Ensure logger has a handler
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    @abstractmethod
    def scrape(self, ticker: str, **kwargs):
        """
        Main method to execute scraping logic for a given ticker.
        Must be implemented by subclasses.
        """
        pass
