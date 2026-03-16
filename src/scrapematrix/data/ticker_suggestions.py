"""Ticker suggestions and search functionality."""
import logging
from typing import List, Optional, Dict

logger = logging.getLogger(__name__)

# Common stock tickers organized by popularity
POPULAR_TICKERS = [
    "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "JPM", "V", "WMT",
    "JNJ", "PG", "ASML", "MA", "ADBE", "NFLX", "CRM", "PYPL", "AMD", "COST",
]

# Extended list of common tickers by exchange and sector
US_STOCKS = {
    "TECH": ["AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "META", "NVDA", "TESLA", "ADBE", "CRM", "NFLX", "PYPL", "SQ", "TEAM", "DBX", "OKTA"],
    "FINANCE": ["JPM", "BAC", "WFC", "GS", "MS", "BLK", "AXP", "MMC", "AON", "ICE"],
    "HEALTHCARE": ["JNJ", "UNH", "PFE", "ABBV", "TMO", "MRK", "GILD", "REGN", "VRTX", "ILMN"],
    "INDUSTRIAL": ["BA", "CAT", "DE", "GE", "HON", "MMM", "UPS", "XOM", "CVX", "MPC"],
    "RETAIL": ["WMT", "TGT", "COST", "HD", "LOW", "MCD", "NKE", "SBUX", "AMRX", "ULTA"],
}

# Comprehensive Global Stock Exchanges Information
EXCHANGE_INFO: Dict[str, Dict] = {
    # 🇺🇸 United States
    "NASDAQ": {
        "currency": "USD",
        "currency_symbol": "$",
        "country": "United States",
        "region": "North America",
        "timezone": "EST",
        "market_hours": "9:30-16:00",
        "sample_tickers": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
    },
    "NYSE": {
        "currency": "USD",
        "currency_symbol": "$",
        "country": "United States",
        "region": "North America",
        "timezone": "EST",
        "market_hours": "9:30-16:00",
        "sample_tickers": ["JPM", "BAC", "WFC", "XOM", "CVX"],
    },
    "AMEX": {
        "currency": "USD",
        "currency_symbol": "$",
        "country": "United States",
        "region": "North America",
        "timezone": "EST",
        "market_hours": "9:30-16:00",
        "sample_tickers": ["AEG", "AEHR", "AEON", "AEPI", "AERC"],
    },

    # 🇨🇦 Canada
    "TSX": {
        "currency": "CAD",
        "currency_symbol": "C$",
        "country": "Canada",
        "region": "North America",
        "timezone": "EST",
        "market_hours": "9:30-16:00",
        "sample_tickers": ["RY", "TD", "BN", "CM", "BCE"],
    },

    # 🇲🇽 Mexico
    "BMV": {
        "currency": "MXN",
        "currency_symbol": "$",
        "country": "Mexico",
        "region": "North America",
        "timezone": "CST",
        "market_hours": "8:30-15:00",
        "sample_tickers": ["GFSUSD", "ASURB", "BIMBOA", "CEMEXCPO", "WALMEX"],
    },

    # 🇬🇧 United Kingdom
    "LSE": {
        "currency": "GBP",
        "currency_symbol": "£",
        "country": "United Kingdom",
        "region": "Europe",
        "timezone": "GMT",
        "market_hours": "8:00-16:30",
        "sample_tickers": ["HSBA", "LLOY", "BARB", "NWG", "RBS"],
    },

    # 🇩🇪 Germany
    "XETRA": {
        "currency": "EUR",
        "currency_symbol": "€",
        "country": "Germany",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "8:00-20:00",
        "sample_tickers": ["SAP", "SIE", "VOW3", "DAI", "ALV"],
    },

    "Frankfurt": {
        "currency": "EUR",
        "currency_symbol": "€",
        "country": "Germany",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "8:00-20:00",
        "sample_tickers": ["SAP", "SIE", "VOW3", "DAI", "ALV"],
    },

    # 🇫🇷 France
    "Euronext Paris": {
        "currency": "EUR",
        "currency_symbol": "€",
        "country": "France",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:30",
        "sample_tickers": ["MC", "OR", "AI", "NOKIA", "ASML"],
    },

    # 🇨🇭 Switzerland
    "SIX Swiss": {
        "currency": "CHF",
        "currency_symbol": "CHF",
        "country": "Switzerland",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:30",
        "sample_tickers": ["NOVN", "RHHBY", "ASML", "ROG", "UHR"],
    },

    # 🇳🇱 Netherlands
    "Euronext Amsterdam": {
        "currency": "EUR",
        "currency_symbol": "€",
        "country": "Netherlands",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:30",
        "sample_tickers": ["ASML", "UNVR", "AKZA", "RDSA", "ADYEN"],
    },

    # 🇮🇹 Italy
    "Borsa Italiana": {
        "currency": "EUR",
        "currency_symbol": "€",
        "country": "Italy",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:25",
        "sample_tickers": ["ENI", "ENEL", "ISP", "URW", "TEN"],
    },

    # 🇪🇸 Spain
    "Bolsa de Madrid": {
        "currency": "EUR",
        "currency_symbol": "€",
        "country": "Spain",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:30",
        "sample_tickers": ["IBE", "BBVA", "SAN", "REP", "AENA"],
    },

    # 🇸🇪 Sweden
    "Nasdaq Stockholm": {
        "currency": "SEK",
        "currency_symbol": "kr",
        "country": "Sweden",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:30",
        "sample_tickers": ["ERIC", "ASTAV", "SWEDA", "VOLVA", "SAND"],
    },

    # 🇩🇰 Denmark
    "Nasdaq Copenhagen": {
        "currency": "DKK",
        "currency_symbol": "kr",
        "country": "Denmark",
        "region": "Europe",
        "timezone": "CET",
        "market_hours": "9:00-17:00",
        "sample_tickers": ["NOVO", "JYSK", "AAPL", "NVO", "ISS"],
    },

    # 🇯🇵 Japan
    "Tokyo Stock Exchange": {
        "currency": "JPY",
        "currency_symbol": "¥",
        "country": "Japan",
        "region": "Asia Pacific",
        "timezone": "JST",
        "market_hours": "9:00-15:00",
        "sample_tickers": ["7203", "6758", "6861", "8306", "8604"],
    },

    "Japan Exchange Group": {
        "currency": "JPY",
        "currency_symbol": "¥",
        "country": "Japan",
        "region": "Asia Pacific",
        "timezone": "JST",
        "market_hours": "9:00-15:00",
        "sample_tickers": ["7203", "6758", "6861", "8306", "8604"],
    },

    # 🇦🇺 Australia
    "ASX": {
        "currency": "AUD",
        "currency_symbol": "A$",
        "country": "Australia",
        "region": "Asia Pacific",
        "timezone": "AEST",
        "market_hours": "10:00-16:00",
        "sample_tickers": ["WBC", "ANZ", "CBA", "BHP", "RIO"],
    },

    # 🇳🇿 New Zealand
    "NZX": {
        "currency": "NZD",
        "currency_symbol": "NZ$",
        "country": "New Zealand",
        "region": "Asia Pacific",
        "timezone": "NZST",
        "market_hours": "10:00-16:00",
        "sample_tickers": ["ANZ", "CER", "AIR", "FBU", "Metlifecare"],
    },

    # 🇭🇰 Hong Kong
    "HKEX": {
        "currency": "HKD",
        "currency_symbol": "HK$",
        "country": "Hong Kong",
        "region": "Asia Pacific",
        "timezone": "HKT",
        "market_hours": "9:30-16:00",
        "sample_tickers": ["0700", "0005", "0011", "0016", "0066"],
    },

    # 🇸🇬 Singapore
    "SGX": {
        "currency": "SGD",
        "currency_symbol": "S$",
        "country": "Singapore",
        "region": "Asia Pacific",
        "timezone": "SGT",
        "market_hours": "9:00-17:00",
        "sample_tickers": ["C6L", "O39", "U11", "M44U", "BS6"],
    },

    # 🇮🇳 India
    "NSE": {
        "currency": "INR",
        "currency_symbol": "₹",
        "country": "India",
        "region": "Asia Pacific",
        "timezone": "IST",
        "market_hours": "9:15-15:30",
        "sample_tickers": ["RELIANCE", "HDFCBANK", "INFOSY", "TCS", "ICICIBANK"],
    },

    "BSE": {
        "currency": "INR",
        "currency_symbol": "₹",
        "country": "India",
        "region": "Asia Pacific",
        "timezone": "IST",
        "market_hours": "9:15-15:30",
        "sample_tickers": ["RELIANCE", "HDFCBANK", "INFOSY", "TCS", "ICICIBANK"],
    },

    # 🇨🇳 China
    "Shanghai Exchange": {
        "currency": "CNY",
        "currency_symbol": "¥",
        "country": "China",
        "region": "Asia Pacific",
        "timezone": "CST",
        "market_hours": "9:30-15:00",
        "sample_tickers": ["600000", "600019", "600519", "601398", "601988"],
    },

    "Shenzhen Exchange": {
        "currency": "CNY",
        "currency_symbol": "¥",
        "country": "China",
        "region": "Asia Pacific",
        "timezone": "CST",
        "market_hours": "9:30-15:00",
        "sample_tickers": ["000001", "000651", "000858", "000651", "000333"],
    },

    # 🇧🇷 Brazil
    "B3": {
        "currency": "BRL",
        "currency_symbol": "R$",
        "country": "Brazil",
        "region": "South America",
        "timezone": "BRT",
        "market_hours": "10:00-17:55",
        "sample_tickers": ["VALE3", "PETR4", "ITUB4", "ABEV3", "BBDC4"],
    },

    # 🇲🇽 Mexico (Alternative)
    "Mexico Stock Exchange": {
        "currency": "MXN",
        "currency_symbol": "$",
        "country": "Mexico",
        "region": "North America",
        "timezone": "CST",
        "market_hours": "8:30-15:00",
        "sample_tickers": ["GFSUSD", "ASURB", "BIMBOA", "CEMEXCPO", "WALMEX"],
    },

    # 🇿🇦 South Africa
    "JSE": {
        "currency": "ZAR",
        "currency_symbol": "R",
        "country": "South Africa",
        "region": "Africa",
        "timezone": "SAST",
        "market_hours": "9:00-16:00",
        "sample_tickers": ["NPN", "REM", "MTN", "NRP", "AGL"],
    },

    # 🇦🇪 United Arab Emirates
    "DFM": {
        "currency": "AED",
        "currency_symbol": "د.إ",
        "country": "United Arab Emirates",
        "region": "Middle East",
        "timezone": "GST",
        "market_hours": "10:00-15:00",
        "sample_tickers": ["EMAAR", "DAMAC", "DIC", "EIB", "FAB"],
    },

    "ADX": {
        "currency": "AED",
        "currency_symbol": "د.إ",
        "country": "United Arab Emirates",
        "region": "Middle East",
        "timezone": "GST",
        "market_hours": "10:00-15:00",
        "sample_tickers": ["ADANIPORTS", "TATASTEEL", "SBIN", "LT", "BAJAJFINSV"],
    },
}

# Comprehensive list of common tickers
ALL_TICKERS = [
    # Technology
    "AAPL", "ADBE", "ADSK", "AMD", "AMZN", "ANET", "ANSS", "ASML", "AVGO", "AXON",
    "BKNG", "CDNS", "CHKP", "CMCSA", "COST", "CPRT", "CRWD", "CRM", "CSCO", "CSGP",
    "CTAS", "CTRA", "DASH", "DATA", "DBX", "DDOG", "DOCU", "DXCM", "EBAY", "ENPH",
    "EXPE", "FTNT", "GDDY", "GILD", "GOOG", "GOOGL", "GRMN", "GRUB", "HUBS", "ILMN",
    "INTU", "ISRG", "JKHY", "KLAC", "LRCX", "LUMN", "LUNR", "MCHP", "META", "MGNI",
    "MNDY", "MRNA", "MSFT", "MTSI", "MYRG", "NEGG", "NFLX", "NKTR", "NRDZ", "NTAP",
    "NVDA", "NVMI", "NWLI", "OKTA", "OTEX", "PAYX", "PAYC", "PLTR", "PTON", "PYPL",
    "QCOM", "QRVO", "RGHT", "RMDS", "ROKU", "RPD", "RSTI", "SAIC", "SANM", "SBNY",
    "SGEN", "SHOO", "SIRI", "SQ", "SSNC", "SWKS", "TEAM", "TECH", "TECK", "TENB",
    "TFII", "TSLA", "TSLP", "TTWO", "TWLO", "TWST", "TXRH", "UBER", "ULTA", "UMPQ",
    "UPST", "VEEV", "VFIV", "VISTRA", "VMLP", "VMPL", "VMWD", "VOD", "VRNS", "VRSN",
    "VRTX", "VRTU", "VSAT", "VTOL", "WDC", "WDAY", "WFRD", "WIRE", "WLDN", "XRAY",
    "YAHOO", "ZEN", "ZETA", "ZION", "ZLAB", "ZLRE", "ZOOM",

    # Finance
    "AEL", "AEP", "AET", "AFL", "AFT", "AGX", "AIG", "AIZ", "ALL", "AMP",
    "AME", "AMP", "AMT", "APG", "AQN", "ASIX", "AWH", "AXE", "AXP", "AZO",
    "BAC", "BAH", "BAP", "BBDC", "BBDO", "BBL", "BCO", "BCS", "BDX", "BFAM",
    "BFB", "BFS", "BFY", "BGS", "BH", "BHF", "BHP", "BHR", "BHS", "BIP",
    "BK", "BKD", "BKE", "BKI", "BKR", "BKU", "BL", "BLK", "BLL", "BLX",
    "BMI", "BMR", "BMS", "BN", "BNH", "BNR", "BNY", "BP", "BPT", "BQ",
    "BRC", "BRD", "BRG", "BRI", "BRKS", "BRL", "BRKR", "BRLI", "BRLR", "BRP",
    "BRPT", "BRR", "BRT", "BRY", "BSAC", "BSD", "BSET", "BSL", "BSLI", "BSPI",
    "BSRR", "BSTC", "BSTO", "BT", "BTA", "BTAF", "BTG", "BTI", "BTOM", "BTU",
    "BUA", "BUBC", "BUDD", "BUI", "BUILT", "BULK", "BULL", "BUMP", "BUNX", "BUR",

    # Healthcare
    "ABMD", "ABT", "ACAB", "ACAD", "ACET", "ACGL", "ACHC", "ACIM", "ACMR", "ACNB",
    "ACRS", "ACST", "ACWX", "ADAP", "ADAT", "ADBE", "ADCT", "ADEA", "ADEM", "ADES",
    "ADEX", "ADFB", "ADIG", "ADIL", "ADIO", "ADMD", "ADMS", "ADNB", "ADOS", "ADPT",
    "ADRA", "ADRX", "ADS", "ADSK", "ADUR", "ADVA", "ADVB", "ADVM", "ADVP", "ADVS",
    "ADWS", "ADYEY", "AEGN", "AEGP", "AEHR", "AEMD", "AEON", "AEPI", "AERC", "AERM",
    "AERO", "AERS", "AERU", "AESF", "AESI", "AEST", "AEUA", "AEUB", "AEUC", "AEUD",
    "AEUS", "AEVA", "AEVI", "AEWA", "AEXF", "AEXS", "AEYC", "AEYE", "AEZR", "AFAI",

    # Industrial/Energy
    "BA", "BAX", "BCAC", "BCOW", "BDGE", "BDN", "BDRA", "BEN", "BENX", "BFAO",
    "BG", "BGAC", "BGAU", "BGB", "BGBA", "BGBP", "BGBW", "BGCP", "BGG", "BGGE",
    "BGHAI", "BGHC", "BGHI", "BGIT", "BGIV", "BGLC", "BGLD", "BGLI", "BGLS", "BGMC",
    "BGMD", "BGMG", "BGMH", "BGMI", "BGML", "BGMO", "BGMS", "BGMT", "BGMU", "BGMV",
    "BGMX", "BGMZ", "BGNC", "BGND", "BGNE", "BGNF", "BGNG", "BGNH", "BGNI", "BGNJ",

    # Retail/Consumer
    "CAL", "CAR", "CARE", "CARF", "CARP", "CARS", "CART", "CARV", "CASE", "CASH",
    "CASS", "CAST", "CASY", "CAT", "CATA", "CATC", "CATE", "CATF", "CATH", "CATO",
    "CATP", "CATS", "CATT", "CATU", "CATV", "CATY", "CAUD", "CAUE", "CAUL", "CAUP",
    "CAUR", "CAUSA", "CAUSE", "CAUS", "CAUTX", "CAUU", "CAUV", "CAUW", "CAUZ", "CAV",
    "CAVA", "CAVE", "CAVM", "CAVS", "CAVU", "CAVY", "CAWA", "CAWC", "CAWD", "CAWE",
    "CAWF", "CAWG", "CAWH", "CAWI", "CAWJ", "CAWK", "CAWL", "CAWM", "CAWN", "CAWO",
]


class TickerSuggestions:
    """Manage ticker suggestions and search functionality."""

    @staticmethod
    def search(query: str, exchange: Optional[str] = None) -> List[str]:
        """
        Search for tickers matching the query.

        Args:
            query: Search query (ticker prefix)
            exchange: Optional exchange filter (e.g., 'NASDAQ', 'NYSE')

        Returns:
            List of matching ticker symbols
        """
        if not query:
            return TickerSuggestions.get_all_tickers()

        query_upper = query.upper().strip()
        results = [ticker for ticker in ALL_TICKERS if ticker.startswith(query_upper)]

        # Filter by exchange if provided
        if exchange:
            results = TickerSuggestions._filter_by_exchange(results, exchange)

        return sorted(results)

    @staticmethod
    def get_all_tickers() -> List[str]:
        """
        Get all available tickers.

        Returns:
            Sorted list of all ticker symbols
        """
        return sorted(list(set(ALL_TICKERS)))

    @staticmethod
    def get_popular_tickers() -> List[str]:
        """
        Get the most popular/traded tickers.

        Returns:
            List of popular ticker symbols
        """
        return POPULAR_TICKERS.copy()

    @staticmethod
    def get_by_category(category: str) -> List[str]:
        """
        Get tickers by category/sector.

        Args:
            category: Category name (e.g., 'TECH', 'FINANCE', 'HEALTHCARE')

        Returns:
            List of tickers in the specified category, or empty list if not found
        """
        for sectors in US_STOCKS.values():
            if category.upper() in US_STOCKS:
                return sorted(US_STOCKS[category.upper()])
        return []

    @staticmethod
    def get_tickers_by_exchange(exchange: str) -> List[str]:
        """
        Get tickers by exchange.

        Args:
            exchange: Exchange name (e.g., 'NASDAQ', 'NYSE')

        Returns:
            List of tickers on the specified exchange
        """
        # Simplified implementation - returns popular tickers for any exchange
        # In a real application, this would filter against a database
        if exchange.upper() in ["NASDAQ", "NYSE", "AMEX"]:
            return sorted(ALL_TICKERS)
        return []

    @staticmethod
    def get_exchanges() -> List[str]:
        """
        Get list of available exchanges.

        Returns:
            List of exchange names
        """
        return list(EXCHANGE_INFO.keys())

    @staticmethod
    def get_currency(exchange: str) -> str:
        """
        Get currency for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            Currency name (e.g., 'USD', 'EUR')
        """
        return EXCHANGE_INFO.get(exchange.upper(), {}).get("currency", "USD")

    @staticmethod
    def get_currency_symbol(exchange: str) -> str:
        """
        Get currency symbol for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            Currency symbol (e.g., '$', '€')
        """
        return EXCHANGE_INFO.get(exchange.upper(), {}).get("currency_symbol", "$")

    @staticmethod
    def get_country(exchange: str) -> str:
        """
        Get country for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            Country name
        """
        return EXCHANGE_INFO.get(exchange.upper(), {}).get("country", "Unknown")

    @staticmethod
    def get_timezone(exchange: str) -> str:
        """
        Get timezone for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            Timezone (e.g., 'EST', 'CET')
        """
        return EXCHANGE_INFO.get(exchange.upper(), {}).get("timezone", "Unknown")

    @staticmethod
    def get_region(exchange: str) -> str:
        """
        Get region for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            Region name (e.g., 'North America', 'Europe', 'Asia Pacific')
        """
        return EXCHANGE_INFO.get(exchange, {}).get("region", "Unknown")

    @staticmethod
    def get_market_hours(exchange: str) -> str:
        """
        Get market hours for an exchange.

        Args:
            exchange: Exchange name

        Returns:
            Market hours (e.g., '9:30-16:00')
        """
        return EXCHANGE_INFO.get(exchange, {}).get("market_hours", "N/A")

    @staticmethod
    def get_sample_tickers(exchange: str, count: int = 5) -> List[str]:
        """
        Get sample tickers for an exchange.

        Args:
            exchange: Exchange name
            count: Number of samples to return

        Returns:
            List of sample ticker symbols
        """
        samples = EXCHANGE_INFO.get(exchange.upper(), {}).get("sample_tickers", [])
        return samples[:count]

    @staticmethod
    def _filter_by_exchange(tickers: List[str], exchange: str) -> List[str]:
        """
        Filter tickers by exchange (internal helper).

        Args:
            tickers: List of tickers to filter
            exchange: Exchange name

        Returns:
            Filtered list of tickers
        """
        # In a real application, this would use a ticker database
        # For now, return all if exchange is valid
        if exchange.upper() in ["NASDAQ", "NYSE", "AMEX"]:
            return tickers
        return tickers
