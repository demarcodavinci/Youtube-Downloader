# Getting Started with YouTube Video Merger

## The Easiest Way: Run the Executable

### Step 1: Open the executable
Navigate to the `dist` folder and double-click `YouTube-Merger.exe`

### Step 2: Paste a YouTube URL
When prompted, paste a YouTube URL like:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Step 3: Wait for download and merge
The tool will:
1. Download the best video stream (video only, no audio)
2. Download the best audio stream (audio only, no video)
3. Merge them into a single MP4 file
4. Save it to the current directory

### Step 4: Check your file
Look for a `.mp4` file in the same directory as the executable

---

## Command Line Usage (Faster)

### Open Command Prompt or PowerShell

**Windows 10/11:**
1. Press `Win + R`
2. Type `cmd` or `powershell`
3. Press Enter

### Navigate to the dist folder
```bash
cd "C:\Users\YOUR_USERNAME\Downloads\claude\ytdownloader\dist"
```

### Run the command
```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

---

## Usage Options

### Download at Best Quality (Default)
```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Download at Specific Quality
```bash
# 720p
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 720

# 480p
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 480

# 360p (smallest file size)
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 360
```

### Save with Custom Name
```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 720 "my_video.mp4"
```

---

## Real Examples

### Example 1: Download Rick Roll in Best Quality
```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
**Result:** `Rick_Astley_-_Never_Gonna_Give_You_Up_(Official_Vi.mp4` (8.8 MB, ~3 minutes 23 seconds)

### Example 2: Download a Tech Video at 720p
```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=pvSdeU13hKc" 720
```
**Result:** Large video file (500+ MB, ~19 minutes)

### Example 3: Download at Smallest Size (360p)
```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 360 "small_version.mp4"
```
**Result:** `small_version.mp4` (smaller file size)

---

## What Happens When You Run It?

### First Run (30-60 seconds longer)
1. **FFmpeg Download** - ~100 MB file downloaded automatically
2. **Extraction** - FFmpeg extracted to the `ffmpeg/` folder
3. **Verification** - Checks if FFmpeg works

### Subsequent Runs (Faster)
1. **Video Download** - Best video stream downloaded
2. **Audio Download** - Best audio stream downloaded
3. **Merging** - Combines video + audio instantly
4. **Cleanup** - Removes temporary files

### Time Estimates
| Video Length | File Size | Download Time |
|---|---|---|
| 3.5 min | 8.8 MB | 30-60 seconds |
| 10 min | 50-100 MB | 1-2 minutes |
| 20 min | 100-300 MB | 2-5 minutes |
| 1 hour | 300-1000 MB | 5-15 minutes |

---

## Troubleshooting

### Problem: "FFmpeg is downloading..."
**Solution:** This is normal on first run. FFmpeg is a large file (~100 MB) and takes 2-5 minutes to download depending on your internet speed.

### Problem: "Requested format is not available"
**Solution:** Some videos are region-restricted or have limitations. Try:
- A different video
- A different quality level
- Or check if you have access to the video

### Problem: Download is slow
**Solution:** 
- This depends on your internet speed
- Try downloading a shorter video to test
- Check if your internet connection is working

### Problem: "Out of disk space"
**Solution:**
- Free up at least 1-2 GB of disk space
- Or download at lower quality (360p or 480p)

### Problem: Executable won't start
**Solution:**
- Run from Command Prompt instead of double-clicking
- Right-click → "Run as Administrator"
- Check if Windows Defender is blocking it (add exception if needed)

---

## Using the Python Script Instead

If you prefer to run Python directly:

### Requirements
```bash
pip install yt-dlp
```

### Run
```bash
python yt_video_merger.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

---

## File Organization

After first run, you'll have:
```
dist/
├── YouTube-Merger.exe           (21.2 MB - the main executable)
├── ffmpeg/
│   ├── ffmpeg.exe               (auto-downloaded on first run)
│   └── ffprobe.exe              (auto-downloaded on first run)
└── .cache/                      (temporary files, auto-cleaned after merge)

Output:
└── Rick_Astley_-_Never_Gonna_Give_You_Up_(Official_Vi.mp4 (merged video)
```

---

## Pro Tips

### Batch Download Multiple Videos
Create `batch_download.bat`:
```batch
@echo off
cd /d "%~dp0"
"dist\YouTube-Merger.exe" "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 720
"dist\YouTube-Merger.exe" "https://www.youtube.com/watch?v=pvSdeU13hKc" 720
"dist\YouTube-Merger.exe" "https://www.youtube.com/watch?v=..." 720
pause
```

Then double-click to download all videos!

### Save All Videos to One Folder
```bash
cd "C:\My Videos"
"C:\Users\YOUR_USERNAME\Downloads\claude\ytdownloader\dist\YouTube-Merger.exe" "URL" quality
```

### Create Desktop Shortcut
1. Right-click `YouTube-Merger.exe`
2. Send to → Desktop (create shortcut)
3. Double-click shortcut anytime

---

## FAQ

**Q: Is this legal?**
A: Download only videos you have permission to use. Respect YouTube's ToS and copyright laws.

**Q: Will this work offline?**
A: No, you need internet to download videos.

**Q: Can I use this on Mac/Linux?**
A: Run the Python script instead:
```bash
python yt_video_merger.py "URL" quality
```

**Q: How much disk space do I need?**
A: At least 500 MB - 2 GB depending on video length and quality.

**Q: Can I convert to other formats?**
A: The current version outputs MP4. Edit the Python script to output other formats.

**Q: Why does it download video and audio separately?**
A: This gives maximum flexibility - YouTube often stores them separately, and combining them ensures you get the highest quality.

**Q: Does it support playlists?**
A: Not yet. Download videos one at a time, or create a batch file.

---

## Next Steps

1. **Try It Now:**
   ```bash
   YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   ```

2. **Download Your First Video**
   - Paste your own YouTube URL
   - Wait 1-5 minutes
   - Check your downloaded file!

3. **Explore Features**
   - Try different quality levels
   - Test with longer videos
   - Use custom output names

---

## Support

- 📖 Read `MERGER_README.md` for detailed documentation
- 🐛 Report issues: https://github.com/anomalyco/opencode
- 💡 OpenCode feedback: Use `ctrl+p` for help

---

**Ready to download? Run your first command!**

```bash
YouTube-Merger.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Happy downloading! 🎬
