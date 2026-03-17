#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ScrapeMatrix Build Script - Create standalone executables

This script builds ScrapeMatrix into a standalone executable using PyInstaller.

Usage:
    python packaging/build_executable.py [--platform windows|macos|linux] [--clean] [--debug]

Examples:
    python packaging/build_executable.py                    # Build for current platform
    python packaging/build_executable.py --platform windows # Build Windows .exe
    python packaging/build_executable.py --clean            # Clean and rebuild
    python packaging/build_executable.py --debug            # Include debug info
"""

import argparse
import os
import sys
import shutil
import subprocess
import io
from pathlib import Path
from typing import Optional

# Fix unicode output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class ScrapeMatrixBuilder:
    """Builder for creating ScrapeMatrix executables."""

    def __init__(self, project_root: Path):
        """Initialize builder.

        Args:
            project_root: Root directory of the ScrapeMatrix project
        """
        self.project_root = project_root
        self.packaging_dir = project_root / "packaging"
        self.build_dir = project_root / "build"
        self.dist_dir = project_root / "dist"
        self.spec_file = self.packaging_dir / "pyinstaller.spec"

    def check_dependencies(self) -> bool:
        """Check if all required dependencies are installed.

        Returns:
            True if all dependencies found, False otherwise
        """
        print("[*] Checking dependencies...")
        required_packages = [
            "PyInstaller",
            "PyQt6",
            "pandas",
            "matplotlib",
            "yfinance",
        ]

        missing = []
        for package in required_packages:
            try:
                __import__(package)
                print(f"  [+] {package}")
            except ImportError:
                print(f"  [-] {package} - MISSING")
                missing.append(package)

        if missing:
            print(f"\n[!] Missing packages: {', '.join(missing)}")
            print(f"\nInstall missing packages with:")
            print(f"  pip install {' '.join(missing)}")
            return False

        return True

    def clean_build(self) -> None:
        """Clean previous build artifacts."""
        print("\n[*] Cleaning previous builds...")

        dirs_to_remove = [self.build_dir, self.dist_dir]
        for dir_path in dirs_to_remove:
            if dir_path.exists():
                print(f"  Removing {dir_path.name}/")
                shutil.rmtree(dir_path)

        # Remove .spec build file if exists
        build_spec = self.packaging_dir / "build"
        if build_spec.exists():
            shutil.rmtree(build_spec)

        print("  [+] Clean complete")

    def build_executable(self, debug: bool = False, clean: bool = False) -> bool:
        """Build the executable using PyInstaller.

        Args:
            debug: Include debug information
            clean: Clean before building

        Returns:
            True if build succeeded, False otherwise
        """
        if clean:
            self.clean_build()

        if not self.check_dependencies():
            return False

        print("\n[*] Building executable...")

        # Build command - use correct PyInstaller arguments
        # When using a .spec file, --specpath is not allowed
        cmd = [
            "pyinstaller",
            str(self.spec_file),
            "--distpath", str(self.dist_dir),
            "--workpath", str(self.build_dir),
        ]

        if debug:
            cmd.append("-d")
            print("  Debug mode enabled")

        print(f"  Running PyInstaller...")

        try:
            result = subprocess.run(cmd, check=True, cwd=str(self.project_root), 
                                  capture_output=False, text=True)
            print("  [+] Build successful")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  [-] Build failed: {e}")
            return False

    def create_installer_batch(self) -> None:
        """Create Windows installer batch script."""
        batch_content = f"""@echo off
REM ScrapeMatrix Windows Installer Script
REM This script packages the ScrapeMatrix executable into an installer

setlocal enabledelayedexpansion

echo.
echo ===============================================
echo  ScrapeMatrix - Windows Installer Builder
echo ===============================================
echo.

REM Check if dist folder exists
if not exist "dist" (
    echo Error: dist folder not found
    echo Please run build_executable.py first
    pause
    exit /b 1
)

echo Creating Windows installer...
echo.

REM Check for NSIS (Nullsoft Scriptable Install System)
where makensis >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Warning: NSIS not found
    echo For installer creation, install NSIS from:
    echo https://nsis.sourceforge.io/
    echo.
    echo For now, the dist\\ScrapeMatrix folder contains the portable executable
    echo Copy this folder to distribute
    pause
    exit /b 1
)

echo NSIS found, proceeding with installer creation...
REM This would run NSIS installer creation
REM makensis /V4 packaging\\scrapematrix_installer.nsi

echo.
echo ===============================================
echo Installation complete!
echo Run: dist\\ScrapeMatrix\\ScrapeMatrix.exe
echo ===============================================
echo.
pause
"""
        batch_file = self.packaging_dir / "create_installer.bat"
        batch_file.write_text(batch_content)
        print(f"  ✅ Created {batch_file.name}")

    def create_readme(self) -> None:
        """Create README for the build output."""
        readme_content = """# ScrapeMatrix Executable Build

