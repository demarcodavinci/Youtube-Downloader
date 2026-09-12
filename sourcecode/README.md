# YouTube Video Downloader

A powerful Python-based YouTube video and audio downloader with support for multiple quality levels.

## Features

✓ Download YouTube videos at various quality levels (360p, 480p, 720p, 1080p, best, worst)
✓ Download audio-only as MP3 files (best, high, medium, low, worst quality)
✓ List all available formats for a video
✓ Progress tracking during downloads
✓ Automatic file naming based on video title and ID
✓ Cross-platform support (Windows, macOS, Linux)

## Prerequisites

- **Python 3.7+** - [Download](https://www.python.org/)
- **FFmpeg** - [Download](https://ffmpeg.org/download.html)
  - FFmpeg is optional but highly recommended for audio extraction and video format conversion

## Installation

### Windows

1. Clone or download this folder
2. Open PowerShell in this directory
3. Run the setup script:
```powershell
.\setup.ps1
```

### Linux/macOS

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install FFmpeg:
   - **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
   - **macOS**: `brew install ffmpeg`

## Usage

### Basic Examples

**Download a video in the best quality:**
```bash
python youtube_downloader.py video "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download a video at 720p:**
```bash
python youtube_downloader.py video "https://www.youtube.com/watch?v=VIDEO_ID" 720
```

**Download audio only (MP3):**
```bash
python youtube_downloader.py audio "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download high-quality audio:**
```bash
python youtube_downloader.py audio "https://www.youtube.com/watch?v=VIDEO_ID" high
```

**List all available formats:**
```bash
python youtube_downloader.py formats "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Show help:**
```bash
python youtube_downloader.py help
```

## Quality Options

### Video Quality
- **best** - Best available quality
- **worst** - Lowest available quality
- **1080** - 1080p or lower
- **720** - 720p or lower
- **480** - 480p or lower
- **360** - 360p or lower
- **240** - 240p or lower

### Audio Quality
- **best** - Best quality (128 kbps+)
- **high** - High quality
- **medium** - Medium quality
- **low** - Low quality
- **worst** - Lowest quality

## Output

Files are automatically saved in the same directory as the script with the naming convention:
```
{video_title}-{video_id}.{extension}
```

## Advanced Usage

You can also use the downloader as a Python module:

```python
from youtube_downloader import YouTubeDownloader
from pathlib import Path

# Initialize downloader
downloader = YouTubeDownloader(Path("/custom/download/path"))

# Download video
downloader.download_video(
    "https://www.youtube.com/watch?v=VIDEO_ID",
    quality="720",
    audio_only=False
)

# Download audio
downloader.download_video(
    "https://www.youtube.com/watch?v=VIDEO_ID",
    quality="best",
    audio_only=True
)

# Get available formats
formats = downloader.list_available_formats("https://www.youtube.com/watch?v=VIDEO_ID")
```

## Troubleshooting

### FFmpeg not found
If you get an error about FFmpeg not being found:
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Add FFmpeg to your system PATH
3. Or install via package manager:
   - Windows: `choco install ffmpeg`
   - macOS: `brew install ffmpeg`
   - Ubuntu: `sudo apt-get install ffmpeg`

### Permission denied (Windows)
If you can't run the setup.ps1 script:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Download fails
- Verify the YouTube URL is correct and the video is publicly available
- Try using a different quality level
- Check your internet connection
- Some videos may have restrictions on downloading

## Dependencies

- **yt-dlp** - YouTube downloader (actively maintained fork of youtube-dl)

## License

This project is provided as-is for educational purposes.

## Support

For issues or feature requests, visit: https://github.com/anomalyco/opencode
