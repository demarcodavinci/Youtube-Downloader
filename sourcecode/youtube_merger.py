#!/usr/bin/env python3
"""
YouTube Video & Audio Merger - Download and combine best quality video + audio
Creates a fully merged video file with both audio and video streams
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Optional, Tuple
import yt_dlp

# Define the download directory
DOWNLOAD_DIR = Path(__file__).parent.absolute()
TEMP_DIR = DOWNLOAD_DIR / ".tmp"


class YouTubeMerger:
    """Download YouTube video and audio, then merge them together"""

    def __init__(self, download_dir: Optional[Path] = None):
        """
        Initialize the merger.
        
        Args:
            download_dir: Directory to save downloads. Defaults to script directory.
        """
        self.download_dir = download_dir or DOWNLOAD_DIR
        self.temp_dir = self.download_dir / ".tmp"
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_ffmpeg()

    def _ensure_ffmpeg(self):
        """Ensure FFmpeg is available"""
        if self._has_ffmpeg():
            print("[INFO] FFmpeg is already installed and available")
            return
        
        print("[WARNING] FFmpeg not found in PATH")
        print("[INFO] Attempting to install FFmpeg...")
        
        # Try pip installation of ffmpeg-python wrapper
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "-q", "ffmpeg-python"],
                capture_output=True,
                timeout=60
            )
            print("[INFO] ffmpeg-python package installed")
        except Exception as e:
            print(f"[WARNING] Could not install ffmpeg-python: {e}")
            print("[INFO] Downloading FFmpeg from official source...")
            self._download_ffmpeg()

    def _download_ffmpeg(self):
        """Download FFmpeg executable for Windows"""
        try:
            import urllib.request
            import zipfile
            
            print("[INFO] Downloading FFmpeg...")
            ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
            zip_path = self.temp_dir / "ffmpeg.zip"
            
            urllib.request.urlretrieve(ffmpeg_url, zip_path)
            
            print("[INFO] Extracting FFmpeg...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir)
            
            # Find ffmpeg.exe
            ffmpeg_exe = None
            for root, dirs, files in os.walk(self.temp_dir):
                if "ffmpeg.exe" in files:
                    ffmpeg_exe = Path(root) / "ffmpeg.exe"
                    break
            
            if ffmpeg_exe:
                print(f"[SUCCESS] FFmpeg downloaded to: {ffmpeg_exe}")
                self.ffmpeg_path = ffmpeg_exe
            else:
                print("[WARNING] Could not locate ffmpeg.exe after extraction")
        except Exception as e:
            print(f"[ERROR] Failed to download FFmpeg: {e}")
            print("[INFO] Please install FFmpeg manually from https://ffmpeg.org/download.html")

    @staticmethod
    def _has_ffmpeg() -> bool:
        """Check if FFmpeg is installed"""
        try:
            subprocess.run(
                ['ffmpeg', '-version'],
                capture_output=True,
                timeout=5,
                check=True
            )
            return True
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return False

    @staticmethod
    def _progress_hook(d):
        """Progress hook for download progress"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"Progress: {percent} at {speed} (ETA: {eta})", end='\r')
        elif d['status'] == 'finished':
            print("\nDownload finished", end='')

    def download_best_video(self, url: str, quality: str = "best") -> Tuple[Optional[Path], Optional[Path]]:
        """
        Download best video and audio streams separately.
        
        Args:
            url: YouTube URL
            quality: Quality option ('best', '720', '480', '360', '240')
            
        Returns:
            Tuple of (video_path, audio_path) or (None, None) on failure
        """
        try:
            print(f"\n{'='*70}")
            print(f"YouTube Video + Audio Downloader")
            print(f"{'='*70}")
            print(f"URL: {url}")
            print(f"Quality: {quality}")
            print(f"Output Directory: {self.download_dir}")
            print(f"{'='*70}\n")

            # Get video info first
            print("[1/3] Getting video information...")
            info = self._get_video_info(url)
            if not info:
                print("[ERROR] Could not get video information")
                return None, None
            
            video_id = info.get('id', 'unknown')
            title = info.get('title', 'video')
            
            print(f"[INFO] Title: {title}")
            print(f"[INFO] Video ID: {video_id}")

            # Download video stream
            print("\n[2/3] Downloading best video stream...")
            video_path = self._download_video_stream(url, video_id, title, quality)
            if not video_path:
                print("[ERROR] Failed to download video stream")
                return None, None
            
            print(f"[SUCCESS] Video downloaded: {video_path.name}")

            # Download audio stream
            print("\n[3/3] Downloading best audio stream...")
            audio_path = self._download_audio_stream(url, video_id, title)
            if not audio_path:
                print("[ERROR] Failed to download audio stream")
                return None, None
            
            print(f"[SUCCESS] Audio downloaded: {audio_path.name}")

            return video_path, audio_path

        except Exception as e:
            print(f"[ERROR] Error during download: {e}")
            return None, None

    def _get_video_info(self, url: str) -> Optional[dict]:
        """Get video information"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"[ERROR] Failed to get video info: {e}")
            return None

    def _download_video_stream(self, url: str, video_id: str, title: str, quality: str) -> Optional[Path]:
        """Download best video stream (video only, no audio)"""
        try:
            quality_map = {
                "best": "bestvideo",
                "720": "bestvideo[height<=720]",
                "480": "bestvideo[height<=480]",
                "360": "bestvideo[height<=360]",
                "240": "bestvideo[height<=240]",
            }
            
            format_string = quality_map.get(quality, "bestvideo")
            
            video_filename = f"{title}_{video_id}_video.mp4"
            ydl_opts = {
                'format': format_string,
                'outtmpl': str(self.temp_dir / video_filename),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [self._progress_hook],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading video stream (format: {format_string})...")
                ydl.extract_info(url, download=True)
            
            video_path = self.temp_dir / video_filename
            if video_path.exists():
                return video_path
            
            # Try to find the actual downloaded file
            for file in self.temp_dir.glob(f"{title}_{video_id}_video*"):
                return file
            
            print("[WARNING] Could not locate downloaded video file")
            return None
            
        except Exception as e:
            print(f"[ERROR] Video download failed: {e}")
            return None

    def _download_audio_stream(self, url: str, video_id: str, title: str) -> Optional[Path]:
        """Download best audio stream (audio only, no video)"""
        try:
            audio_filename = f"{title}_{video_id}_audio.m4a"
            ydl_opts = {
                'format': 'bestaudio',
                'outtmpl': str(self.temp_dir / audio_filename),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [self._progress_hook],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading audio stream (bestaudio)...")
                ydl.extract_info(url, download=True)
            
            audio_path = self.temp_dir / audio_filename
            if audio_path.exists():
                return audio_path
            
            # Try to find the actual downloaded file
            for file in self.temp_dir.glob(f"{title}_{video_id}_audio*"):
                return file
            
            print("[WARNING] Could not locate downloaded audio file")
            return None
            
        except Exception as e:
            print(f"[ERROR] Audio download failed: {e}")
            return None

    def merge_video_audio(self, video_path: Path, audio_path: Path, output_name: Optional[str] = None) -> bool:
        """
        Merge video and audio files using FFmpeg.
        
        Args:
            video_path: Path to video file
            audio_path: Path to audio file
            output_name: Output filename (optional)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not video_path.exists():
                print(f"[ERROR] Video file not found: {video_path}")
                return False
            
            if not audio_path.exists():
                print(f"[ERROR] Audio file not found: {audio_path}")
                return False
            
            if not output_name:
                # Extract title from video filename
                output_name = video_path.stem.rsplit('_video', 1)[0] + ".mp4"
            
            output_path = self.download_dir / output_name
            
            print(f"\n{'='*70}")
            print(f"Merging Video + Audio")
            print(f"{'='*70}")
            print(f"Video: {video_path.name}")
            print(f"Audio: {audio_path.name}")
            print(f"Output: {output_name}")
            print(f"{'='*70}\n")
            
            # FFmpeg command to merge video and audio
            ffmpeg_cmd = [
                'ffmpeg',
                '-i', str(video_path),      # Input video
                '-i', str(audio_path),      # Input audio
                '-c:v', 'copy',             # Copy video codec (no re-encoding)
                '-c:a', 'aac',              # Use AAC audio codec
                '-shortest',                # Use shortest stream length
                '-y',                       # Overwrite output file
                str(output_path)            # Output file
            ]
            
            print(f"Running FFmpeg merge command...")
            result = subprocess.run(
                ffmpeg_cmd,
                capture_output=True,
                text=True,
                timeout=600  # 10 minute timeout
            )
            
            if result.returncode != 0:
                print(f"[ERROR] FFmpeg merge failed:")
                print(result.stderr)
                return False
            
            if output_path.exists():
                file_size_mb = output_path.stat().st_size / (1024 * 1024)
                print(f"\n[SUCCESS] Video merged successfully!")
                print(f"Output: {output_path}")
                print(f"File size: {file_size_mb:.2f} MB")
                return True
            else:
                print("[ERROR] Output file was not created")
                return False
                
        except subprocess.TimeoutExpired:
            print("[ERROR] FFmpeg merge operation timed out")
            return False
        except Exception as e:
            print(f"[ERROR] Merge failed: {e}")
            return False

    def download_and_merge(self, url: str, quality: str = "best", output_name: Optional[str] = None) -> bool:
        """
        Complete workflow: download video, download audio, and merge them.
        
        Args:
            url: YouTube URL
            quality: Video quality
            output_name: Output filename (optional)
            
        Returns:
            True if successful, False otherwise
        """
        video_path, audio_path = self.download_best_video(url, quality)
        
        if not video_path or not audio_path:
            return False
        
        success = self.merge_video_audio(video_path, audio_path, output_name)
        
        # Cleanup temp files if merge was successful
        if success:
            try:
                print("\n[INFO] Cleaning up temporary files...")
                video_path.unlink()
                audio_path.unlink()
                print("[INFO] Temporary files removed")
            except Exception as e:
                print(f"[WARNING] Could not clean up temp files: {e}")
        
        return success


def print_usage():
    """Print usage instructions"""
    print("\n" + "="*70)
    print("YouTube Video + Audio Downloader & Merger")
    print("="*70)
    print("\nUsage:")
    print("  python youtube_merger.py <URL> [quality] [output_name]")
    print("\nQuality options: best, 720, 480, 360, 240")
    print("\nExamples:")
    print("  python youtube_merger.py https://www.youtube.com/watch?v=VIDEO_ID")
    print("  python youtube_merger.py https://www.youtube.com/watch?v=VIDEO_ID 720")
    print("  python youtube_merger.py https://www.youtube.com/watch?v=VIDEO_ID best my_video.mp4")
    print("\nNotes:")
    print("  - Downloads the best available video and audio streams separately")
    print("  - Merges them into a single MP4 file using FFmpeg")
    print("  - Requires FFmpeg to be installed or in PATH")
    print("  - All output files are saved to the script directory")
    print("="*70 + "\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    url = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else "best"
    output_name = sys.argv[3] if len(sys.argv) > 3 else None
    
    merger = YouTubeMerger(DOWNLOAD_DIR)
    success = merger.download_and_merge(url, quality, output_name)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
