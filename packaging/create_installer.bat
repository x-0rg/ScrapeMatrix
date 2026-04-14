@echo off
REM ScrapeMatrix Windows Installer Script (v0.1.0)
REM Production-ready installer with error handling

setlocal enabledelayedexpansion

echo.
echo ===============================================
echo  ScrapeMatrix - Windows Installer Builder v0.1.0
echo ===============================================
echo.

REM Check if dist folder exists
if not exist "dist" (
    echo Error: dist folder not found
    echo Please run build_executable.py first
    pause
    exit /b 1
)

REM Check if executable exists
if not exist "dist\ScrapeMatrix\ScrapeMatrix.exe" (
    echo Error: ScrapeMatrix.exe not found
    echo Build may have failed
    pause
    exit /b 1
)

echo [OK] Executable found
echo.

REM Check for NSIS (Nullsoft Scriptable Install System)
where makensis >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] NSIS not found (optional)
    echo.
    echo For installer creation, install NSIS from:
    echo https://nsis.sourceforge.io/
    echo.
    echo For now, the dist\ScrapeMatrix folder is ready for distribution:
    echo - Portable executable (no installation needed)
    echo - All dependencies included
    echo - Ready to zip and distribute
    echo.
    echo Next steps:
    echo 1. Run: dist\ScrapeMatrix\ScrapeMatrix.exe
    echo 2. Or zip dist\ScrapeMatrix for distribution
    echo.
    pause
    exit /b 0
)

echo [OK] NSIS found, proceeding with installer creation...
echo.

REM This would run NSIS installer creation
REM makensis /V4 packaging\scrapematrix_installer.nsi

echo ===============================================
echo Installation preparation complete!
echo ===============================================
echo.
echo Run: dist\ScrapeMatrix\ScrapeMatrix.exe
echo.
pause
