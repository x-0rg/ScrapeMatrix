# 🚀 ScrapeMatrix v0.1.0 - Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Launch Application (30 seconds)
```bash
dist\ScrapeMatrix\ScrapeMatrix.exe
```
✅ Application window appears with 3 tabs (Home, Stock Viewer, RAG Chat)

### Step 2: Open Settings & Logs (10 seconds)
Click the **⚙️ Settings & Logs** button in the toolbar (top right)
✅ Settings dialog opens with 2 tabs

### Step 3: Explore Logs (2 minutes)
In the **📋 Logs** tab:
1. See real-time log messages
2. Notice color coding:
   - 🟢 Green = INFO
   - 🔴 Red = ERROR
   - 🟡 Orange = WARNING
   - 🔵 Gray = DEBUG
3. Try log filtering dropdown
4. Watch logs update as you interact

### Step 4: Explore Settings (1 minute)
In the **⚙️ Settings** tab:
1. Change theme (Light/Dark)
2. Adjust font size
3. Set log level
4. Enable file logging
5. Click Close

### Step 5: Try Features (1 minute)
1. Go to **📊 Stock Viewer** tab
2. Type ticker symbol (e.g., "AAPL")
3. Press Enter to search
4. Notice logs updating in real-time

✅ You've now experienced all new features!

---

## 🎯 Common Tasks

### View Application Logs
1. Click **⚙️ Settings & Logs** button
2. Switch to **📋 Logs** tab
3. Scroll through messages
4. Filter by level if needed

### Export Logs for Support
1. Open Settings & Logs dialog
2. Go to **📋 Logs** tab
3. Click **💾 Export Logs** button
4. Logs saved to timestamped file
5. Share file with support team

### Enable Persistent Logging
1. Open Settings & Logs dialog
2. Go to **⚙️ Settings** tab
3. Check **"Enable file logging"**
4. Close dialog
5. Logs now saved to `~/.scrapematrix/logs/`

### Change Log Verbosity
1. Open Settings & Logs dialog
2. Go to **⚙️ Settings** tab
3. Change **Log Level** dropdown
4. More verbose = more messages
5. Less verbose = only important messages

### Clear All Logs
1. Open Settings & Logs dialog
2. Click **🗑️ Clear Logs** button
3. All logs cleared
4. Logs will restart from this point

---

## 📚 Feature Overview

### Settings Dialog Components

#### 📋 Logs Tab
```
┌─────────────────────────────────┐
│ Real-time Log Display           │
│ • 1000 most recent logs         │
│ • Color-coded by level          │
│ • Auto-scroll to bottom         │
│                                 │
│ [Example log entries shown]     │
│                                 │
├─────────────────────────────────┤
│ Filter: [All ▼]                 │
│ ☑ Auto-scroll to bottom         │
│ [🗑️ Clear] [💾 Export] [✕ Close]│
└─────────────────────────────────┘
```

#### ⚙️ Settings Tab
```
📱 Application Settings
├─ Theme: [Light ▼]
└─ Font Size: [10 pt ▼]

📊 Data & Logging
├─ ☑ Enable automatic updates
├─ Log Level: [INFO ▼]
└─ ☐ Enable file logging

📈 Stock Viewer Settings
└─ Auto-refresh: [30 seconds ▼]
```

---

## 🔍 Understanding Logs

### Log Format
```
HH:MM:SS | LEVEL    | COMPONENT | MESSAGE
16:45:23 | INFO     | gui.main_window | 🚀 MainWindow initializing
```

### Log Levels Explained

| Level | Symbol | Color | Usage |
|-------|--------|-------|-------|
| DEBUG | 🐛 | Gray | Low-level debugging info |
| INFO | ℹ️ | Green | General info (most common) |
| WARNING | ⚠️ | Orange | Potential issues |
| ERROR | ❌ | Red | Errors (critical) |

### Common Log Messages

```
✅ "Tab loaded" = Feature initialized successfully
🔧 "Opening settings dialog" = User action
📊 "Stock lookup" = Data operation
⚠️ "Missing package" = Warning condition
❌ "Build failed" = Error occurred
```

---

## 🛠️ Troubleshooting

