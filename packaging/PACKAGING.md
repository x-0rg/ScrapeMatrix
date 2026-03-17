# 📦 Packaging Guide - Creating Executables

Complete guide to building standalone executables for ScrapeMatrix.

## Overview

ScrapeMatrix can be packaged into standalone executables for Windows, macOS, and Linux using PyInstaller. This allows users to run the application without installing Python.

---

## Quick Start (5 minutes)

### Windows

**Option 1: Batch Script (Easiest)**
```batch
cd D:\projects\ScrapeMatrix
packaging\build_windows.bat
```

**Option 2: PowerShell**
```powershell
cd D:\projects\ScrapeMatrix
.\packaging\build_windows.ps1
```

**Option 3: Python**
```bash
cd D:\projects\ScrapeMatrix
python packaging/build_executable.py
```

### macOS/Linux

```bash
cd ~/projects/ScrapeMatrix
python packaging/build_executable.py --platform macos
# or
python packaging/build_executable.py --platform linux
```

---

## Prerequisites

### Required Software

1. **Python 3.8+**
   - Download from https://www.python.org
   - Verify: `python --version`

2. **PyInstaller**
   ```bash
   pip install PyInstaller
   ```

3. **All Dependencies**
   ```bash
   pip install -e .
   ```
   Or:
   ```bash
   pip install PyQt6 pandas matplotlib yfinance
   ```

### Verify Installation

```bash
python -c "import PyInstaller; print(PyInstaller.__version__)"
```

Should output: `PyInstaller 5.x.x` or higher

---

## Build Process

### Step-by-Step

#### 1. Prepare Environment

```bash
cd D:\projects\ScrapeMatrix

# Create/activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -e .
pip install PyInstaller
```

#### 2. Build Executable

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

#### 3. Locate Output

Build output is in: `dist/ScrapeMatrix/`

- **Windows:** `dist/ScrapeMatrix/ScrapeMatrix.exe`
- **macOS:** `dist/ScrapeMatrix/ScrapeMatrix`
- **Linux:** `dist/ScrapeMatrix/ScrapeMatrix`

---

## Build Options

### Command-Line Arguments

```
--platform PLATFORM    Target platform: windows, macos, or linux
--clean               Clean previous builds before building
--debug               Include debug information in executable
```

### Examples

**Clean build for Windows:**
```bash
python packaging/build_executable.py --platform windows --clean
```

**Incremental build with debug:**
```bash
python packaging/build_executable.py --debug
```

**Detect platform automatically:**
```bash
python packaging/build_executable.py --clean
```

---

## File Structure

```
packaging/
├── pyinstaller.spec           # PyInstaller configuration
├── build_executable.py        # Main build script
├── build_windows.bat          # Windows batch build script
├── build_windows.ps1          # Windows PowerShell build script
├── PACKAGING.md               # This file
├── scrapematrix.ico           # Application icon (optional)
└── README.md                  # Output README template
```

---

## Output Structure

After successful build:

```
dist/ScrapeMatrix/
├── ScrapeMatrix.exe              # Main executable
├── ScrapeMatrix                  # Executable (macOS/Linux)
├── _internal/                    # Dependencies and libraries
│   ├── PyQt6/                   # PyQt6 framework
│   ├── matplotlib/              # Matplotlib library
│   ├── pandas/                  # Pandas library
│   ├── yfinance/                # Yahoo Finance API
│   └── ... (other libraries)
├── README.txt                    # Instructions for users
└── base_library.zip            # Bundled Python libraries
```

**Total Size:** ~500MB (includes all dependencies)

---

## Distribution

### Portable Distribution (Recommended)

1. **Zip the folder:**
   ```bash
   # Windows (PowerShell)
   Compress-Archive -Path dist\ScrapeMatrix -DestinationPath ScrapeMatrix-0.1.0-windows.zip
   
   # macOS/Linux
   zip -r ScrapeMatrix-0.1.0-macos.zip dist/ScrapeMatrix
   ```

2. **Share the ZIP file:**
   - Users can extract anywhere
   - No installation needed
   - Run directly: `ScrapeMatrix.exe`

### Windows Installer (Optional)

For more professional distribution, create an installer using NSIS:

1. **Install NSIS:**
   - Download from https://nsis.sourceforge.io/
   
2. **Create installer script:**
   - See `scrapematrix_installer.nsi` (create separately)
   
3. **Build installer:**
   ```bash
   "C:\Program Files (x86)\NSIS\makensis.exe" scrapematrix_installer.nsi
   ```

---

## Running the Executable

### Windows

**Double-click:**
- Navigate to `dist/ScrapeMatrix/`
- Double-click `ScrapeMatrix.exe`

**Command line:**
```cmd
dist\ScrapeMatrix\ScrapeMatrix.exe
```

**PowerShell:**
```powershell
& .\dist\ScrapeMatrix\ScrapeMatrix.exe
```

### macOS

**Finder:**
- Navigate to `dist/ScrapeMatrix/`
- Double-click `ScrapeMatrix`

**Terminal:**
```bash
./dist/ScrapeMatrix/ScrapeMatrix
```

### Linux

**Terminal:**
```bash
./dist/ScrapeMatrix/ScrapeMatrix
```

**Or make executable:**
```bash
chmod +x dist/ScrapeMatrix/ScrapeMatrix
./dist/ScrapeMatrix/ScrapeMatrix
```

---

## Troubleshooting

### Build Fails: "Module not found"

**Cause:** Missing dependencies

**Solution:**
```bash
pip install PyInstaller PyQt6 pandas matplotlib yfinance
python packaging/build_executable.py --clean
```

