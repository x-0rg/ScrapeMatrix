"""Stock ticker symbols database and search functionality."""

# Popular stock tickers organized by sector/category
POPULAR_TICKERS = {
    "Technology": [
        "AAPL", "GOOGL", "GOOG", "MSFT", "AMZN", "TSLA",
        "META", "NVDA", "INTEL", "AMD", "QCOM", "CRM", "ADBE"
    ],
    "Finance": [
        "JPM", "BAC", "WFC", "GS", "MS", "BLK", "SCHW", "COIN"
    ],
    "Healthcare": [
        "JNJ", "PFE", "MRNA", "ABBV", "TMO", "LLY", "AZN", "BNTX"
    ],
    "Consumer": [
        "WMT", "TGT", "COST", "MCD", "NKE", "HD", "AMZN", "EBAY"
    ],
    "Energy": [
        "XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "VLO"
    ],
    "Industrial": [
        "BA", "CAT", "MMM", "GE", "HON", "RTX", "LMT", "NOC"
    ],
    "Utilities": [
        "NEE", "DUK", "SO", "AEP", "EXC", "PEG", "SRE", "AWK"
    ],
    "Real Estate": [
        "XLRE", "PLD", "AMT", "CCI", "EQIX", "WELL", "SPG", "PSA"
    ],
    "Communications": [
        "VZ", "T", "CMCSA", "CHTR", "TMUS", "DISH"
    ]
}

# Flatten and sort all tickers (remove duplicates)
ALL_TICKERS = sorted(list(set(
    ticker for tickers in POPULAR_TICKERS.values() for ticker in tickers
)))


class TickerSuggestions:
    """Provide stock ticker suggestions and search capabilities."""

    @staticmethod
    def get_all_tickers() -> list[str]:
        """Get sorted list of all popular tickers."""
        return ALL_TICKERS

    @staticmethod
    def get_by_category(category: str) -> list[str]:
        """Get tickers by category/sector."""
        return POPULAR_TICKERS.get(category, [])

    @staticmethod
    def get_categories() -> list[str]:
        """Get all available categories."""
        return list(POPULAR_TICKERS.keys())

    @staticmethod
    def search(query: str) -> list[str]:
        """
        Search for tickers matching the query prefix.

        Args:
            query: Search string (case-insensitive)

        Returns:
            List of tickers starting with the query string
        """
        query_upper = query.upper()
        return [ticker for ticker in ALL_TICKERS if ticker.startswith(query_upper)]
