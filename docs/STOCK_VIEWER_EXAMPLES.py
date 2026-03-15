"""
Stock Viewer Feature - Code Example

This demonstrates how to use the StockDataLoader and StockViewer components.
"""

# ============================================================================
# EXAMPLE 1: Using StockDataLoader directly in Python
# ============================================================================

from scrapematrix.data.loaders import StockDataLoader

# Fetch historical data
df = StockDataLoader.fetch_stock_data(
    ticker="AAPL",
    period="6mo",
    interval="1d"
)

if df is not None:
    print(df.head())
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")

# Get stock information
info = StockDataLoader.get_stock_info("AAPL")
print(f"\nStock Info:")
for key, value in info.items():
    print(f"  {key}: {value}")


# ============================================================================
# EXAMPLE 2: Using StockViewer in GUI
# ============================================================================

# The StockViewer widget is automatically integrated in the main GUI
# Simply run: python -m scrapematrix

# Then:
# 1. Go to "📊 Stock Viewer" tab
# 2. Enter ticker (e.g., "AAPL")
# 3. Select period (default: 1y)
# 4. Click "Fetch Data"
# 5. View chart, info, and historical data in tabs


# ============================================================================
# EXAMPLE 3: Creating a custom data pipeline
# ============================================================================

import asyncio
from scrapematrix.data.loaders import StockDataLoader

async def analyze_multiple_stocks():
    """Analyze multiple stocks concurrently."""
    
    stocks = ["AAPL", "GOOGL", "MSFT", "TSLA"]
    results = {}
    
    for ticker in stocks:
        # Fetch data
        data = StockDataLoader.fetch_stock_data(ticker)
        info = StockDataLoader.get_stock_info(ticker)
        
        if data is not None:
            # Calculate metrics
            latest_price = data['Close'].iloc[-1]
            previous_close = data['Close'].iloc[-2]
            change_percent = ((latest_price - previous_close) / previous_close) * 100
            
            results[ticker] = {
                "current_price": latest_price,
                "change_percent": change_percent,
                "info": info
            }
    
    return results

# Run analysis
results = asyncio.run(analyze_multiple_stocks())

for ticker, data in results.items():
    print(f"\n{ticker}")
    print(f"  Price: ${data['current_price']:.2f}")
    print(f"  Change: {data['change_percent']:.2f}%")


# ============================================================================
# EXAMPLE 4: Useful ticker symbols
# ============================================================================

"""
TECH STOCKS:
- AAPL: Apple
- GOOGL: Alphabet (Google)
- MSFT: Microsoft
- AMZN: Amazon
- TSLA: Tesla
- META: Meta (Facebook)
- NVDA: NVIDIA

FINANCIAL:
- JPM: JPMorgan Chase
- BAC: Bank of America
- GS: Goldman Sachs
- WFC: Wells Fargo

CONSUMER:
- WMT: Walmart
- TGT: Target
- COST: Costco
- MCD: McDonald's

PHARMA:
- JNJ: Johnson & Johnson
- PFE: Pfizer
- MRNA: Moderna
- AZN: AstraZeneca

ENERGY:
- XOM: ExxonMobil
- CVX: Chevron
- COP: ConocoPhillips

UTILITIES:
- NEE: NextEra Energy
- DUK: Duke Energy
"""
