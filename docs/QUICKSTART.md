# ⚡ Quick Start Guide

Get ScrapeMatrix up and running in 5 minutes!

## Prerequisites

- **Python:** 3.8 or higher
- **Git:** For cloning the repository
- **Virtual Environment:** Recommended (venv, conda, etc.)

## 🚀 Installation (5 minutes)

### 1. Clone the Repository
```bash
git clone https://github.com/x-0rg/ScrapeMatrix.git
cd ScrapeMatrix
```

### 2. Create Virtual Environment
```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -e .
```

## ▶️ Running the Application

### Option 1: Python Module (Recommended)
```bash
python -m scrapematrix
```

### Option 2: PowerShell Script (Windows)
```powershell
.\run.ps1
```

### Option 3: Direct Python
```bash
python src/scrapematrix/__main__.py
```

## 🎯 First Steps

Once the application is running:

1. **Explore Home Tab**
   - Overview of available features
   - Introduction to the interface

2. **Try Stock Viewer**
   - Click the "📊 Stock Viewer" tab
   - Select an exchange from the dropdown
   - Enter a ticker symbol (e.g., AAPL, GOOGL, MSFT)
   - Click "Fetch Data" to load stock information
   - View the interactive chart and company info

3. **Test Ticker Autocomplete**
   - Start typing in the ticker input field
   - See suggestions appear automatically
   - Click a suggestion to select it

## 📊 Example Workflows

### Get Apple Stock Data (NASDAQ)
1. Select **NASDAQ - United States** from exchange dropdown
2. Type: **AAPL**
3. Select period: **1y** (one year)
4. Click **Fetch Data**
5. View chart and company information

### Search Multiple Exchanges
1. Select **🌍 All Global Exchanges**
2. Type any ticker from any exchange
3. Examples: AAPL (USA), 0700 (Hong Kong), SAP (Germany)
4. Fetch and compare data

## 🔧 Troubleshooting Quick Fixes

### "Module not found" error
```bash
# Reinstall the package
pip install -e .
```

### Application won't start
```bash
# Check Python version
python --version  # Should be 3.8+

# Check dependencies
pip install PyQt6>=6.6.1 matplotlib>=3.7.0 pandas>=1.5.0 yfinance>=0.2.32
```

### Rate limit errors from Yahoo Finance
- Wait a few moments before making another request
- Avoid making many rapid requests

### Display issues
- Ensure your graphics drivers are updated
- Try running with: `python -m scrapematrix`

## 📚 Next Steps

- **Learn More:** Read [USER_GUIDE.md](USER_GUIDE.md)
- **Understand the Code:** Read [ARCHITECTURE.md](ARCHITECTURE.md)
- **Contribute:** Read [CONTRIBUTING.md](CONTRIBUTING.md)
- **Troubleshoot:** Read [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 🆘 Need Help?

1. **Check FAQ:** [FAQ.md](FAQ.md)
2. **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
3. **Full Installation Guide:** [INSTALLATION.md](INSTALLATION.md)
4. **GitHub Issues:** https://github.com/x-0rg/ScrapeMatrix/issues
5. **Jira Board:** https://x-0rg.atlassian.net/jira/software/projects/SCRAMX/boards/1

---

**Time to First Run:** ~5 minutes  
**Difficulty:** ⭐ Beginner  
**Last Updated:** 2026-03-16
