# Quick Start: Country Stock Filter

## 🚀 What's New?

Added a **Country Dropdown** to filter stocks by country. Now you can:
- Select a country 🌍
- See stocks only from that country 📊
- Get smart autocomplete suggestions 💡

---

## 🎯 How to Use

### Step-by-Step Guide

1. **Run the application**
   ```bash
   python -m scrapematrix
   ```

2. **See the new Country dropdown**
   ```
   ┌─────────────────────────────────────────┐
   │ Country: [🌍 All Countries ▼]           │
   │ Stock Ticker: [start typing...]         │
   │ Period: [1y ▼]  [Fetch Data]           │
   └─────────────────────────────────────────┘
   ```

3. **Select a country** (click dropdown)
   - 🌍 All Countries (shows all stocks)
   - 🇺🇸 United States (70+ stocks)
   - 🇨🇦 Canada (15 stocks)
   - 🇬🇧 United Kingdom (15 stocks)
   - 🇯🇵 Japan (10 stocks)
   - 🇩🇪 Germany (10 stocks)
   - 🇫🇷 France (10 stocks)
   - 🇭🇰 Hong Kong (10 stocks)
   - 🇮🇳 India (10 stocks)
   - 🇦🇺 Australia (15 stocks)
   - 🇸🇬 Singapore (5 stocks)

4. **Type in Stock Ticker field**
   - See suggestions from selected country only!
   - Example: Select 🇺🇸 USA, type "A" → See AAPL, AMZN, AMD, ...

5. **Select a stock** from the dropdown

6. **Click "Fetch Data"** to load stock information

---

## 📊 Available Stocks by Country

### 🇺🇸 United States (70+ stocks)
**Technology:** AAPL, GOOGL, MSFT, AMZN, TSLA, META, NVDA, INTEL, AMD, QCOM, CRM, ADBE
**Finance:** JPM, BAC, WFC, GS, MS, BLK, SCHW, COIN
**Healthcare:** JNJ, PFE, MRNA, ABBV, TMO, LLY, AZN, BNTX
**Consumer:** WMT, TGT, COST, MCD, NKE, HD, EBAY
**Energy:** XOM, CVX, COP, SLB, EOG, MPC, PSX, VLO
**Industrial:** BA, CAT, MMM, GE, HON, RTX, LMT, NOC
**Utilities:** NEE, DUK, SO, AEP, EXC, PEG, SRE, AWK
**Real Estate:** XLRE, PLD, AMT, CCI, EQIX, WELL, SPG, PSA
**Communications:** VZ, T, CMCSA, CHTR, TMUS, DISH

### 🇨🇦 Canada
RY, TD, BNS, CM, BMO, ENB, TRP, CNQ, SU, CVE, BTO, BAM, GIB, WCP, AR, SHOP, LSPD, CNR, MRU

### 🇬🇧 United Kingdom
BARCLAYS, HSBA, STAN, NWG, SHELL, BP, SGE, ULVR, DGE, SBRY, GLEN, ANTM, RIO, GSK, HALEON, AZN

### 🇯🇵 Japan
7203 (Toyota), 6758 (Sony), 9984 (SoftBank), 8306 (Mizuho), 8411 (Sumitomo), 8001 (Nomura)

### 🇩🇪 Germany
SAP, SIE, DAI, BMW, BASF, HEN3, DBK, ARL, MUV2

### 🇫🇷 France
LVMH, OREP, DXPE, BNPP, GLE, KN, EDF, ENGI, VIE

### 🇭🇰 Hong Kong
0001 (HSBC), 0002 (CLP), 0003 (HKExch), 0005 (AEON), 0700 (Tencent), 9988 (Alibaba), 0016, 0083, 0153, 1928

### 🇮🇳 India
TCS, INFY, WIPRO, HDBK, ICICIBANK, AXISBANK, MARUTI, TATA, SUNPHARMA, CIPLA, ITC, NESTLEIND

### 🇦🇺 Australia
ANZ, WBC, NAB, CBA, BHP, RIO, FMG, WES, APA, ORI, DJS, TEL

### 🇸🇬 Singapore
OCBC, DBS, UOB, SEATRADE, CAPITALAND, OXLEY

---

## 🎬 Example Workflows

