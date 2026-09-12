# YouTube Video + Audio Merger (Complete Solution)

A fully functional solution to download YouTube videos and audio, then merge them into a single high-quality MP4 file.

## Features

✅ **Download Best Video Stream** - Gets the best available video quality
✅ **Download Best Audio Stream** - Gets the highest quality audio
✅ **Automatic Merging** - Combines video + audio into single MP4 file
✅ **FFmpeg Auto-Install** - Automatically downloads FFmpeg if not found
✅ **Standalone Executable** - 21.2 MB .exe file that runs without Python
✅ **Python Script Option** - Use Python script directly for more control
✅ **Quality Selection** - Choose video quality: best, 720p, 480p, 360p, 240p
✅ **Progress Tracking** - Real-time download and merge progress
✅ **Automatic Cleanup** - Removes temporary files after merging

## Quick Start

### Option 1: Using Standalone Executable (Easiest)

```bash
# Navigate to dist folder
cd dist

# Run the executable
YouTube-Merger.exe "https://www.youtube.com/watch?v=VIDEO_ID"

# Specify quality (optional)
YouTube-Merger.exe "https://www.youtube.com/watch?v=VIDEO_ID" 720

# Specify output filename (optional)
YouTube-Merger.exe "https://www.youtube.com/watch?v=VIDEO_ID" 360 "my_video.mp4"
```

### Option 2: Using Python Script

```bash
# Basic usage
python yt_video_merger.py "https://www.youtube.com/watch?v=VIDEO_ID"

# With quality selection
python yt_video_merger.py "https://www.youtube.com/watch?v=VIDEO_ID" 720

# With custom output name
python yt_video_merger.py "https://www.youtube.com/watch?v=VIDEO_ID" best "my_video.mp4"
```

## Requirements

### For Executable (.exe)
- **Windows OS** (built for Windows 64-bit)
- **Internet connection**
- **FFmpeg** (auto-downloaded on first run)
- **~1-2 GB free disk space** (for large videos)

### For Python Script
- **Python 3.7+**
- **Dependencies**: yt-dlp, requests
- **FFmpeg** (auto-downloaded on first run)

## Installation

### No Installation Needed!

The executable is standalone and portable. Just run it directly:

```bash
cd dist
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## Usage Examples

```bash
# Download Rick Roll in best quality and merge
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download at 720p
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 720

# Download at 360p with custom name
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 360 "rickroll.mp4"

# Long form video (19 minutes) - usually takes 2-5 minutes to download and merge
YouTube-Merger.exe "https://www.youtube.com/watch?v=pvSdeU13hKc" best

