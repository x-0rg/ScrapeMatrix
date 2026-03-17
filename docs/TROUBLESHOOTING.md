# 🔧 Troubleshooting Guide

Solutions to common issues and problems.

## 🚀 Installation Problems

### Issue: "Python is not recognized"
**Symptoms:** `'python' is not recognized as an internal or external command`

**Solutions:**
1. **Install Python:** Download from https://www.python.org
2. **Add to PATH:**
   - Windows: Reinstall Python, check "Add Python to PATH"
   - macOS/Linux: Use python3 instead
3. **Verify:** `python --version`

---

### Issue: Virtual Environment Won't Activate
**Symptoms:** Activation script doesn't work

**Check your OS:**
- **Windows PowerShell:** `.venv\Scripts\Activate.ps1`
- **Windows CMD:** `.venv\Scripts\activate.bat`
- **macOS/Linux:** `source .venv/bin/activate`

**If still failing:**
```bash
# Try recreating venv
rm -rf .venv
python -m venv .venv
source .venv/bin/activate  # or appropriate command
```

---

### Issue: "Module not found" After Installation
**Symptoms:** `ModuleNotFoundError: No module named 'scrapematrix'`

**Solutions:**
1. **Activate virtual environment first**
   ```bash
   source .venv/bin/activate  # Check activation worked
   ```

2. **Reinstall the package**
   ```bash
   pip install -e . --force-reinstall
   ```

3. **Clear cache and try again**
   ```bash
   pip cache purge
   pip install -e .
   ```

---

### Issue: PyQt6 Installation Fails
**Symptoms:** `ERROR: Could not build wheels for PyQt6`

**Solutions:**
1. **Update pip:**
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

2. **Try conda (easier for PyQt6):**
   ```bash
   conda install -c conda-forge pyqt6
   ```

3. **On macOS**, may need Xcode:
   ```bash
   xcode-select --install
   ```

---

## 🎯 Running the Application

### Issue: Application Won't Start
**Symptoms:** Application closes immediately or shows no window

**Solutions:**

1. **Check Python version:**
   ```bash
   python --version  # Should be 3.8+
   ```

2. **Check dependencies:**
   ```bash
   python -c "import PyQt6; print('PyQt6 OK')"
   python -c "import pandas; print('Pandas OK')"
   python -c "import yfinance; print('yfinance OK')"
   ```

3. **Run with error output:**
   ```bash
   python -m scrapematrix  # Shows full error
   ```

4. **Check graphics drivers:**
   - Windows: Update drivers
   - macOS: Update OS
   - Linux: Update graphics drivers

---

### Issue: "Display backend not found"
**Symptoms:** `ERROR: Requested backend not available` or similar display error

**Solutions:**
```bash
# Try different backend (Linux)
export QT_QPA_PLATFORM=xcb
python -m scrapematrix

# Or with offscreen
export QT_QPA_PLATFORM=offscreen
python -m scrapematrix
```

---

### Issue: Application Starts But Shows Blank Window
**Symptoms:** Window appears but is empty

**Solutions:**
1. **Resize window:**
   - Drag window edges to larger size
   - Application may need minimum size

2. **Check graphics:**
   - Update graphics drivers
   - Try different display settings

3. **Restart application:**
   - Close completely
   - Run again

---

## 📊 Using the Application

### Issue: "Symbol not found"
**Symptoms:** Error when trying to fetch stock data

**Causes & Solutions:**
1. **Wrong ticker:**
   - Use autocomplete to verify
   - Check exchange's website

2. **Delisted stock:**
   - Company no longer publicly traded
   - Try different stock

3. **Spelling error:**
   - Verify spelling carefully
   - Use autocomplete

4. **Data not available:**
   - Try different time period
   - Check if publicly traded

---

### Issue: "Rate Limited" or Request Timeout
**Symptoms:** Error about too many requests

**Causes:** Yahoo Finance rate limiting

**Solutions:**
1. **Wait 30-60 seconds**
2. **Try different ticker**
3. **Reduce frequency of requests**
4. **Try again in a few minutes**

**To prevent:**
- Don't fetch too frequently
- Space out requests
- Avoid batch operations

---

### Issue: No Autocomplete Suggestions
**Symptoms:** Typing doesn't show any suggestions

**Solutions:**
1. **Type more characters:**
   - Single letters might not match
   - Type 2-3 characters

2. **Check spelling:**
   - Must match existing tickers
   - Case-insensitive but careful with spelling

3. **Ticker might not exist:**
   - Use full ticker if you know it
   - Check exchange's website

---

### Issue: Chart Not Displaying
**Symptoms:** Chart tab is blank

**Causes & Solutions:**
1. **Haven't fetched data:**
   - Click "Fetch Data" button
   - Wait for completion

2. **Data fetch failed:**
   - Check error messages
   - Try different stock

3. **Graphics issue:**
   - Update graphics drivers
   - Restart application

---

### Issue: Data Shows Gaps
**Symptoms:** Missing data points in chart or table

**Causes:**
- Weekends (markets closed)
- Holidays
- Trading halts
- Company delisted
- Data not available from Yahoo

**This is normal - not an error**

---

## 🔗 Network Issues

### Issue: "Connection Error" or "Network Unreachable"
**Symptoms:** Can't fetch data, error about network

