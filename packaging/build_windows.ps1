# ===============================================
#  ScrapeMatrix - Windows Executable Builder (PowerShell)
# ===============================================
#
# This script builds ScrapeMatrix into a Windows
# executable (.exe) using PyInstaller
#
# Requirements:
#   - Python 3.8+
#   - PyInstaller
#   - All dependencies installed
#
# Usage:
#   .\build_windows.ps1              # Clean build
#   .\build_windows.ps1 -NoClean     # Incremental build
#   .\build_windows.ps1 -Debug       # With debug info

param(
    [switch]$NoClean = $false,
    [switch]$Debug = $false
)

Write-Host "`n" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan
Write-Host "  ScrapeMatrix Windows Build Script" -ForegroundColor Green
Write-Host "=" * 50 -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Error: Python not found" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ from https://www.python.org" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Check PyInstaller installation
Write-Host "Checking PyInstaller..." -ForegroundColor Yellow
try {
    python -c "import PyInstaller" 2>&1 | Out-Null
    Write-Host "✓ PyInstaller found" -ForegroundColor Green
} catch {
    Write-Host "⚠ PyInstaller not found, installing..." -ForegroundColor Yellow
    pip install pyinstaller
}

Write-Host ""
Write-Host "Building ScrapeMatrix executable..." -ForegroundColor Yellow
Write-Host ""

# Build arguments
$buildArgs = @("packaging/build_executable.py", "--platform", "windows")

if (-not $NoClean) {
    $buildArgs += "--clean"
}

if ($Debug) {
    $buildArgs += "--debug"
}

# Run the build script
python @buildArgs

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "=" * 50 -ForegroundColor Green
    Write-Host "  Build completed successfully!" -ForegroundColor Green
    Write-Host "=" * 50 -ForegroundColor Green
    Write-Host ""
    Write-Host "Location: " -ForegroundColor Yellow -NoNewline
    Write-Host "dist\ScrapeMatrix\ScrapeMatrix.exe" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Run: dist\ScrapeMatrix\ScrapeMatrix.exe" -ForegroundColor Gray
    Write-Host "  2. Or zip dist\ScrapeMatrix for distribution" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Build failed! Check errors above." -ForegroundColor Red
    Write-Host ""
    exit 1
}
