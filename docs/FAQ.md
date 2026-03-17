# ❓ Frequently Asked Questions (FAQ)

Common questions about ScrapeMatrix and their answers.

## 🚀 Getting Started

### Q: What is ScrapeMatrix?
**A:** ScrapeMatrix is a professional desktop application for stock market analysis. It fetches real-time and historical stock data from Yahoo Finance and displays it with interactive charts and information tables.

### Q: How do I install it?
**A:** See [INSTALLATION.md](INSTALLATION.md) for complete installation instructions. Quick version:
```bash
git clone https://github.com/x-0rg/ScrapeMatrix.git
cd ScrapeMatrix
pip install -e .
python -m scrapematrix
```

### Q: What are the system requirements?
**A:** 
- Python 3.8 or higher
- 2GB RAM minimum
- 500MB disk space
- Internet connection (for stock data)
- Any OS: Windows, macOS, Linux

### Q: Is it free?
**A:** Yes! ScrapeMatrix is completely free and open source (MIT License).

### Q: Do I need an account?
**A:** No account needed. Stock data comes from Yahoo Finance (free public API).

---

## 💻 Installation Issues

### Q: "Python not found" error
**A:** Install Python from https://www.python.org. Make sure to check "Add Python to PATH" during installation.

### Q: "Module not found" when installing
**A:** 
```bash
# Update pip first
pip install --upgrade pip

# Try installing again
pip install -e .

# If still fails, try:
pip cache purge
pip install -e . --force-reinstall
```

### Q: Virtual environment won't activate
**A:** 
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows CMD: `.venv\Scripts\activate.bat`
- macOS/Linux: `source .venv/bin/activate`

### Q: PyQt6 won't install
**A:** 
```bash
# Try conda
conda install -c conda-forge pyqt6

# Or upgrade pip
pip install --upgrade pip
pip install PyQt6
```

---

## 🎯 Using the Application

### Q: How do I look up a stock?
**A:** 
1. Select an exchange from the dropdown
2. Type the ticker symbol (e.g., AAPL)
3. Select a time period
4. Click "Fetch Data"

### Q: What's a ticker symbol?
**A:** A short code for a stock. Examples:
- AAPL = Apple
- MSFT = Microsoft
- GOOGL = Google
- JPM = JP Morgan
- 0700 = Tencent (Hong Kong)

### Q: Can I look up international stocks?
**A:** Yes! Select the appropriate exchange:
- NASDAQ/NYSE for US
- XETRA for Germany
- LSE for UK
- HKEX for Hong Kong
- etc.

### Q: What time periods are available?
**A:**
- 1mo = 1 month of daily data
- 3mo = 3 months
- 6mo = 6 months
- 1y = 1 year (recommended)
- 2y = 2 years
- 5y = 5 years
- max = all available data (can be 50+ years)

### Q: Why are some data points missing?
**A:** Stock data might be missing if:
- Company was delisted
- Trading stopped temporarily
- Holidays (markets closed)
- Data is not available from Yahoo Finance

---

## 📊 Data & Visualization

### Q: What data is shown?
**A:** Three tabs display:
1. **Chart:** Price movement over time
2. **Stock Info:** Company metrics (P/E, dividend, etc.)
3. **Historical Data:** Daily prices (last 50 days)

### Q: Can I download the data?
**A:** Currently: Copy from tables (Ctrl+C)
- Future: CSV, JSON, PDF export (coming soon)

### Q: Why is the chart not displaying?
**A:** 
- Make sure you clicked "Fetch Data"
- Wait for the progress bar to complete
- Check for error messages in status bar
- Try a different stock

### Q: Can I zoom into the chart?
**A:** Matplotlib chart features:
- Scroll to zoom
- Click-drag to pan
- Right-click to reset
- Toolbar buttons (coming soon)

---

## 🔍 Search & Autocomplete

### Q: How does autocomplete work?
**A:** Start typing in the ticker field:
- Shows matching tickers instantly
- Select from dropdown or finish typing
- Press Enter to search

### Q: Can I search by company name?
**A:** Currently: Only ticker symbols
- Future: Company name search (v0.3)

### Q: Why don't I see any suggestions?
**A:** 
- Ticker database might be limited
- Try typing more characters
- Verify spelling
- Use full ticker symbol

### Q: What if I can't find a ticker?
**A:** 
- Check stock exchange's website
- Verify the company is publicly traded
- Check if recently delisted
- Try different spelling

---

## 🌍 Exchanges

### Q: How many exchanges are supported?
**A:** 30+ global exchanges across 6 regions:
- North America: 6
- Europe: 10
- Asia-Pacific: 10
- South America: 1
- Africa: 1
- Middle East: 2

### Q: Can I trade on all exchanges?
**A:** You can view data from all exchanges. Actual trading requires a brokerage account (not included in app).

### Q: What if my exchange isn't listed?
**A:** 
- Let us know via GitHub issue
- We plan to add more exchanges
- Contribute: See [CONTRIBUTING.md](CONTRIBUTING.md)

### Q: What are market hours?
**A:** Check the status bar when you select an exchange. Shows trading hours in local timezone.

---

## ⚠️ Errors & Troubleshooting

### Q: "Symbol not found" error
**A:** The ticker symbol doesn't exist or data unavailable:
- Check ticker spelling
- Try autocomplete to verify
- Stock might be delisted
- Try a different stock

