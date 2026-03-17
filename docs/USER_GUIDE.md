# 👥 User Guide

Complete guide to using ScrapeMatrix for stock analysis and market research.

## Getting Started

### First Launch

1. **Run the application:**
   ```bash
   python -m scrapematrix
   ```

2. **Wait for startup:**
   - Loading takes ~2-3 seconds
   - You'll see the main window with two tabs

3. **Explore the interface:**
   - Home tab with feature overview
   - Stock Viewer tab for data analysis

---

## 🏠 Home Tab

The Home tab provides:
- **Feature Overview** - Summary of capabilities
- **Quick Start Tips** - How to get started
- **Navigation Help** - Guide to features

---

## 📊 Stock Viewer Tab

### Main Components

#### 1. Exchange Selector
```
┌─────────────────────────────────────┐
│ Select Exchange: [NASDAQ ▼]        │
│ Currency: 💱 $USD                   │
└─────────────────────────────────────┘
```

**Features:**
- 30+ global exchanges
- Organized by region
- Shows currency and timezone

**How to use:**
1. Click the dropdown
2. Select your exchange
3. Ticker input will update with examples

---

#### 2. Ticker Input
```
┌──────────────────────────────────────┐
│ Ticker: [AAPL            ▼]         │
│ Showing: AAPL, MSFT, GOOGL, ...      │
└──────────────────────────────────────┘
```

**Features:**
- Dynamic autocomplete
- Smart suggestions
- Exchange-specific examples

**How to use:**
1. Click in the input field
2. Start typing (e.g., "AP" for Apple)
3. Select from suggestions
4. Or type full ticker symbol

---

#### 3. Period Selector
```
┌──────────────────────────┐
│ Period: [1y ▼]          │
│ Options: 1mo, 3mo, 6mo,  │
│ 1y, 2y, 5y, max         │
└──────────────────────────┘
```

**Available Periods:**
- **1mo** - Last month
- **3mo** - Last 3 months
- **6mo** - Last 6 months
- **1y** - Last year (recommended)
- **2y** - Last 2 years
- **5y** - Last 5 years
- **max** - All available data

---

#### 4. Fetch Button
```
┌─────────────────────┐
│ [Fetch Data]        │
└─────────────────────┘
```

**Actions:**
- Starts data fetching
- Shows progress bar
- Updates when complete

---

### Status Bar

Shows real-time information:
```
📊 NASDAQ | 🌍 United States (N.America) | 💱 $USD | 🕐 EST | ⏰ 9:30-16:00
```

**Information displayed:**
- Current exchange
- Country and region
- Currency symbol
- Timezone
- Market trading hours

---

## 📈 Data Display Tabs

After fetching data, you'll see three tabs:

### Chart Tab
- **Display:** Interactive line chart
- **Shows:** Stock price over time
- **Features:**
  - Zoom in/out
  - Pan across time
  - Hover for values

### Stock Info Tab
- **Display:** Company information table
- **Shows:** Key metrics and data
- **Information:**
  - Company name
  - Sector
  - Market cap
  - Dividend yield
  - P/E ratio
  - And more

### Historical Data Tab
- **Display:** Price data table
- **Shows:** Last 50 trading days
- **Columns:**
  - Date
  - Open price
  - High price
  - Low price
  - Close price

---

## 🔍 Workflow Examples

### Example 1: Look Up Apple Stock

**Step 1: Select Exchange**
1. Click Exchange dropdown
2. Select "NASDAQ - United States"
3. Notice: Placeholder changes to show US ticker examples

**Step 2: Enter Ticker**
1. Click Ticker input field
2. Type "A" - see suggestions appear
3. Or type "AAPL" completely
4. Press Enter or click suggestion

**Step 3: Choose Period**
1. Click Period dropdown
2. Select "1y" (default, recommended)
3. Or choose another period

**Step 4: Fetch Data**
1. Click "Fetch Data" button
2. Wait for progress bar to complete
3. View chart and information

**Step 5: Analyze**
1. View Chart tab - see price trend over year
2. View Stock Info tab - see company metrics
3. View Historical Data tab - see daily prices

---

### Example 2: Compare Time Periods

**Finding the best period:**

1. Fetch data with 1y period
2. Analyze the price trend
3. Change period to 5y to see longer trend
4. Compare volatility and growth

---

### Example 3: Multi-Exchange Trading

**Trade on different exchanges:**