### Workflow 1: Find US Tech Stocks
```
1. Country: Select 🇺🇸 United States
2. Ticker: Type "N" → See NVDA, NKE, ...
3. Select NVDA
4. Period: Keep 1y
5. Click "Fetch Data"
6. View NVIDIA stock data!
```

### Workflow 2: Compare Banks Across Countries
```
1. Country: 🇺🇸 USA → Search JPM → Fetch
2. Country: 🇨🇦 Canada → Search RY → Fetch
3. Country: 🇬🇧 UK → Search HSBA → Fetch
4. Compare performance across markets
```

### Workflow 3: Explore Canadian Energy
```
1. Country: 🇨🇦 Canada
2. Ticker: Type "EN" → See ENB (Enbridge)
3. Select ENB
4. Fetch and analyze Canada's top energy company
```

---

## 💡 Tips & Tricks

### Tip 1: Use "All Countries" to Browse
- Don't know which country? Select 🌍 All Countries
- Browse by typing letters
- See what's available globally

### Tip 2: Switch Countries Quickly
- Just click the Country dropdown again
- Ticker field clears automatically
- Suggestions update instantly

### Tip 3: International Tickers
- Hong Kong stocks use numeric codes: 0700, 0001, etc.
- Japan stocks also use codes: 6758 (Sony)
- US uses letter codes: AAPL, MSFT, etc.

### Tip 4: Fastest Stocks to Load
- US stocks (most reliable data)
- UK stocks (good data quality)
- Canada stocks (good coverage)
- International stocks (may be slower)

---

## ⚙️ Technical Details

### How It Works:
1. Country dropdown filters the stock database
2. As you type, suggestions come from selected country
3. All suggestions are country-filtered in real-time
4. Stock data fetched from Yahoo Finance

### For Developers:
New methods added to `TickerSuggestions`:

```python
# Get all countries
countries = TickerSuggestions.get_countries()
# ['🇦🇺 Australia', '🇨🇦 Canada', ...]

# Get stocks from country
stocks = TickerSuggestions.get_tickers_by_country("🇺🇸 United States")
# ['AAPL', 'GOOGL', 'MSFT', ...]

# Search in country
results = TickerSuggestions.search("AA", country="🇺🇸 United States")
# ['AAPL', 'AMZN']

# Get sectors in country
sectors = TickerSuggestions.get_sectors_by_country("🇺🇸 United States")
# ['Technology', 'Finance', 'Healthcare', ...]
```

---

## ❓ FAQ

**Q: Can I search all countries at once?**
A: Yes! Select "🌍 All Countries" at the top of the dropdown.

**Q: Why is my international ticker not loading?**
A: Yahoo Finance may not support all tickers. Try popular ones first (TCS, INFY from India, SHOP from Canada).

**Q: How do I add more stocks?**
A: Edit `src/scrapematrix/data/ticker_suggestions.py` and add to the `STOCKS_BY_COUNTRY` dictionary.

**Q: Can I add more countries?**
A: Yes! Just add a new entry to `STOCKS_BY_COUNTRY` with country name, sectors, and stocks.

**Q: Are the stock lists complete?**
A: No, they're curated lists of popular/major stocks. You can always manually enter other tickers!

---

## 🐛 Troubleshooting

**Problem: Dropdown shows "All Countries" but I selected a country**
- Solution: Make sure you clicked on the specific country name, not a blank area

**Problem: Stock data fails to load**
- Solution: Some international stocks may not be available on Yahoo Finance. Try a major US stock instead.

**Problem: Autocomplete is slow**
- Solution: Try pressing Backspace and retyping. It should refresh quickly.

---

## 📈 What's Next?

### Future Enhancements:
1. **Sector Filter** - Filter by industry within country
2. **Watchlists by Country** - Save favorites per country
3. **Country Comparison Charts** - Compare market performance
4. **Real-time Updates** - Live prices by country
5. **Export Data** - Download country-specific data

---

## 🎓 Learning Resources

For detailed information, see:
- `docs/COUNTRY_STOCK_FILTER_FEATURE.md` - Complete feature documentation
- `src/scrapematrix/data/ticker_suggestions.py` - Stock database
- `src/scrapematrix/gui/widgets/stock_viewer.py` - UI implementation

---

**Enjoy exploring stocks from around the world! 🌍📊**
