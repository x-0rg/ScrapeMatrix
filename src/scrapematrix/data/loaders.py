"""Stock data loading from Yahoo Finance."""
import logging
from typing import Optional

import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


class StockDataLoader:
    """Load and fetch stock data from Yahoo Finance."""

    @staticmethod
    def fetch_stock_data(
        ticker: str,
        period: str = "1y",
        interval: str = "1d"
    ) -> Optional[pd.DataFrame]:
        """
        Fetch historical stock data from Yahoo Finance.

        Args:
            ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            period: Data period - '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
            interval: Data interval - '1m', '5m', '15m', '30m', '60m', '1d', '1wk', '1mo', '3mo'

        Returns:
            DataFrame with OHLCV (Open, High, Low, Close, Volume) data, or None if fetch fails.
        """
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period, interval=interval)

            if hist.empty:
                logger.warning(f"No data returned for {ticker}")
                return None

            return hist
        except Exception as e:
            logger.error(f"Error fetching stock data for {ticker}: {e}")
            return None

    @staticmethod
    def get_stock_info(ticker: str) -> dict:
        """
        Fetch stock metadata and financial information.

        Args:
            ticker: Stock ticker symbol

        Returns:
            Dictionary with company info:
                - name: Company name
                - current_price: Current stock price
                - previous_close: Previous trading day close
                - open: Today's opening price
                - high_52w: 52-week high
                - low_52w: 52-week low
                - market_cap: Market capitalization
                - pe_ratio: Price-to-earnings ratio
                - dividend_yield: Dividend yield percentage
                - sector: Industry sector
        """
        try:
            stock = yf.Ticker(ticker)
            return {
                "name": stock.info.get("longName", "N/A"),
                "current_price": stock.info.get("currentPrice", "N/A"),
                "previous_close": stock.info.get("previousClose", "N/A"),
                "open": stock.info.get("open", "N/A"),
                "high_52w": stock.info.get("fiftyTwoWeekHigh", "N/A"),
                "low_52w": stock.info.get("fiftyTwoWeekLow", "N/A"),
                "market_cap": stock.info.get("marketCap", "N/A"),
                "pe_ratio": stock.info.get("trailingPE", "N/A"),
                "dividend_yield": stock.info.get("dividendYield", "N/A"),
                "sector": stock.info.get("sector", "N/A"),
            }
        except Exception as e:
            logger.error(f"Error fetching stock info for {ticker}: {e}")
            return {}