### Executable Won't Start

**Windows:**
1. Open Command Prompt
2. Run: `dist\ScrapeMatrix\ScrapeMatrix.exe`
3. Check for error messages

**macOS/Linux:**
```bash
./dist/ScrapeMatrix/ScrapeMatrix
# Check for error output
```

### Graphics/Display Issues

**Cause:** PyQt6 graphics backend issues

**Solution:**
- Update graphics drivers
- Set Windows compatibility mode (Windows 7, Windows 10)
- Try different display DPI settings

### File Not Found Errors

**Cause:** Incomplete or moved files

**Solution:**
- Do not move individual files from `dist/ScrapeMatrix/`
- Keep entire folder structure intact
- Re-zip and distribute entire folder

### "The application failed to initialize properly"

**Cause:** Missing Visual C++ redistributables (Windows)

**Solution:**
```bash
# Install Visual C++ Redistributables
# Download from: https://support.microsoft.com/en-us/help/2977003
```

### Build Takes Too Long

**Cause:** Large dependencies (matplotlib, pandas)

**Solution:**
- First build takes longest
- Subsequent builds faster with `--no-clean`
- Use SSD for faster I/O

---

## Advanced Configuration

### Customizing Build (pyinstaller.spec)

Edit `packaging/pyinstaller.spec` to:

1. **Hide console window:**
   ```python
   console=False  # Already set
   ```

2. **Add custom icon:**
   ```python
   icon='packaging/scrapematrix.ico'
   ```

3. **Change executable name:**
   ```python
   name='MyApp'
   ```

4. **Add hidden imports:**
   ```python
   hiddenimports=['module1', 'module2']
   ```

5. **Exclude modules:**
   ```python
   excludedimports=['unwanted_module']
   ```

### Creating an Icon

1. **Prepare image** (256x256 PNG)
2. **Convert to ICO:**
   ```bash
   pip install Pillow
   python -c "from PIL import Image; Image.open('icon.png').save('scrapematrix.ico')"
   ```
3. **Place in packaging/scrapematrix.ico**
4. **Rebuild:** `python packaging/build_executable.py`

---

## Performance Optimization

### Reduce Executable Size

1. **Use UPX (Ultimate Packer):**
   ```bash
   pip install upx
   # UPX is automatically used if available
   ```

2. **Remove debug symbols:**
   ```bash
   # Edit pyinstaller.spec
   debug=False  # Already set
   ```

### Faster Startup

1. **Lazy imports:**
   - Move imports inside functions
   - Only import when needed

2. **Onefile vs Directory:**
   - Directory mode (current): Faster startup
   - Onefile mode: Slower startup, single executable

---

## Distribution Checklist

- [ ] Build completed successfully
- [ ] Executable tested on target OS
- [ ] All features working
- [ ] No error messages in console
- [ ] README included in dist folder
- [ ] Folder zipped with proper structure
- [ ] Version number updated in code
- [ ] Release notes prepared
- [ ] Hash/checksum calculated

---

## System Requirements (For Users)

### Windows
- Windows 7 SP1 or later
- 2GB RAM minimum
- 500MB disk space
- Modern graphics driver

### macOS
- macOS 10.13 or later
- 2GB RAM minimum
- 500MB disk space

### Linux
- Ubuntu 16.04 LTS or later
- 2GB RAM minimum
- 500MB disk space
- libxkbcommon-x11-0 library

---

## CI/CD Integration (GitHub Actions)

Future: Automate builds in GitHub Actions

```yaml
# .github/workflows/build.yml
name: Build Executables
on: [release]
jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -e . PyInstaller
      - run: python packaging/build_executable.py
      - uses: actions/upload-artifact@v2
        with:
          name: scrapematrix-windows
          path: dist/ScrapeMatrix
```

---

## Comparison: PyInstaller vs Alternatives

| Feature | PyInstaller | cx_Freeze | py2exe | Nuitka |
|---------|------------|-----------|--------|--------|
| **Cross-platform** | ✅ | ✅ | ❌ | ✅ |
| **Easy setup** | ✅✅ | ✅ | ✅ | ❌ |
| **Executable size** | Large | Medium | Medium | Small |
| **Startup time** | Fast | Fast | Fast | Fastest |
| **Community support** | ✅✅✅ | ✅ | ❌ | ✅ |
| **PyQt6 support** | ✅ | ✅ | ❌ | ✅ |

**We chose PyInstaller:** Most popular, easiest setup, best support

---

## Resources

- **PyInstaller Docs:** https://pyinstaller.org/
- **PyInstaller Config:** https://pyinstaller.org/en/stable/spec-files.html
- **NSIS Installer:** https://nsis.sourceforge.io/
- **UPX Compressor:** https://upx.github.io/

---

## FAQ

**Q: Can I distribute the executable commercially?**
A: Yes! ScrapeMatrix is MIT licensed - free for commercial use.

**Q: Will antivirus flag the executable?**
A: PyInstaller executables sometimes trigger false positives. This is normal and safe.

**Q: Can I run the executable on different OS than where it was built?**
A: No - must build on target OS (Windows exe on Windows, macOS app on macOS, etc)

**Q: How large will the executable be?**
A: ~500MB (includes all dependencies). Size cannot be significantly reduced.

**Q: Can I update the executable after distribution?**
A: Users would need to download new version. Consider cloud updates for future versions.

---

## Next Steps

1. **Build:** Run `python packaging/build_executable.py`
2. **Test:** Run the executable on target OS
3. **Verify:** Test all features work correctly
4. **Package:** Zip the `dist/ScrapeMatrix` folder
5. **Distribute:** Share the ZIP file with users

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
