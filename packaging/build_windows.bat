@echo off
REM ===============================================
REM  ScrapeMatrix - Windows Executable Builder
REM ===============================================
REM
REM This script builds ScrapeMatrix into a Windows
REM executable (.exe) using PyInstaller
REM
REM Requirements:
REM   - Python 3.8+
REM   - PyInstaller
REM   - All dependencies installed
REM
REM Usage:
REM   .\build_windows.bat              (clean build)
REM   .\build_windows.bat --no-clean   (incremental build)

setlocal enabledelayedexpansion

echo.
echo ===============================================
echo  ScrapeMatrix Windows Build Script
echo ===============================================
echo.

REM Check Python installation
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not found
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python found:
python --version
echo.

REM Check PyInstaller installation
python -c "import PyInstaller" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ⚠ PyInstaller not found
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo.
echo Building ScrapeMatrix executable...
echo.

REM Run the build script
python packaging/build_executable.py --platform windows %*

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ===============================================
    echo  Build completed successfully!
    echo ===============================================
    echo.
    echo Location: dist\ScrapeMatrix\ScrapeMatrix.exe
    echo.
    echo Next steps:
    echo   1. Run: dist\ScrapeMatrix\ScrapeMatrix.exe
    echo   2. Or zip dist\ScrapeMatrix for distribution
    echo.
) else (
    echo.
    echo Build failed! Check errors above.
    echo.
)

pause