### Problem: Settings button not responding
**Solution:**
1. Wait 2-3 seconds
2. Try clicking again
3. Check logs for errors
4. Restart application

### Problem: No logs appearing
**Solution:**
1. Check log level (change from ERROR to INFO)
2. Interact with app (perform action)
3. Look for new logs
4. Verify logging enabled

### Problem: Export button doesn't work
**Solution:**
1. Check folder exists: `~/.scrapematrix/logs/`
2. Verify write permissions
3. Try clearing logs first
4. Ensure disk space available

### Problem: Application is slow
**Solution:**
1. Set log level to ERROR (reduces output)
2. Disable file logging
3. Clear logs (🗑️ button)
4. Restart application

---

## 💡 Tips & Tricks

### Tip 1: Use Log Filtering
When troubleshooting specific issues, filter logs to only show ERROR messages:
- Filter: ERROR
- Easier to spot problems
- Less noise to scan through

### Tip 2: Export Before Restart
If experiencing issues, export logs BEFORE restarting:
1. Click 💾 Export Logs
2. Logs saved with timestamp
3. Now restart application
4. Share exported file with support

### Tip 3: Monitor Real-time
For performance testing:
1. Open Settings & Logs
2. Set filter to DEBUG
3. Perform actions
4. Watch timestamp changes
5. Identify slow operations

### Tip 4: Save Custom Settings
Your settings are preserved:
1. Change theme to Dark
2. Set log level to DEBUG
3. Close dialog
4. Settings remembered on restart

### Tip 5: Regular Log Export
Set up routine (weekly):
1. Click 💾 Export Logs
2. Store in archive folder
3. Delete old logs with 🗑️ Clear
4. Keeps application running fast

---

## 📖 Next Steps

### For Users
- ✅ Done! You understand the new features
- Read [FEATURES_v0.1.0.md](docs/FEATURES_v0.1.0.md) for advanced usage
- Contact support if issues

### For Developers
- Build: `python packaging/build_executable.py --clean`
- Test: `python scrapematrix_launcher.py`
- Code: See [src/scrapematrix/gui/dialogs/settings_dialog.py](src/scrapematrix/gui/dialogs/settings_dialog.py)

### For Operators
- Review [UPGRADE_v0.1.0.md](docs/UPGRADE_v0.1.0.md)
- Plan deployment
- Test in staging first

---

## 🎓 Learning Path

| Level | Topic | Time | Resource |
|-------|-------|------|----------|
| Beginner | First run | 5 min | This guide |
| Beginner | Using settings | 5 min | Settings dialog |
| Beginner | Viewing logs | 5 min | Logs tab |
| Intermediate | Troubleshooting | 10 min | [FEATURES_v0.1.0.md](docs/FEATURES_v0.1.0.md) |
| Intermediate | Building executable | 15 min | [UPGRADE_v0.1.0.md](docs/UPGRADE_v0.1.0.md) |
| Advanced | Modifying code | 30 min | [RAG_SYSTEM.md](docs/RAG_SYSTEM.md) |
| Advanced | Custom deployment | 1 hr | [DEPLOYMENT.md](docs/DEPLOYMENT.md) |

---

## ❓ Quick FAQ

**Q: Where are my logs stored?**  
A: Displayed in app (live), or in `~/.scrapematrix/logs/` if file logging enabled

**Q: How many logs kept in memory?**  
A: Last 1000 logs automatically managed

**Q: Can I change log colors?**  
A: Yes, edit [settings_dialog.py](src/scrapematrix/gui/dialogs/settings_dialog.py)

**Q: Will logs persist between restarts?**  
A: Only if file logging enabled (check Settings tab)

**Q: How do I share logs with support?**  
A: Click 💾 Export Logs, send exported file

---

## 🎯 What You've Learned

✅ Launch the application  
✅ Access Settings & Logs dialog  
✅ View real-time logs  
✅ Filter logs by level  
✅ Configure application settings  
✅ Export logs for support  
✅ Enable file logging  
✅ Understand log messages  

---

**Version**: v0.1.0  
**Status**: Ready to Use ✅  
**Support**: [FEATURES_v0.1.0.md](docs/FEATURES_v0.1.0.md)