### Q: "Rate Limited" error
**A:** Yahoo Finance limits requests:
- Wait 30-60 seconds
- Try another stock
- Come back later
- Use less frequently

### Q: "No data available"
**A:** Yahoo Finance has no data for this stock:
- Stock might be too new
- Company might be delisted
- Symbol might be wrong
- Try another stock

### Q: Application crashes
**A:** 
- Check error message
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Report issue on GitHub

### Q: UI freezes when loading
**A:** This shouldn't happen. If it does:
- Check internet connection
- Wait for progress bar
- Restart application
- Report bug with details

---

## 🔧 Performance

### Q: Why is it slow?
**A:** Possible causes:
- Slow internet connection
- Large time period (max data)
- Computer is busy
- Yahoo Finance is slow

**Solutions:**
- Check internet speed
- Use shorter period (1y instead of max)
- Close other applications
- Try again later

### Q: How much data can it handle?
**A:** 
- Can display 10+ years of daily data
- Handles 750+ tickers
- Multiple exchanges simultaneously

### Q: Will it work on my computer?
**A:** If it meets requirements:
- Python 3.8+
- 2GB RAM
- 500MB disk
- Modern graphics

---

## 🆘 Getting Help

### Q: Where can I report bugs?
**A:** 
- GitHub Issues: https://github.com/x-0rg/ScrapeMatrix/issues
- Jira Board: https://x-0rg.atlassian.net/jira/software/projects/SCRAMX/boards/1

### Q: How do I ask questions?
**A:**
- GitHub Discussions (coming soon)
- GitHub Issues
- Check FAQ and docs first

### Q: Where can I suggest features?
**A:**
- GitHub Issues (Feature Request)
- GitHub Discussions
- Jira board

### Q: Is there documentation?
**A:** Yes! Comprehensive docs in `/docs`:
- [QUICKSTART.md](QUICKSTART.md) - Get started quickly
- [USER_GUIDE.md](USER_GUIDE.md) - How to use
- [ARCHITECTURE.md](ARCHITECTURE.md) - How it works
- Many more...

---

## 🤝 Contributing

### Q: Can I contribute?
**A:** Yes! All contributions welcome:
- Code (features, fixes)
- Documentation
- Testing
- Bug reports
- Ideas

See [CONTRIBUTING.md](CONTRIBUTING.md)

### Q: I found a bug, what should I do?
**A:**
1. Check TROUBLESHOOTING.md
2. Search existing issues
3. Create new issue with:
   - Clear description
   - Steps to reproduce
   - Error message
   - System info

### Q: How can I help?
**A:**
- Test the application
- Report issues
- Improve documentation
- Create pull requests
- Share feedback

---

## 📝 Data & Privacy

### Q: What data does the app collect?
**A:** Nothing! No data collection:
- No tracking
- No analytics
- No personal info
- All data is local

### Q: Is my data safe?
**A:** 
- No external servers used
- Only connects to Yahoo Finance API
- Public data only
- Your computer only

### Q: Can I export my data?
**A:** 
- Currently: Copy from tables
- Future: CSV, JSON export (v0.2)

---

## 🔐 Security

### Q: Is it safe to use?
**A:** Yes! Security features:
- No account required
- No personal data
- Open source (reviewed by community)
- MIT licensed

### Q: What about my internet connection?
**A:** Only connects to:
- Yahoo Finance API (public data)
- No login required
- HTTPS/secure connection
- Standard traffic

---

## 🎓 Learning & Resources

### Q: How do I learn to use it?
**A:**
1. Read [QUICKSTART.md](QUICKSTART.md) (5 min)
2. Run application
3. Try example (AAPL stock)
4. Read [USER_GUIDE.md](USER_GUIDE.md)
5. Explore features

### Q: Where's the documentation?
**A:** In `/docs` folder:
- [README.md](README.md) - Index
- [QUICKSTART.md](QUICKSTART.md) - Getting started
- [USER_GUIDE.md](USER_GUIDE.md) - Using app
- [FEATURES.md](FEATURES.md) - Feature list
- Many more...

### Q: Are there video tutorials?
**A:** Coming soon! Check:
- YouTube
- GitHub
- Project website

---

## 💡 Tips & Tricks

### Q: What's the best time period to use?
**A:** Depends on your analysis:
- **Short-term:** 1-3 months
- **Medium-term:** 6-12 months (recommended)
- **Long-term:** 5 years or max
- **Comparison:** Try multiple periods

### Q: Which stocks should I follow?
**A:**
- Use autocomplete to discover
- Start with popular ones (AAPL, MSFT)
- Try different sectors
- Create watchlist (coming soon)

### Q: How often should I check prices?
**A:** Depends on your strategy:
- Day traders: Continuously
- Swing traders: Daily
- Investors: Weekly/monthly
- Long-term: Quarterly/yearly

---

## 🚀 Future Questions

### Q: When is v0.2 coming?
**A:** See [ROADMAP.md](ROADMAP.md) for timeline

### Q: Will there be a mobile app?
**A:** Planned for v2.0+ (2027+)

### Q: Can I use this for trading?
**A:** For analysis only (not for actual trades):
- You need a brokerage account
- Use their trading platform
- Use ScrapeMatrix for research

### Q: Will it cost money?
**A:** No! Always free (MIT License)

---

## 📞 Still Have Questions?

### Where to Get Help
1. **This FAQ:** Read above
2. **Documentation:** Read `/docs`
3. **GitHub Issues:** Search & ask
4. **Troubleshooting:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
