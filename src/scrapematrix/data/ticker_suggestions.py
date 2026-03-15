"""Stock ticker symbols database and search functionality."""

# Country information: currency, exchange, etc.
COUNTRY_INFO = {
    "🇺🇸 United States": {
        "currency": "USD",
        "currency_symbol": "$",
        "exchange": "NYSE/NASDAQ",
        "timezone": "EST"
    },
    "🇨🇦 Canada": {
        "currency": "CAD",
        "currency_symbol": "C$",
        "exchange": "TSX",
        "timezone": "EST"
    },
    "🇬🇧 United Kingdom": {
        "currency": "GBP",
        "currency_symbol": "£",
        "exchange": "LSE",
        "timezone": "GMT"
    },
    "🇯🇵 Japan": {
        "currency": "JPY",
        "currency_symbol": "¥",
        "exchange": "TSE",
        "timezone": "JST"
    },
    "🇩🇪 Germany": {
        "currency": "EUR",
        "currency_symbol": "€",
        "exchange": "xetra",
        "timezone": "CET"
    },
    "🇫🇷 France": {
        "currency": "EUR",
        "currency_symbol": "€",
        "exchange": "Euronext Paris",
        "timezone": "CET"
    },
    "🇭🇰 Hong Kong": {
        "currency": "HKD",
        "currency_symbol": "HK$",
        "exchange": "HKEX",
        "timezone": "HKT"
    },
    "🇮🇳 India": {
        "currency": "INR",
        "currency_symbol": "₹",
        "exchange": "NSE/BSE",
        "timezone": "IST"
    },
    "🇦🇺 Australia": {
        "currency": "AUD",
        "currency_symbol": "A$",
        "exchange": "ASX",
        "timezone": "AEDT"
    },
    "🇸🇬 Singapore": {
        "currency": "SGD",
        "currency_symbol": "S$",
        "exchange": "SGX",
        "timezone": "SGT"
    }
}

# Popular stock tickers organized by country
STOCKS_BY_COUNTRY = {
    "🇺🇸 United States": {
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
    },
    "🇨🇦 Canada": {
        "Banking": ["RY", "TD", "BNS", "CM", "BMO"],
        "Energy": ["ENB", "TRP", "CNQ", "SU", "CVE"],
        "Mining": ["BTO", "BAM", "GIB", "WCP", "AR"],
        "Technology": ["SHOP", "LSPD"],
        "Consumer": ["CNR", "MRU"]
    },
    "🇬🇧 United Kingdom": {
        "Banking": ["BARCLAYS", "HSBA", "STAN", "NWG"],
        "Energy": ["SHELL", "BP", "SGE"],
        "Consumer": ["ULVR", "DGE", "SBRY"],
        "Mining": ["GLEN", "ANTM", "RIO"],
        "Pharma": ["GSK", "HALEON", "AZN"]
    },
    "🇯🇵 Japan": {
        "Electronics": ["7203", "6758", "9984"],  # Toyota, Sony, SoftBank
        "Banking": ["8306", "8411", "8001"],      # Mizuho, Sumitomo, Nomura
        "Automotive": ["7203", "7261"],           # Toyota, Mazda
        "Retail": ["8015", "9983"],               # Mitsubishi UFJ, SoftBank
        "Industrial": ["6367"]                    # Daiwa House
    },
    "🇩🇪 Germany": {
        "Automotive": ["SAP", "SIE", "DAI", "BMW"],
        "Industrial": ["BASF", "SIE", "HEN3"],
        "Banking": ["DBK", "ARL"],
        "Engineering": ["MUV2"]
    },
    "🇫🇷 France": {
        "Luxury": ["LVMH", "OREP", "DXPE"],
        "Banking": ["BNPP", "GLE", "KN"],
        "Energy": ["EDF", "ENGI"],
        "Utilities": ["ENGI", "VIE"]
    },
    "🇭🇰 Hong Kong": {
        "Banking": ["0001", "0002", "0003", "0005"],  # HSBC, CLP, HKExch, AEON
        "Tech": ["0700", "9988"],                      # Tencent, Alibaba
        "Property": ["0016", "0083"],
        "Consumer": ["0153", "1928"]
    },
    "🇮🇳 India": {
        "IT": ["TCS", "INFY", "WIPRO"],
        "Banking": ["HDBK", "ICICIBANK", "AXISBANK"],
        "Automotive": ["MARUTI", "TATA"],
        "Pharma": ["SUNPHARMA", "CIPLA"],
        "Consumer": ["ITC", "NESTLEIND"]
    },
    "🇦🇺 Australia": {
        "Banking": ["ANZ", "WBC", "NAB", "CBA"],
        "Mining": ["BHP", "RIO", "FMG"],
        "Energy": ["WES", "APA", "ORI"],
        "Retail": ["WES", "DJS"],
        "Telecom": ["TEL"]
    },
    "🇸🇬 Singapore": {
        "Banking": ["OCBC", "DBS", "UOB"],
        "Shipping": ["SEATRADE"],
        "Real Estate": ["CAPITALAND"],
        "Energy": ["OXLEY"]
    }
}

