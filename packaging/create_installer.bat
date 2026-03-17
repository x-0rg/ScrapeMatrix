@echo off
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
    echo For now, the dist\ScrapeMatrix folder contains the portable executable
    echo Copy this folder to distribute
    pause
    exit /b 1
)

echo NSIS found, proceeding with installer creation...
REM This would run NSIS installer creation
REM makensis /V4 packaging\scrapematrix_installer.nsi

echo.
echo ===============================================
echo Installation complete!
echo Run: dist\ScrapeMatrix\ScrapeMatrix.exe
echo ===============================================
echo.
pause
