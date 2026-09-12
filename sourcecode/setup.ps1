# YouTube Downloader Setup Script for Windows PowerShell

Write-Host "YouTube Downloader Setup" -ForegroundColor Green
Write-Host "======================" -ForegroundColor Green
Write-Host ""

# Check if Python is installed
Write-Host "Checking for Python installation..." -ForegroundColor Yellow
$python_check = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ from https://www.python.org" -ForegroundColor Yellow
    exit 1
}
Write-Host "Python found: $python_check" -ForegroundColor Green

# Check if FFmpeg is installed
Write-Host "Checking for FFmpeg installation..." -ForegroundColor Yellow
$ffmpeg_check = ffmpeg -version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: FFmpeg is not installed or not in PATH" -ForegroundColor Yellow
    Write-Host "FFmpeg is required for audio extraction and video conversion" -ForegroundColor Yellow
    Write-Host "Install from: https://ffmpeg.org/download.html" -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "Continue without FFmpeg? (y/n)"
    if ($continue -ne "y") {
        exit 1
    }
} else {
    Write-Host "FFmpeg found!" -ForegroundColor Green
}

Write-Host ""
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Setup completed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Green
    Write-Host "  Download video:     python youtube_downloader.py video <URL> [quality]" -ForegroundColor Cyan
    Write-Host "  Download audio:     python youtube_downloader.py audio <URL> [quality]" -ForegroundColor Cyan
    Write-Host "  List formats:       python youtube_downloader.py formats <URL>" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Video qualities:  best, worst, 1080, 720, 480, 360, 240" -ForegroundColor Cyan
    Write-Host "Audio qualities:  best, high, medium, low, worst" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host "Setup failed!" -ForegroundColor Red
    exit 1
}
