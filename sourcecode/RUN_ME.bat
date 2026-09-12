@echo off
REM YouTube Video Merger - Batch Launcher
REM Double-click this file to run the YouTube downloader and merger

echo.
echo ===============================================
echo   YouTube Video + Audio Merger
echo ===============================================
echo.

REM Check if URL is provided as command line argument
if "%~1"=="" (
    echo Usage:
    echo   1. Double-click this file and paste a YouTube URL
    echo   2. Or run: RUN_ME.bat "https://www.youtube.com/watch?v=VIDEO_ID"
    echo.
    set /p URL="Enter YouTube URL: "
) else (
    set URL=%~1
)

if "%URL%"=="" (
    echo Error: No URL provided
    pause
    exit /b 1
)

REM Check if quality is provided
if "%~2"=="" (
    set QUALITY=best
) else (
    set QUALITY=%~2
)

echo.
echo Downloading and merging video from:
echo %URL%
echo Quality: %QUALITY%
echo.

REM Run the executable
if exist "dist\YouTube-Merger.exe" (
    cd /d "%~dp0"
    "dist\YouTube-Merger.exe" "%URL%" "%QUALITY%"
) else (
    echo Error: YouTube-Merger.exe not found!
    echo Please ensure YouTube-Merger.exe is in the dist folder
    pause
    exit /b 1
)

echo.
echo Done! Press any key to exit...
pause
exit /b 0
