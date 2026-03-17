# 📦 ScrapeMatrix Packaging

Build standalone executables for Windows, macOS, and Linux.

## 📂 Files in This Folder

| File | Purpose |
|------|---------|
| **pyinstaller.spec** | PyInstaller configuration |
| **build_executable.py** | Main build script (Python) |
| **build_windows.bat** | Windows batch build script |
| **build_windows.ps1** | Windows PowerShell build script |
| **PACKAGING.md** | Detailed technical guide |
| **scrapematrix.ico** | Application icon (optional) |

---

## 🚀 Quick Start

### Windows (PowerShell)
```powershell
.\build_windows.ps1 -Clean
```

### Windows (Batch)
```batch
build_windows.bat
```

### All Platforms (Python)
```bash
python build_executable.py --clean
```

---

## 📍 Output

Executable is created in: `../dist/ScrapeMatrix/`

- **Windows:** `ScrapeMatrix.exe`
- **macOS:** `ScrapeMatrix`
- **Linux:** `ScrapeMatrix`

---

## 📚 Documentation

- **[PACKAGING.md](PACKAGING.md)** - Detailed technical guide
- **[../docs/DEPLOYMENT.md](../docs/DEPLOYMENT.md)** - User-friendly guide
- **[../docs/TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md)** - Problem solving

---

## ✅ Prerequisites

- Python 3.8+
- PyInstaller: `pip install PyInstaller`
- Dependencies: `pip install -e ..`

---

## 🔨 Build Options

```bash
# Clean build
python build_executable.py --clean

# With debug info
python build_executable.py --debug

# Incremental build (faster)
python build_executable.py

# Specific platform
python build_executable.py --platform windows
python build_executable.py --platform macos
python build_executable.py --platform linux
```

---

## 🎓 How It Works

1. **PyInstaller scans** your code for imports
2. **Bundles everything:**
   - Python runtime
   - PyQt6 framework
   - All dependencies
   - Application code
3. **Creates executable:**
   - Single .exe (Windows)
   - Single binary (macOS/Linux)
   - With bundled dependencies

---

## 📊 Build Output

```
dist/ScrapeMatrix/
├── ScrapeMatrix.exe          ← Executable
├── _internal/                ← Dependencies
├── base_library.zip
└── README.txt                ← User instructions
```

**Size:** ~500MB (includes all dependencies)

---

## 🆘 Troubleshooting

### Build fails
- Check Python version: `python --version` (need 3.8+)
- Install PyInstaller: `pip install PyInstaller`
- Install dependencies: `pip install -e ..`

### Executable won't start
- Run from command line to see errors
- Update graphics drivers
- Check Windows compatibility settings

### More help
- See [PACKAGING.md](PACKAGING.md) for detailed guide
- See [../docs/TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md)

---

## 📝 Files Explained

### pyinstaller.spec
PyInstaller configuration file that specifies:
- Entry point: `src/scrapematrix/__main__.py`
- Hidden imports (PyQt6, matplotlib, pandas, yfinance)
- Executable settings
- Output configuration

### build_executable.py
Main Python build script that:
- Checks dependencies
- Runs PyInstaller
- Creates output README
- Shows build summary

### build_windows.ps1
PowerShell convenience script that:
- Checks Python and PyInstaller
- Runs build_executable.py
- Shows success/error messages
- Works with Windows natively

### build_windows.bat
Batch file convenience script that:
- Checks Python installation
- Installs missing PyInstaller
- Calls build_executable.py
- Pauses to show results

---

## 🎯 Distribution

### For Users
1. Zip `dist/ScrapeMatrix` folder
2. Share the ZIP file
3. Users extract and run `ScrapeMatrix.exe`

### No installation needed!
Users don't need Python or any other software installed.

---

## 🔄 Workflow

```
1. Edit code
   ↓
2. Test: python -m scrapematrix
   ↓
3. Build: python build_executable.py --clean
   ↓
4. Test: dist/ScrapeMatrix/ScrapeMatrix.exe
   ↓
5. Zip dist/ScrapeMatrix
   ↓
6. Share with users
```

---

## 💡 Tips

- First build takes 10-15 minutes (large dependencies)
- Incremental builds faster (use without --clean)
- Keep _internal folder intact (dependencies)
- Don't move individual files from ScrapeMatrix folder
- Size ~500MB is normal (includes Python + Qt + pandas)

---

## 🎓 Learn More

- **PyInstaller Documentation:** https://pyinstaller.org/
- **Spec Files:** https://pyinstaller.org/en/stable/spec-files.html
- **ScrapeMatrix Docs:** ../docs/

---

## 📞 Support

- Check [PACKAGING.md](PACKAGING.md) for detailed guide
- See [../docs/TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md) for help
- Create GitHub issue if needed

---

**Last Updated:** 2026-03-16  
**Status:** ✅ Ready to use
