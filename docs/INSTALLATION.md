# 💾 Installation & Setup Guide

Complete guide for installing ScrapeMatrix for users and developers.

## System Requirements

### Minimum Requirements
- **OS:** Windows 7+, macOS 10.13+, or Ubuntu 16.04+
- **RAM:** 2 GB minimum
- **Storage:** 500 MB free space
- **Python:** 3.8+
- **Network:** Internet connection (for stock data)

### Recommended Specification
- **OS:** Windows 10+, macOS 11+, or Ubuntu 20.04+
- **RAM:** 4 GB or more
- **Storage:** 1 GB free space
- **Python:** 3.10+ (latest stable)

---

## Installation Methods

### Method 1: From Source (Recommended for Development)

#### Step 1: Clone Repository
```bash
git clone https://github.com/x-0rg/ScrapeMatrix.git
cd ScrapeMatrix
```

#### Step 2: Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
# Install package in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

#### Step 4: Verify Installation
```bash
# Check Python version
python --version  # Should be 3.8+

# Check if package is installed
python -c "import scrapematrix; print(scrapematrix.__version__)"
# Output: 0.1.0

# Check dependencies
pip list | grep -E "PyQt6|pandas|matplotlib|yfinance"
```

---

### Method 2: From PyPI (Once Released)

```bash
pip install scrapematrix
```

---

### Method 3: Using Conda

```bash
conda create -n scrapematrix python=3.10
conda activate scrapematrix
conda install -c conda-forge pyqt6 pandas matplotlib
pip install yfinance
git clone https://github.com/x-0rg/ScrapeMatrix.git
cd ScrapeMatrix
pip install -e .
```

---

## Virtual Environment Setup

### Why Virtual Environment?
- Isolates project dependencies
- Prevents version conflicts
- Makes project portable
- Simplifies cleanup

### Creating Virtual Environment

**Option 1: venv (Built-in)**
```bash
python -m venv .venv
```

**Option 2: conda (Anaconda)**
```bash
conda create -n scrapematrix python=3.10
```

**Option 3: virtualenv**
```bash
pip install virtualenv
virtualenv .venv
```

### Activating Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### Deactivating Virtual Environment
```bash
deactivate
```

---

## Dependency Installation

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **PyQt6** | >=6.6.1 | GUI framework |
| **pandas** | >=1.5.0 | Data processing |
| **matplotlib** | >=3.7.0 | Visualization |
| **yfinance** | >=0.2.32 | Stock data API |

### Installation Commands

**All dependencies:**
```bash
pip install -e .
```

**Individual packages:**
```bash
pip install PyQt6>=6.6.1
pip install pandas>=1.5.0
pip install matplotlib>=3.7.0
pip install yfinance>=0.2.32
```

**Development dependencies:**
```bash
pip install pytest pytest-cov black flake8 mypy
```

---

## Running the Application

### Method 1: Python Module (Recommended)
```bash
python -m scrapematrix
```

**Advantages:**
- Works everywhere
- Proper module execution
- Correct working directory

### Method 2: PowerShell Script (Windows)
```powershell
.\run.ps1
```

**Features:**
- Environment checking
- Dependency verification
- Automatic launching

### Method 3: Direct Python
```bash
python src/scrapematrix/__main__.py
```

### Method 4: Entry Point
```bash
scrapematrix
```

**Note:** Only works if package is installed with entry points

---

## Troubleshooting Installation

### "Python not found"
```bash
# Check Python installation
python --version

# On macOS/Linux, might need python3
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

### "Module not found" (after installation)
```bash
# Reinstall package
pip install -e . --force-reinstall

# Or reinstall with clean environment
pip cache purge
pip install -e .
```

### "Permission denied"
```bash
# macOS/Linux - might need sudo
sudo pip install -e .

# Or use --user flag
pip install --user -e .
```

### "ModuleNotFoundError"
```bash
# Activate virtual environment
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# Verify activation
which python  # or where python (Windows)
```

### PyQt6 Installation Issues
```bash
# Try upgrading pip first
pip install --upgrade pip

# Then install PyQt6
pip install PyQt6>=6.6.1

# If still failing, try conda
conda install -c conda-forge pyqt6
```

### Display/Graphics Issues
```bash
# Update graphics drivers
# Windows: Device Manager → Display adapters → Update driver
# macOS: Software Update
# Linux: System Settings → About

# Try running with different backend
export QT_QPA_PLATFORM=xcb  # Linux
python -m scrapematrix
```

---

## Development Setup

### Additional Development Tools

```bash
# Testing
pip install pytest pytest-cov pytest-qt