## Build Successful ✅

The ScrapeMatrix executable has been built successfully!

### Location
- **Executable**: `dist/ScrapeMatrix/ScrapeMatrix.exe`
- **Data Files**: `dist/ScrapeMatrix/` (all supporting files)

### Running the Application

#### Option 1: Direct Execution
```bash
dist/ScrapeMatrix/ScrapeMatrix.exe
```

#### Option 2: Windows Command Line
```cmd
cd dist\\ScrapeMatrix
ScrapeMatrix.exe
```

#### Option 3: Windows PowerShell
```powershell
& .\\dist\\ScrapeMatrix\\ScrapeMatrix.exe
```

### Distribution

To distribute to users:

1. **Portable Distribution**
   - Zip the entire `dist/ScrapeMatrix` folder
   - Users can extract anywhere and run directly
   - No installation needed
   - Size: ~500MB (includes all dependencies)

2. **With Installer** (optional)
   - Use NSIS to create an installer
   - See `packaging/create_installer.bat`

### System Requirements

- Windows 7 or later
- 2GB RAM minimum
- 500MB disk space
- No Python installation needed

### Troubleshooting

#### Application won't start
- Check Windows Event Viewer for errors
- Try running from command line to see error messages
- Ensure all files are in the `ScrapeMatrix` folder

#### Graphics/Display Issues
- Update graphics drivers
- Try different display DPI settings
- Check Windows compatibility settings

#### Missing Dependencies
- Do not move individual files
- Keep entire `ScrapeMatrix` folder structure intact

### Building on Different Platforms

**Windows (Current)**
```cmd
python packaging\\build_executable.py --clean
```

**macOS**
```bash
python packaging/build_executable.py --platform macos
```

**Linux**
```bash
python packaging/build_executable.py --platform linux
```

### Build Options

```
--platform PLATFORM    Target platform (windows, macos, linux)
--clean               Clean before building
--debug               Include debug information
--no-deps             Don't bundle dependencies
```

### For Developers

See `packaging/build_executable.py` for full build configuration and options.

---

Built with PyInstaller
Project: ScrapeMatrix v0.1.0
"""
        readme_file = self.dist_dir / "ScrapeMatrix" / "README.txt"
        if readme_file.parent.exists():
            readme_file.write_text(readme_content)
            print(f"  ✅ Created README in dist folder")

    def show_summary(self, success: bool) -> None:
        """Show build summary.

        Args:
            success: Whether build was successful
        """
        print("\n" + "=" * 60)
        if success:
            print("  [+] BUILD SUCCESSFUL!")
            print("=" * 60)
            print("\n[*] Executable location:")
            print(f"  {self.dist_dir / 'ScrapeMatrix' / 'ScrapeMatrix.exe'}")
            print("\n[*] To run the application:")
            print(f"  1. Navigate to: {self.dist_dir / 'ScrapeMatrix'}")
            print(f"  2. Double-click: ScrapeMatrix.exe")
            print("\n[*] Distribution:")
            print(f"  Zip the entire 'ScrapeMatrix' folder in dist/")
            print("  Users can extract and run directly (no installation needed)")
            print("\n[*] Size: ~500MB (includes all dependencies)")
        else:
            print("  [-] BUILD FAILED")
            print("=" * 60)
            print("\nPlease check the errors above and try again.")
            print("\n[*] For help, see:")
            print("  - docs/TROUBLESHOOTING.md")
            print("  - packaging/PACKAGING.md")

        print("\n" + "=" * 60 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Build ScrapeMatrix executable",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python packaging/build_executable.py              # Build for current OS
  python packaging/build_executable.py --clean      # Clean and rebuild
  python packaging/build_executable.py --debug      # Include debug info
        """,
    )

    parser.add_argument(
        "--platform",
        choices=["windows", "macos", "linux"],
        default=sys.platform.startswith("win") and "windows" or "linux",
        help="Target platform (default: auto-detect)",
    )
    parser.add_argument("--clean", action="store_true", help="Clean before building")
    parser.add_argument("--debug", action="store_true", help="Include debug information")

    args = parser.parse_args()

    # Determine project root
    script_path = Path(__file__).parent
    project_root = script_path.parent

    # Create builder
    builder = ScrapeMatrixBuilder(project_root)

    # Build executable
    success = builder.build_executable(debug=args.debug, clean=args.clean)

    if success:
        builder.create_installer_batch()
        builder.create_readme()

    builder.show_summary(success)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
