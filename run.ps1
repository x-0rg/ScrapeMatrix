#!/usr/bin/env powershell
# ScrapeMatrix - Quick Start Guide

Write-Host "╔══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                    SCRAPEMATRIX                          ║" -ForegroundColor Cyan
Write-Host "║          Industrial Stock Analysis Desktop App            ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "📋 Checking environment..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check dependencies
Write-Host ""
Write-Host "📦 Checking dependencies..." -ForegroundColor Yellow
$dependencies = @{
    "PyQt6" = "6.6.1"
    "matplotlib" = "3.7.0"
    "pandas" = "1.5.0"
    "yfinance" = "0.2.32"
}

foreach ($dep in $dependencies.GetEnumerator()) {
    $check = python -c "import $($dep.Key); print('OK')" 2>$null
    if ($check -eq "OK") {
        Write-Host "✅ $($dep.Key) >= $($dep.Value)" -ForegroundColor Green
    } else {
        Write-Host "❌ $($dep.Key) not found" -ForegroundColor Red
    }
}

# Install package in dev mode
Write-Host ""
Write-Host "📥 Installing ScrapeMatrix in development mode..." -ForegroundColor Yellow
pip install -e . --quiet 2>$null
Write-Host "✅ Installation complete" -ForegroundColor Green

# Launch application
Write-Host ""
Write-Host "🚀 Starting ScrapeMatrix application..." -ForegroundColor Cyan
Write-Host ""
python -m scrapematrix
