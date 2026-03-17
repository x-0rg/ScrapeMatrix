# 📦 Building Standalone Executables

Complete guide to creating `.exe` files (Windows), `.app` files (macOS), and executables (Linux) for ScrapeMatrix.

## 🎯 Overview

ScrapeMatrix can be packaged into **standalone executables** that run without requiring Python installation. This guide covers the complete process.

### What You Get

After building:
- ✅ Single executable file (`.exe` on Windows)
- ✅ All dependencies bundled
- ✅ No Python installation required for users
- ✅ Professional distribution package

---

## 📋 Quick Start (Windows)

### Fastest Way (3 steps)

1. **Open PowerShell in project folder**
   ```powershell
   cd D:\projects\ScrapeMatrix
   ```

2. **Run build script**
   ```powershell
   .\packaging\build_windows.ps1
   ```

3. **Run the executable**
   ```powershell
   .\dist\ScrapeMatrix\ScrapeMatrix.exe
   ```

**Time required:** 5-10 minutes (depending on system)

---

## ⚙️ Prerequisites

### Required

1. **Python 3.8 or higher**
   - Check: `python --version`
   - Download: https://www.python.org

2. **PyInstaller**
   ```bash
   pip install PyInstaller
   ```

3. **All ScrapeMatrix dependencies**
   ```bash
   pip install -e .
   ```

### Verify Setup

```powershell
# Test all requirements
python --version                          # Should be 3.8+
python -m pip --version                   # Verify pip
python -c "import PyInstaller; print('✓ PyInstaller')"
python -c "import PyQt6; print('✓ PyQt6')"
python -c "import pandas; print('✓ pandas')"
python -c "import matplotlib; print('✓ matplotlib')"
python -c "import yfinance; print('✓ yfinance')"
```

---

## 🔨 Build Methods

### Method 1: PowerShell (Windows) - Recommended

```powershell
cd D:\projects\ScrapeMatrix
.\packaging\build_windows.ps1 -Clean
```

**Options:**
```powershell
.\packaging\build_windows.ps1              # Standard build
.\packaging\build_windows.ps1 -Clean       # Clean first
.\packaging\build_windows.ps1 -Debug       # With debug info
```

### Method 2: Batch (Windows)

```batch
cd D:\projects\ScrapeMatrix
packaging\build_windows.bat
```

### Method 3: Python (All Platforms)

**Windows:**
```bash
python packaging/build_executable.py --clean
```

**macOS:**
```bash
python packaging/build_executable.py --platform macos --clean
```

**Linux:**
```bash
python packaging/build_executable.py --platform linux --clean
```

---

## 📍 Output Location

After successful build, executable is at:

**Windows:**
```
dist/ScrapeMatrix/ScrapeMatrix.exe
```

**macOS:**
```
dist/ScrapeMatrix/ScrapeMatrix
```

**Linux:**
```
dist/ScrapeMatrix/ScrapeMatrix
```

---

## 🚀 Running the Executable

### Windows

**Option 1: Double-click**
- Go to `dist/ScrapeMatrix/`
- Double-click `ScrapeMatrix.exe`

**Option 2: Command line**
```cmd
dist\ScrapeMatrix\ScrapeMatrix.exe
```

**Option 3: PowerShell**
```powershell
& .\dist\ScrapeMatrix\ScrapeMatrix.exe
```

### macOS

```bash
./dist/ScrapeMatrix/ScrapeMatrix
```

### Linux

```bash
chmod +x dist/ScrapeMatrix/ScrapeMatrix
./dist/ScrapeMatrix/ScrapeMatrix
```

---

## 📦 Distribution

### For Users (Portable)

1. **Zip the folder**
   ```powershell
   # Windows PowerShell
   Compress-Archive -Path .\dist\ScrapeMatrix -DestinationPath ScrapeMatrix-0.1.0-windows.zip
   ```

2. **Share the ZIP file**
   - Users download ZIP
   - Extract anywhere
   - Run directly (no installation)

### Folder Structure Shared with Users

```
ScrapeMatrix-0.1.0-windows.zip
└── ScrapeMatrix/
    ├── ScrapeMatrix.exe          ← Run this
    ├── _internal/                ← All dependencies
    ├── README.txt                ← Instructions
    └── base_library.zip
```

---

## 🔧 Build Configuration

### Customizing Build

Edit `packaging/pyinstaller.spec`:

**1. Change executable name:**
```python
name='MyApp'
```

**2. Add custom icon:**
```python
icon='packaging/scrapematrix.ico'
```

**3. Change console behavior:**
```python
console=False  # No console window
# or
console=True   # Show console
```

**4. Add hidden imports:**
```python
hiddenimports=['module1', 'module2']
```

### Rebuild after Changes

```bash
python packaging/build_executable.py --clean
```

---

## ⚠️ Troubleshooting

### Build Fails: "Python not found"

```
Error: Python not recognized
```

**Fix:**
1. Install Python from https://www.python.org
2. During install, check "Add Python to PATH"
3. Restart terminal

### Build Fails: "PyInstaller not found"

```
Error: No module named PyInstaller
```

**Fix:**
```bash
pip install PyInstaller
```

### Build Fails: "Module not found"

```
Error: ModuleNotFoundError: No module named 'PyQt6'
```