# Flatten all sectors into country-based lists
STOCKS_BY_COUNTRY_FLAT = {
    country: sorted(list(set(
        ticker for sector_tickers in sectors.values() 
        for ticker in sector_tickers
    )))
    for country, sectors in STOCKS_BY_COUNTRY.items()
}

# Popular stock tickers organized by sector/category (for backward compatibility)
POPULAR_TICKERS = STOCKS_BY_COUNTRY["🇺🇸 United States"]

# Flatten and sort all tickers (remove duplicates)
ALL_TICKERS = sorted(list(set(
    ticker for country_tickers in STOCKS_BY_COUNTRY_FLAT.values() 
    for ticker in country_tickers
)))


class TickerSuggestions:
    """Provide stock ticker suggestions and search capabilities."""

    @staticmethod
    def get_all_tickers() -> list[str]:
        """Get sorted list of all popular tickers."""
        return ALL_TICKERS

    @staticmethod
    def get_countries() -> list[str]:
        """Get list of all available countries."""
        return sorted(list(STOCKS_BY_COUNTRY.keys()))

    @staticmethod
    def get_tickers_by_country(country: str) -> list[str]:
        """
        Get all tickers for a specific country.

        Args:
            country: Country name (e.g., "🇺🇸 United States")

        Returns:
            List of tickers from that country
        """
        return STOCKS_BY_COUNTRY_FLAT.get(country, [])

    @staticmethod
    def get_sectors_by_country(country: str) -> list[str]:
        """
        Get all sectors/categories for a specific country.

        Args:
            country: Country name

        Returns:
            List of sectors available in that country
        """
        return list(STOCKS_BY_COUNTRY.get(country, {}).keys())

    @staticmethod
    def get_tickers_by_country_sector(country: str, sector: str) -> list[str]:
        """
        Get tickers for a specific country and sector.

        Args:
            country: Country name
            sector: Sector/category name

        Returns:
            List of tickers from that country and sector
        """
        if country not in STOCKS_BY_COUNTRY:
            return []
        return STOCKS_BY_COUNTRY[country].get(sector, [])

    @staticmethod
    def search(query: str, country: str = None) -> list[str]:
        """
        Search for tickers matching the query prefix.

        Args:
            query: Search string (case-insensitive)
            country: Optional country filter (e.g., "🇺🇸 United States")

        Returns:
            List of tickers starting with the query string
        """
        query_upper = query.upper()

        # If country specified, search only in that country
        if country and country in STOCKS_BY_COUNTRY_FLAT:
            tickers = STOCKS_BY_COUNTRY_FLAT[country]
            return [ticker for ticker in tickers if ticker.startswith(query_upper)]

        # Otherwise search all tickers
        return [ticker for ticker in ALL_TICKERS if ticker.startswith(query_upper)]

    @staticmethod
    def get_by_category(category: str) -> list[str]:
        """Get tickers by category/sector (for backward compatibility)."""
        return POPULAR_TICKERS.get(category, [])

    @staticmethod
    def get_country_info(country: str) -> dict:
        """
        Get currency and exchange information for a country.

        Args:
            country: Country name (e.g., "🇺🇸 United States")

        Returns:
            Dictionary with currency, currency_symbol, exchange, timezone
        """
        return COUNTRY_INFO.get(country, {
            "currency": "N/A",
            "currency_symbol": "$",
            "exchange": "N/A",
            "timezone": "N/A"
        })

    @staticmethod
    def get_currency(country: str) -> str:
        """
        Get currency code for a country.

        Args:
            country: Country name

        Returns:
            Currency code (e.g., "USD", "EUR", "JPY")
        """
        info = COUNTRY_INFO.get(country, {})
        return info.get("currency", "N/A")

    @staticmethod
    def get_currency_symbol(country: str) -> str:
        """
        Get currency symbol for a country.

        Args:
            country: Country name

        Returns:
            Currency symbol (e.g., "$", "€", "¥")
        """
        info = COUNTRY_INFO.get(country, {})
        return info.get("currency_symbol", "$")

    @staticmethod
    def get_exchange(country: str) -> str:
        """
        Get stock exchange name for a country.

        Args:
            country: Country name

        Returns:
            Exchange name (e.g., "NYSE/NASDAQ", "LSE", "TSE")
        """
        info = COUNTRY_INFO.get(country, {})
        return info.get("exchange", "N/A")

    @staticmethod
    def get_sample_tickers(country: str, count: int = 3) -> list[str]:
        """
        Get sample ticker symbols for a country.

        Args:
            country: Country name
            count: Number of samples to return

        Returns:
            List of sample tickers from that country
        """
        tickers = STOCKS_BY_COUNTRY_FLAT.get(country, [])
        return tickers[:count] if tickers else []

    @staticmethod
    def get_categories() -> list[str]:
        """Get all available categories (for backward compatibility)."""
        return list(POPULAR_TICKERS.keys())