**Causes & Solutions:**
1. **Check internet connection:**
   ```bash
   ping google.com  # Test connectivity
   ```

2. **Check firewall:**
   - Whitelist application
   - Disable firewall temporarily to test

3. **Check proxy:**
   - If behind corporate proxy, may need configuration
   - Contact IT department

4. **Yahoo Finance is down:**
   - Check status: https://status.finance.yahoo.com
   - Try again later

---

### Issue: Very Slow Data Loading
**Symptoms:** Takes minutes to fetch data

**Causes & Solutions:**
1. **Slow internet:**
   - Check connection speed
   - Close other downloads

2. **Large time period:**
   - Using "max" period requests lots of data
   - Try shorter period (1y instead)

3. **Computer busy:**
   - Close unnecessary applications
   - Check CPU/disk usage

4. **Yahoo Finance is slow:**
   - Try again in a moment
   - Usually resolves itself

---

## 🎨 Display Problems

### Issue: Text Too Small (High DPI Screens)
**Symptoms:** Text is hard to read on 4K monitors

**Solutions (Coming Soon):**
- Font size adjustment
- DPI scaling settings
- High DPI support being added

**Workaround:**
- Use Windows scaling (150-200%)
- Will be fixed in v0.2

---

### Issue: Dark Mode/Light Mode Not Working
**Symptoms:** Application uses wrong theme

**Status:** Dark mode coming in v0.3

**Workaround:** Use system theme
- Windows: Settings → Personalization
- macOS: System Preferences → General
- Linux: GNOME/KDE settings

---

### Issue: Window Layout Broken
**Symptoms:** Buttons/fields not visible or arranged incorrectly

**Solutions:**
1. **Resize window:**
   - Drag edges to larger size

2. **Reset layout:**
   - Delete config files (if they exist)
   - Restart application

3. **Check resolution:**
   - Minimum 1366x768 recommended
   - Smaller resolutions may not work

---

## 💾 Data Problems

### Issue: Data Doesn't Match Other Sources
**Symptoms:** Prices differ from other websites

**Reasons:**
1. **Time differences:** Different timezones
2. **Adjusted prices:** Dividends, splits adjustments
3. **Source differences:** Various data providers differ slightly
4. **Timing:** Prices update throughout day

**This is normal** - slight variations are expected

---

### Issue: Can't Export Data
**Symptoms:** No export button visible

**Status:** Coming in v0.2

**Workaround:**
1. Click on table
2. Select all (Ctrl+A)
3. Copy (Ctrl+C)
4. Paste to Excel/text editor

---

## 🐛 Crashes & Errors

### Issue: Application Crashes Unexpectedly
**Symptoms:** App closes without warning

**To report:**
1. Note what you were doing
2. Check error in console
3. Report on GitHub with:
   - Error message
   - Steps to reproduce
   - System info (OS, Python version)

**To debug:**
```bash
# Run with verbose output
python -m scrapematrix  2>&1 | tee error.log
```

---

### Issue: UI Freezes
**Symptoms:** Application becomes unresponsive

**Note:** Shouldn't happen with proper threading

**If it does:**
1. Wait (may be processing)
2. Close window if unresponsive
3. Report issue with details

**To prevent:**
- Don't click multiple times rapidly
- Let operations complete
- Check status bar for progress

---

## 🔍 Debugging Tips

### Enable Verbose Logging
```bash
# Set logging level
python -m scrapematrix --verbose
```

### Check Application Logs
```bash
# View logs (if saved)
cat ~/.scrapematrix/logs.txt  # macOS/Linux
type %APPDATA%\.scrapematrix\logs.txt  # Windows
```

### Run in Debug Mode
```python
# In python interactive mode
from scrapematrix.data.loaders import StockDataLoader
data = StockDataLoader.fetch_stock_data("AAPL", "1y")
print(data)  # Check what's returned
```

---

## 📞 Getting Help

### Still Having Issues?

1. **Check Documentation:**
   - [FAQ.md](FAQ.md)
   - [USER_GUIDE.md](USER_GUIDE.md)
   - [README.md](README.md)

2. **Search Known Issues:**
   - GitHub Issues: https://github.com/x-0rg/ScrapeMatrix/issues

3. **Create an Issue:**
   - Include: Error message, steps, system info
   - Attach: Screenshots if helpful
   - Be detailed as possible

4. **Check Status:**
   - Yahoo Finance status: https://status.finance.yahoo.com

---

## 🎯 Common Solutions Checklist

### Before Reporting a Bug:
- [ ] Read this guide
- [ ] Check FAQ
- [ ] Update Python & dependencies
- [ ] Restart application
- [ ] Check internet connection
- [ ] Verify ticker symbol spelling
- [ ] Try different stock
- [ ] Restart computer
- [ ] Reinstall application

### When Reporting:
- [ ] Include full error message
- [ ] Include steps to reproduce
- [ ] Include system information
- [ ] Check existing issues first
- [ ] Be detailed and specific

---

## 📚 Resources

- **Main Documentation:** [README.md](README.md)
- **FAQ:** [FAQ.md](FAQ.md)
- **User Guide:** [USER_GUIDE.md](USER_GUIDE.md)
- **Installation:** [INSTALLATION.md](INSTALLATION.md)
- **Issues:** https://github.com/x-0rg/ScrapeMatrix/issues

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