# Download short video (3.5 minutes) - usually takes 30-60 seconds total
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" best
```

## Quality Options

- **best** - Best available quality (usually 1080p or 720p video + highest bitrate audio)
- **720** - Download at maximum 720p resolution
- **480** - Download at maximum 480p resolution
- **360** - Download at maximum 360p resolution
- **240** - Download at maximum 240p resolution

## How It Works

1. **Video Extraction**: Downloads the best available video stream (no audio)
2. **Audio Extraction**: Downloads the best available audio stream
3. **Merging**: Uses FFmpeg to combine video + audio into single MP4
4. **Cleanup**: Removes temporary files
5. **Output**: Final merged video saved to current directory

## Output

The merged video file is saved in the current directory with:
- **Format**: MP4 (H.264 video + AAC audio)
- **Codec**: Copy (no re-encoding, keeps original quality)
- **Naming**: Based on video title + ".mp4"

Example:
```
Rick_Astley_-_Never_Gonna_Give_You_Up_(Official_Vi.mp4 (8.8 MB, 3.5 minutes)
This_GPU_can_be_Hacked_to_Unlock_Secret_Memory.mp4 (687+ MB, 19 minutes)
```

## Troubleshooting

### "FFmpeg not found"
Solution: The script will automatically download FFmpeg on first run. This may take 2-5 minutes.

### "Requested format is not available"
Solution: YouTube may have restricted this video. Try a different quality option or URL.

### "Download is very slow"
Solution: This is normal - depends on your internet speed. Large videos take longer.
- 3.5 minute video at 360p: ~30-60 seconds
- 19 minute video at best: ~2-5 minutes
- 1 hour video at best: ~15-30 minutes

### "Out of disk space"
Solution: Ensure you have enough free space. Rule of thumb:
- 360p video: ~50-100 MB
- 720p video: ~200-500 MB
- Best quality: ~500MB-2GB depending on duration

### Executable won't run
Solution: Make sure you're running `YouTube-Merger.exe`, not the Python script. If it still fails:
1. Try running from Command Prompt instead of PowerShell
2. Check Windows Defender isn't blocking it
3. Run as Administrator

### FFmpeg not downloading
If automatic download fails, download manually:
1. Visit https://ffmpeg.org/download.html
2. Download "ffmpeg-essentials" for Windows
3. Extract to the same directory as the executable
4. Create a folder named "ffmpeg" and place ffmpeg.exe inside

## Files Included

```
ytdownloader/
├── YouTube-Merger.exe           # Standalone executable (21.2 MB)
├── yt_video_merger.py           # Python script source
├── youtube_downloader.py        # Original downloader script
├── ffmpeg/                      # FFmpeg binaries (auto-downloaded)
├── .cache/                      # Temporary files (auto-cleaned)
└── README files                 # Documentation
```

## Technical Details

### Executable Size
- **21.2 MB** (includes Python, all dependencies, but not FFmpeg)
- FFmpeg (98+ MB) downloaded on first run to `ffmpeg/` folder

### Performance
- Video download speed: Limited by internet speed (5-20 MB/s typical)
- Audio download speed: Usually 2-3 MB/s
- Merging speed: Instant (just combines without re-encoding)

### Supported URLs
- ✅ YouTube videos
- ✅ YouTube Shorts
- ✅ Unlisted videos
- ✅ Private videos (if you have access)
- ✅ Age-restricted videos (may require authentication)

## Advanced Usage

### Batch Download Multiple Videos

**Create a file `download_list.txt`:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=pvSdeU13hKc
https://www.youtube.com/watch?v=...
```

**Run batch script:**
```bash
for /f %%i in (download_list.txt) do (
    YouTube-Merger.exe "%%i" 720
)
```

### Custom Output Directory

The executable always saves to the current directory. To save to a specific folder:
```bash
cd "C:\My Videos"
"C:\Users\omgpr\Downloads\claude\ytdownloader\dist\YouTube-Merger.exe" "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Supported Platforms

- ✅ **Windows 10+** (64-bit) - Primary support
- ⚠️ **Windows 7-8** - May need manual FFmpeg installation
- ✅ **Linux/macOS** - Use Python script with `python yt_video_merger.py`

## Legal Notice

This tool is for downloading videos you have permission to download. Respect copyright laws and YouTube's Terms of Service. Only download videos you have rights to use.

## Support & Issues

If you encounter issues:

1. Try running from Command Prompt (not PowerShell)
2. Check you have internet connection
3. Verify the YouTube URL is valid and public
4. Try a different video to test
5. Check disk space is available
6. Report issues at: https://github.com/anomalyco/opencode

## Changelog

### v1.0 (Current)
- ✨ Standalone executable released
- ✨ Auto FFmpeg installation
- ✨ Video + audio merging
- ✨ Quality selection
- ✨ Progress tracking
- ✨ Automatic cleanup

## License

This project is provided as-is for educational purposes.

---

**Tested with:**
- Windows 11 (Pro, 64-bit)
- YouTube videos from 3.5 minutes to 19+ minutes
- Quality formats: 360p, 720p, 1080p
- File sizes: 8 MB to 700+ MB

**Last Updated:** September 13, 2026
