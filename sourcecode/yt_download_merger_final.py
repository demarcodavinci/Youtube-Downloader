#!/usr/bin/env python3
"""
YouTube Video + Audio Downloader & Merger (Final Version)
Downloads best video and audio streams, merges them into single MP4 file.
All files saved in the SAME DIRECTORY as the executable.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import Optional
import yt_dlp

# Get the directory where this script/executable is located
if getattr(sys, 'frozen', False):
    # Running as executable
    WORK_DIR = Path(sys.executable).parent.absolute()
else:
    # Running as script
    WORK_DIR = Path(__file__).parent.absolute()

TEMP_DIR = WORK_DIR / "temp_download"
FFMPEG_DIR = WORK_DIR / "ffmpeg"
FFMPEG_EXE = FFMPEG_DIR / "ffmpeg.exe"


class YouTubeVideoMerger:
    """Download and merge YouTube video + audio"""

    def __init__(self):
        """Initialize merger"""
        self.work_dir = WORK_DIR
        self.temp_dir = TEMP_DIR
        self.ffmpeg_exe = self._get_ffmpeg_path()
        
        # Create working directories
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"[INFO] Working directory: {self.work_dir}")

    def _get_ffmpeg_path(self) -> Optional[Path]:
        """Get FFmpeg executable path"""
        # Check local FFmpeg first
        if FFMPEG_EXE.exists():
            return FFMPEG_EXE
        
        # Check system PATH
        try:
            result = subprocess.run(
                ['where', 'ffmpeg'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return Path(result.stdout.strip().split('\n')[0])
        except Exception:
            pass
        
        return None

    def _ensure_ffmpeg(self) -> bool:
        """Ensure FFmpeg is available, download if needed"""
        if self.ffmpeg_exe:
            try:
                subprocess.run(
                    [str(self.ffmpeg_exe), "-version"],
                    capture_output=True,
                    timeout=5,
                    check=True
                )
                print("[OK] FFmpeg found and working")
                return True
            except Exception:
                pass
        
        print("[WARNING] FFmpeg not found in system PATH")
        print("[INFO] Attempting to download FFmpeg locally...")
        
        try:
            import urllib.request
            import zipfile
            
            print("[*] Downloading FFmpeg (100-200 MB)...")
            print("[*] This may take several minutes...")
            
            url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
            zip_path = self.temp_dir / "ffmpeg.zip"
            
            urllib.request.urlretrieve(url, zip_path)
            print("[OK] Download complete")
            
            # Extract
            print("[*] Extracting FFmpeg...")
            FFMPEG_DIR.mkdir(exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir / "ffmpeg_extract")
            
            # Find and move ffmpeg.exe
            for root, dirs, files in os.walk(self.temp_dir / "ffmpeg_extract"):
                if "ffmpeg.exe" in files:
                    src = Path(root) / "ffmpeg.exe"
                    dst = FFMPEG_DIR / "ffmpeg.exe"
                    shutil.copy2(src, dst)
                    self.ffmpeg_exe = dst
                    print(f"[OK] FFmpeg installed to: {dst}")
                    
                    # Also copy ffprobe
                    if (Path(root) / "ffprobe.exe").exists():
                        shutil.copy2(Path(root) / "ffprobe.exe", FFMPEG_DIR / "ffprobe.exe")
                    
                    break
            
            # Cleanup extract folder
            shutil.rmtree(self.temp_dir / "ffmpeg_extract", ignore_errors=True)
            zip_path.unlink(missing_ok=True)
            
            return True
            
        except Exception as e:
            print(f"[ERROR] Failed to set up FFmpeg: {e}")
            print("\n[INFO] Please install FFmpeg manually:")
            print("  1. Download from https://ffmpeg.org/download.html")
            print("  2. Extract and add to system PATH")
            print("  3. Or place ffmpeg.exe in this directory")
            return False

    @staticmethod
    def _progress_hook(d):
        """Print download progress"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"  Progress: {percent} | Speed: {speed} | ETA: {eta}", end='\r')
        elif d['status'] == 'finished':
            print("\n  Download finished")

    def get_video_info(self, url: str) -> Optional[dict]:
        """Get video information"""
        try:
            with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"[ERROR] Failed to get video info: {e}")
            return None

    def download_video_stream(
        self, 
        url: str, 
        video_id: str,
        title: str,
        quality: str = "best"
    ) -> Optional[Path]:
        """Download video stream only (no audio)"""
        try:
            quality_map = {
                "best": "bestvideo",
                "720": "bestvideo[height<=720]",
                "480": "bestvideo[height<=480]",
                "360": "bestvideo[height<=360]",
                "240": "bestvideo[height<=240]",
            }
            
            fmt = quality_map.get(quality, "bestvideo")
            filename = f"{title}_{video_id}_VIDEO.%(ext)s"
            
            print(f"\n[Step 1/3] Downloading video stream ({fmt})...")
            
            opts = {
                'format': fmt,
                'outtmpl': str(self.temp_dir / filename),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [self._progress_hook],
            }
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.extract_info(url, download=True)
            
            # Find the downloaded file
            for file in self.temp_dir.glob(f"{title}_{video_id}_VIDEO.*"):
                print(f"[OK] Video saved: {file.name}")
                return file
            
            return None
            
        except Exception as e:
            print(f"[ERROR] Video download failed: {e}")
            return None

    def download_audio_stream(
        self,
        url: str,
        video_id: str,
        title: str
    ) -> Optional[Path]:
        """Download audio stream only (no video)"""
        try:
            filename = f"{title}_{video_id}_AUDIO.%(ext)s"
            
            print(f"\n[Step 2/3] Downloading audio stream (best quality)...")
            
            opts = {
                'format': 'bestaudio',
                'outtmpl': str(self.temp_dir / filename),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [self._progress_hook],
            }
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.extract_info(url, download=True)
            
            # Find the downloaded file
            for file in self.temp_dir.glob(f"{title}_{video_id}_AUDIO.*"):
                print(f"[OK] Audio saved: {file.name}")
                return file
            
            return None
            
        except Exception as e:
            print(f"[ERROR] Audio download failed: {e}")
            return None

    def merge_streams(
        self,
        video_file: Path,
        audio_file: Path,
        output_file: Optional[Path] = None
    ) -> bool:
        """Merge video and audio using FFmpeg"""
        
        if not output_file:
            title = video_file.stem.replace('_VIDEO', '')
            output_file = self.work_dir / f"{title}_MERGED.mp4"
        
        try:
            print(f"\n[Step 3/3] Merging video and audio...")
            print(f"  Video: {video_file.name}")
            print(f"  Audio: {audio_file.name}")
            print(f"  Output: {output_file.name}")
            
            # FFmpeg command
            cmd = [
                str(self.ffmpeg_exe),
                '-i', str(video_file),
                '-i', str(audio_file),
                '-c:v', 'copy',
                '-c:a', 'aac',
                '-shortest',
                '-y',
                str(output_file)
            ]
            
            # Run FFmpeg
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=1200
            )
            
            if result.returncode != 0:
                print(f"[ERROR] FFmpeg failed:\n{result.stderr}")
                return False
            
            if output_file.exists():
                size_mb = output_file.stat().st_size / (1024 * 1024)
                print(f"\n[SUCCESS] Video merged! ({size_mb:.1f} MB)")
                print(f"[OK] Output: {output_file.name}")
                print(f"[OK] Full path: {output_file}")
                return True
            
            return False
            
        except subprocess.TimeoutExpired:
            print("[ERROR] Merge operation timed out")
            return False
        except Exception as e:
            print(f"[ERROR] Merge failed: {e}")
            return False

    def download_and_merge(
        self,
        url: str,
        quality: str = "best",
        output_name: Optional[str] = None
    ) -> bool:
        """Complete download and merge workflow"""
        
        print("\n" + "="*80)
        print("YouTube Video + Audio Merger".center(80))
        print("="*80)
        
        # Ensure FFmpeg
        if not self._ensure_ffmpeg():
            print("\n[ERROR] Cannot proceed without FFmpeg")
            return False
        
        # Get video info
        print(f"\n[INFO] Processing: {url}")
        info = self.get_video_info(url)
        if not info:
            return False
        
        video_id = info.get('id', 'video')
        title = info.get('title', 'download').replace(' ', '_')[:50]
        
        print(f"[+] Title: {info.get('title', 'Unknown')}")
        print(f"[+] Duration: {info.get('duration', 'N/A')} seconds")
        
        # Download streams
        video_file = self.download_video_stream(url, video_id, title, quality)
        if not video_file:
            return False
        
        audio_file = self.download_audio_stream(url, video_id, title)
        if not audio_file:
            return False
        
        # Merge
        if output_name:
            output_file = self.work_dir / output_name
        else:
            output_file = self.work_dir / f"{title}.mp4"
        
        success = self.merge_streams(video_file, audio_file, output_file)
        
        # Cleanup ONLY temp files, NOT output
        if success:
            try:
                print("\n[INFO] Cleaning up temporary files...")
                video_file.unlink(missing_ok=True)
                audio_file.unlink(missing_ok=True)
                
                # Remove temp directory if empty
                try:
                    if self.temp_dir.exists() and not any(self.temp_dir.iterdir()):
                        self.temp_dir.rmdir()
                        print("[OK] Temp directory removed")
                except Exception:
                    pass
                
                print("[OK] Cleanup complete")
            except Exception as e:
                print(f"[WARNING] Cleanup issue: {e}")
        
        print("\n" + "="*80)
        return success


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("\n" + "="*80)
        print("YouTube Video + Audio Downloader & Merger".center(80))
        print("="*80)
        print("\nUsage:")
        print("  YouTube-Merger.exe <URL> [quality] [output_name]")
        print("\nQuality: best, 720, 480, 360, 240 (default: best)")
        print("\nExamples:")
        print("  YouTube-Merger.exe https://www.youtube.com/watch?v=VIDEO_ID")
        print("  YouTube-Merger.exe https://www.youtube.com/watch?v=VIDEO_ID 720")
        print("  YouTube-Merger.exe https://www.youtube.com/watch?v=VIDEO_ID best my_video.mp4")
        print("\nNotes:")
        print("  - Downloads best video + audio streams")
        print("  - Automatically merges them into single MP4")
        print("  - FFmpeg downloaded automatically if not found")
        print("  - All files saved in same directory as executable")
        print("="*80 + "\n")
        return 1
    
    url = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else "best"
    output_name = sys.argv[3] if len(sys.argv) > 3 else None
    
    merger = YouTubeVideoMerger()
    success = merger.download_and_merge(url, quality, output_name)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