**Fix:**
```bash
pip install -e .
pip install PyQt6 pandas matplotlib yfinance
```

### Executable Won't Start

1. **Check system compatibility:**
   - Windows 7 or newer
   - 2GB RAM minimum
   - Modern graphics driver

2. **Run from command line:**
   ```cmd
   dist\ScrapeMatrix\ScrapeMatrix.exe
   # See error messages
   ```

3. **Update graphics drivers:**
   - NVIDIA/AMD/Intel website
   - Windows Update

### "Graphics/Display Error"

**Causes:** PyQt6/OpenGL issues

**Solutions:**
1. Update graphics drivers
2. Try Windows compatibility mode
3. Check DPI settings

### Build Takes Forever

**Normal:** First build takes 10-15 minutes (large dependencies)

**Speed up:**
- Use SSD (faster I/O)
- Close other applications
- Incremental builds: `python packaging/build_executable.py` (no --clean)

---

## 📊 Build Details

### What Gets Included

The executable includes:
- ✅ Python runtime
- ✅ PyQt6 framework
- ✅ Matplotlib library
- ✅ Pandas library
- ✅ yfinance API
- ✅ All other dependencies

### File Sizes

| Component | Size |
|-----------|------|
| Python runtime | ~20 MB |
| PyQt6 | ~200 MB |
| Matplotlib | ~100 MB |
| Pandas | ~50 MB |
| Other libraries | ~80 MB |
| **Total** | **~500 MB** |

### Why So Large?

- Python runtime (needed)
- PyQt6 is large (Qt framework)
- Matplotlib visualization
- Complete dependency tree

**Size cannot be significantly reduced** - this is typical for PyInstaller builds

---

## 🎓 Advanced Usage

### Command-Line Options

```bash
python packaging/build_executable.py --help
```

**Options:**
```
--platform PLATFORM    windows, macos, or linux
--clean               Clean before building
--debug               Include debug info
```

### Clean Build vs Incremental

```bash
# Full clean build (slowest)
python packaging/build_executable.py --clean

# Incremental build (faster)
python packaging/build_executable.py
```

### Creating an Icon

1. **Prepare 256x256 PNG image**

2. **Convert to ICO:**
   ```bash
   pip install Pillow
   python -c "from PIL import Image; Image.open('icon.png').save('packaging/scrapematrix.ico')"
   ```

3. **Rebuild:**
   ```bash
   python packaging/build_executable.py --clean
   ```

---

## 📋 Pre-Build Checklist

Before distributing, verify:

- [ ] Build completes without errors
- [ ] Executable runs on target OS
- [ ] All features working correctly
- [ ] No console errors
- [ ] Stock lookup works
- [ ] Charts display correctly
- [ ] Data tables show data
- [ ] Autocomplete working

---

## 🔄 Rebuild Steps

When updating the application:

1. **Make code changes**
   ```bash
   # Edit source files
   # Test with: python -m scrapematrix
   ```

2. **Update version** (optional)
   ```toml
   # pyproject.toml
   version = "0.2.0"
   ```

3. **Clean and rebuild**
   ```bash
   python packaging/build_executable.py --clean
   ```

4. **Test executable**
   ```bash
   ./dist/ScrapeMatrix/ScrapeMatrix.exe
   ```

5. **Re-distribute**
   - Zip new dist/ScrapeMatrix folder
   - Share with users

---

## 📚 Related Documentation

- **PACKAGING.md** - Technical details
- **Installation.md** - User installation guide
- **QUICKSTART.md** - Getting started
- **TROUBLESHOOTING.md** - Problem solutions

---

## 🔗 Resources

### Tools Used

- **PyInstaller:** https://pyinstaller.org/
- **PyQt6:** https://www.riverbankcomputing.com/software/pyqt/
- **Python:** https://www.python.org/

### Alternatives

- **cx_Freeze** - More complex, smaller size
- **py2exe** - Windows only
- **Nuitka** - Compiles to C++, very fast

---

## ✅ Success Indicators

Your build is successful when you see:

```
✅ BUILD SUCCESSFUL!
────────────────────────────────────────────

📦 Executable location:
  dist/ScrapeMatrix/ScrapeMatrix.exe

🚀 To run the application:
  1. Navigate to: dist/ScrapeMatrix
  2. Double-click: ScrapeMatrix.exe

📋 Distribution:
  Zip the entire 'ScrapeMatrix' folder in dist/
  Users can extract and run directly

💾 Size: ~500MB (includes all dependencies)
```

---

## 🆘 Getting Help

If you encounter issues:

1. **Check TROUBLESHOOTING.md** - Common problems
2. **Check PACKAGING.md** - Detailed technical guide
3. **Check console output** - Run from command line
4. **GitHub Issues** - Search for similar problems
5. **PyInstaller Docs** - https://pyinstaller.org/

---

## 🎉 Next Steps

1. ✅ **Install prerequisites** (Python, PyInstaller)
2. ✅ **Run build script** (build_windows.ps1 or build_executable.py)
3. ✅ **Test executable** (run dist/ScrapeMatrix/ScrapeMatrix.exe)
4. ✅ **Zip for distribution** (share with users)

You now have a standalone executable! 🚀

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