1. Select "🌍 All Global Exchanges"
2. Type "AAPL" → Search all exchanges
3. Switch exchange:
   - Select NYSE
   - Type "JPM" (JP Morgan)
   - Fetch data
4. Compare with other exchanges

---

## 🌍 Global Exchanges

### Supported Exchanges

**United States (3):**
- NASDAQ
- NYSE
- AMEX

**Canada:**
- TSX

**Europe (10):**
- LSE (UK)
- XETRA (Germany)
- Frankfurt (Germany)
- Euronext Paris (France)
- SIX Swiss (Switzerland)
- Euronext Amsterdam (Netherlands)
- Borsa Italiana (Italy)
- Bolsa de Madrid (Spain)
- Nasdaq Stockholm (Sweden)
- Nasdaq Copenhagen (Denmark)

**Asia-Pacific (10):**
- Tokyo Stock Exchange (Japan)
- ASX (Australia)
- HKEX (Hong Kong)
- SGX (Singapore)
- NSE (India)
- BSE (India)
- Shanghai Exchange (China)
- Shenzhen Exchange (China)
- NZX (New Zealand)
- And more...

---

## 📊 Understanding the Data

### Chart
- **X-axis:** Time period (dates)
- **Y-axis:** Stock price ($)
- **Line:** Price movement
- **Green uptrend:** Prices rising
- **Red downtrend:** Prices falling

### Stock Information
- **Market Cap:** Total value of company
- **P/E Ratio:** Price to Earnings ratio
- **Dividend:** Cash returned to shareholders
- **52 Week High/Low:** Year price range
- **Volume:** Trading activity

### Historical Data
- **Open:** Price at market open
- **High:** Highest price that day
- **Low:** Lowest price that day
- **Close:** Price at market close
- **Volume:** Trading volume (optional)

---

## ⚙️ Tips & Tricks

### Tip 1: Autocomplete
- Start typing to see suggestions
- Suggestions update dynamically
- Arrow keys to navigate
- Enter to select

### Tip 2: Exchange Information
- Status bar shows market hours
- Check if market is currently open
- Different exchanges have different hours

### Tip 3: Ticker Format
- US stocks: Letter symbols (AAPL, MSFT)
- Japanese: Numbers (7203, 6758)
- Hong Kong: Numbers (0700, 0005)
- Placeholder shows format for selected exchange

### Tip 4: Error Handling
- "Symbol not found" - Check ticker spelling
- "Rate limited" - Wait a few seconds
- "No data found" - Stock might be delisted

### Tip 5: Data Interpretation
- Recent trends show momentum
- Compare different periods
- Look for support/resistance levels
- Volume confirms price moves

---

## ⚠️ Troubleshooting

### "No Data Found"
**Cause:** Stock doesn't exist or is delisted
**Solution:**
- Check ticker spelling
- Try a different stock
- Use autocomplete to verify

### "Rate Limited"
**Cause:** Too many requests to Yahoo Finance
**Solution:**
- Wait 30 seconds
- Try another ticker
- Come back later

### "Connection Error"
**Cause:** No internet connection
**Solution:**
- Check internet connection
- Try again in a moment
- Check router/WiFi

### "UI Freezing"
**Cause:** Application is loading data
**Solution:**
- Wait for progress bar
- Don't click repeatedly
- Check status bar for progress

### Chart Not Displaying
**Cause:** No data loaded yet
**Solution:**
- Fetch data first
- Check error messages
- Try different ticker

---

## 🎓 Learning Resources

### For More Information
- Read [FEATURES.md](FEATURES.md) for feature details
- Read [EXCHANGES.md](EXCHANGES.md) for exchange info
- Check [FAQ.md](FAQ.md) for common questions
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for help

---

## 🎯 Common Tasks

| Task | Steps |
|------|-------|
| **Look up a stock** | Select exchange → Enter ticker → Click Fetch |
| **See 5-year trend** | Select 5y period → Fetch data |
| **Compare time periods** | Fetch 1y, then fetch 5y in separate sessions |
| **Find ticker symbol** | Start typing in ticker input, see suggestions |
| **Check market hours** | Look at status bar for selected exchange |
| **See company info** | Click "Stock Info" tab after fetching |
| **View daily prices** | Click "Historical Data" tab after fetching |
| **Track a stock** | Fetch same stock regularly, note prices |

---

## 📞 Support

- **Documentation:** Read the docs/ folder
- **FAQ:** Check [FAQ.md](FAQ.md)
- **Issues:** Report on GitHub
- **Troubleshooting:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