# Code Quality
pip install black flake8 pylint mypy

# Documentation
pip install sphinx sphinx-rtd-theme

# Development convenience
pip install ipython jupyter notebook
```

### IDE Setup

#### Visual Studio Code
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black"
}
```

#### PyCharm
1. File → Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Select "Existing Environment"
4. Point to `.venv/bin/python` (or Scripts/python.exe on Windows)

#### Visual Studio Community
1. File → Open → Project/Solution
2. Select ScrapeMatrix folder
3. Python → Environments → Add Virtual Environment
4. Select existing .venv folder

---

## Verifying Installation

### Complete Verification Script

**Windows (PowerShell):**
```powershell
Write-Host "ScrapeMatrix Installation Verification"
Write-Host "======================================"

# Check Python
python --version

# Activate venv
.\.venv\Scripts\Activate.ps1

# Check package
python -c "import scrapematrix; print('✓ scrapematrix', scrapematrix.__version__)"

# Check dependencies
python -c "import PyQt6; print('✓ PyQt6')"
python -c "import pandas; print('✓ pandas')"
python -c "import matplotlib; print('✓ matplotlib')"
python -c "import yfinance; print('✓ yfinance')"

Write-Host "Installation Complete!"
```

**macOS/Linux (Bash):**
```bash
#!/bin/bash
echo "ScrapeMatrix Installation Verification"
echo "======================================"

# Check Python
python3 --version

# Activate venv
source .venv/bin/activate

# Check package
python -c "import scrapematrix; print('✓ scrapematrix', scrapematrix.__version__)"

# Check dependencies
python -c "import PyQt6; print('✓ PyQt6')"
python -c "import pandas; print('✓ pandas')"
python -c "import matplotlib; print('✓ matplotlib')"
python -c "import yfinance; print('✓ yfinance')"

echo "Installation Complete!"
```

---

## Post-Installation Steps

### 1. Explore the Documentation
```bash
# Read the user guide
cat docs/USER_GUIDE.md

# Read quick start
cat docs/QUICKSTART.md
```

### 2. Run Your First Test
```bash
python -m scrapematrix
```

### 3. Try a Stock Lookup
1. Open application
2. Select NASDAQ from exchange dropdown
3. Type: AAPL
4. Click "Fetch Data"
5. View the chart and information

### 4. (Optional) Run Tests
```bash
pytest tests/
```

---

## Updating Installation

### Update Package
```bash
# Update from source
cd ScrapeMatrix
git pull
pip install -e . --upgrade

# Update from PyPI (when available)
pip install --upgrade scrapematrix
```

### Update Dependencies
```bash
# Update all dependencies
pip install -e . --upgrade

# Update specific package
pip install --upgrade PyQt6
```

---

## Uninstalling

### Remove Package
```bash
pip uninstall scrapematrix
```

### Remove Virtual Environment
```bash
# Windows PowerShell
Remove-Item -Recurse .venv

# macOS/Linux
rm -rf .venv
```

### Clean Installation Cache
```bash
pip cache purge
```

---

## Getting Help

### If Installation Fails

1. **Check Prerequisites**
   - Python 3.8+: `python --version`
   - Git installed: `git --version`
   - Internet connection working

2. **Check Logs**
   ```bash
   pip install -e . --verbose
   ```

3. **Search Issues**
   - GitHub Issues: https://github.com/x-0rg/ScrapeMatrix/issues
   - Read TROUBLESHOOTING.md

4. **Ask for Help**
   - Create an issue with:
     - OS and Python version
     - Full error message
     - Steps to reproduce

---

## System-Specific Notes

### Windows
- Requires Visual C++ Build Tools for some packages
- PowerShell execution policy: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
- Use `python` not `python3`

### macOS
- May need Xcode Command Line Tools: `xcode-select --install`
- Use `python3` and `pip3` explicitly
- May need to allow app in Privacy settings

### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt-get install python3-dev python3-pip python3-venv
sudo apt-get install libxkbcommon-x11-0 libdbus-1-3

# Then proceed with installation
```

---

## Performance Optimization

### For Better Performance

```bash
# Install compiled versions
pip install numpy scipy  # Speeds up pandas

# Install faster YAML parser
pip install pyyaml

# Enable JIT compilation
pip install numba
```

---

## Next Steps

✅ Installation complete!

**Next:**
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Run the application
3. Read [USER_GUIDE.md](USER_GUIDE.md)
4. Explore the codebase

---

**Last Updated:** 2026-03-16  
**Version:** 1.0  
**Status:** ✅ Complete
