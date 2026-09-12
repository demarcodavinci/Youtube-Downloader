#!/usr/bin/env python3
"""
YouTube Video and Audio Downloader
Supports downloading videos and audio at different quality levels
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional, List
import yt_dlp

# Define the download directory
DOWNLOAD_DIR = Path(__file__).parent.absolute()


class YouTubeDownloader:
    """Download YouTube videos and audio with quality options"""

    def __init__(self, download_dir: Optional[Path] = None):
        """
        Initialize the downloader.
        
        Args:
            download_dir: Directory to save downloads. Defaults to script directory.
        """
        self.download_dir = download_dir or DOWNLOAD_DIR
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self._check_and_install_js_runtime()

    def _check_and_install_js_runtime(self):
        """Check for and install JavaScript runtime if needed"""
        try:
            # Try to import yt_dlp_ejs (should be installed)
            import yt_dlp_ejs  # noqa
        except ImportError:
            try:
                print("[INFO] Installing JavaScript runtime support...")
                subprocess.run([sys.executable, "-m", "pip", "install", "-q", "yt-dlp-ejs"], 
                              capture_output=True, timeout=60)
                print("[INFO] JavaScript runtime installed successfully")
            except Exception:
                print("[WARNING] Could not install JavaScript runtime. Some videos may not work.")
    
    def _has_ffmpeg(self) -> bool:
        """Check if FFmpeg is installed"""
        try:
            subprocess.run(['ffmpeg', '-version'], 
                          capture_output=True, timeout=5, check=True)
            return True
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return False

    def get_video_info(self, url: str) -> dict:
        """
        Get information about a YouTube video.
        
        Args:
            url: YouTube URL
            
        Returns:
            Dictionary with video information
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            print(f"Error getting video info: {e}")
            return {}

    def download_video(
        self,
        url: str,
        quality: str = "best",
        audio_only: bool = False,
    ) -> bool:
        """
        Download a YouTube video or audio.
        
        Args:
            url: YouTube URL
            quality: Quality option ('best', 'worst', or specific format)
            audio_only: If True, download audio only
            
        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"\n{'='*60}")
            print(f"YouTube Downloader")
            print(f"{'='*60}")
            print(f"URL: {url}")
            print(f"Quality: {quality}")
            print(f"Type: {'Audio Only' if audio_only else 'Video'}")
            print(f"Save Location: {self.download_dir}")
            print(f"{'='*60}\n")

            if audio_only:
                ydl_opts = self._get_audio_opts(quality)
            else:
                ydl_opts = self._get_video_opts(quality)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("Starting download...")
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                print(f"\n[SUCCESS] Download completed!")
                print(f"File: {filename}")
                return True

        except Exception as e:
            print(f"\n[ERROR] Download failed: {e}")
            return False

    def _get_video_opts(self, quality: str) -> dict:
        """Get yt-dlp options for video download"""
        has_ffmpeg = self._has_ffmpeg()
        
        # Use simple fallback format selection that works without FFmpeg
        # For this YouTube video, available formats include:
        # Video: 134 (360p), 133 (240p), 160 (144p), 243 (360p webm), etc.
        # Audio: 140 (audio), 251 (audio webm), etc.
        format_map = {
            "best": "best",  # Best single file
            "worst": "worst",
            "1080": "bestvideo[height<=1080]/best",
            "720": "bestvideo[height<=720]/best",
            "480": "bestvideo[height<=480]/best",
            "360": "bestvideo[height=360]/best",
            "240": "bestvideo[height=240]/best",
        }
        
        format_string = format_map.get(quality, "best")
        
        return {
            'format': format_string,
            'outtmpl': str(self.download_dir / '%(title)s-%(id)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'progress_hooks': [self._progress_hook],
            'socket_timeout': 30,
            'extractor_args': {'youtube': {'lang': ['en']}},
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            },
            'skip_unavailable_fragments': True,
        }

    def _get_audio_opts(self, quality: str) -> dict:
        """Get yt-dlp options for audio download"""
        quality_map = {
            "best": 0,
            "worst": 10,
            "high": 0,
            "medium": 5,
            "low": 9,
        }
        
        audio_quality = quality_map.get(quality, 0)
        
        has_ffmpeg = self._has_ffmpeg()
        
        if not has_ffmpeg:
            # Without FFmpeg, just download best audio file directly
            return {
                'format': 'bestaudio/best',
                'outtmpl': str(self.download_dir / '%(title)s-%(id)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [self._progress_hook],
            }
        
        # With FFmpeg, extract audio as MP3
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': str(audio_quality if audio_quality > 0 else '192'),
            }],
            'outtmpl': str(self.download_dir / '%(title)s-%(id)s'),
            'quiet': False,
            'no_warnings': False,
            'progress_hooks': [self._progress_hook],
            'keepvideo': False,
        }

    @staticmethod
    def _progress_hook(d):
        """Progress hook for download progress"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"Progress: {percent} at {speed} (ETA: {eta})", end='\r')
        elif d['status'] == 'finished':
            print("\nDownload finished. Processing...", end='')

    def list_available_formats(self, url: str) -> List[dict]:
        """
        List all available formats for a video.
        
        Args:
            url: YouTube URL
            
        Returns:
            List of available formats
        """
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                formats = info.get('formats', [])
                
                print(f"\nAvailable formats for: {info.get('title', 'Unknown')}\n")
                print(f"{'Format ID':<12} {'Resolution':<15} {'FPS':<8} {'Audio':<15} {'Codec':<20}")
                print("-" * 80)
                
                for fmt in formats:
                    fmt_id = fmt.get('format_id', 'N/A')
                    resolution = f"{fmt.get('height', 'N/A')}p"
                    fps = f"{fmt.get('fps', 'N/A')}"
                    audio = "Yes" if fmt.get('acodec') != 'none' else "No"
                    codec = fmt.get('vcodec', fmt.get('acodec', 'N/A'))[:20]
                    
                    print(f"{fmt_id:<12} {resolution:<15} {fps:<8} {audio:<15} {codec:<20}")
                
                return formats
        except Exception as e:
            print(f"Error listing formats: {e}")
            return []


def print_usage():
    """Print usage instructions"""
    print("\n" + "="*60)
    print("YouTube Downloader - Usage Guide")
    print("="*60)
    print("\nSupported Commands:")
    print("  video <url> [quality]      - Download video")
    print("  audio <url> [quality]      - Download audio only (MP3)")
    print("  formats <url>              - List available formats")
    print("  help                       - Show this help message")
    print("\nQuality Options:")
    print("  Video:  best, worst, 1080, 720, 480, 360, 240")
    print("  Audio:  best, high, medium, low, worst")
    print("\nExamples:")
    print("  python youtube_downloader.py video https://www.youtube.com/watch?v=dQw4w9WgXcQ 720")
    print("  python youtube_downloader.py audio https://www.youtube.com/watch?v=dQw4w9WgXcQ best")
    print("  python youtube_downloader.py formats https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("="*60 + "\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()
    downloader = YouTubeDownloader(DOWNLOAD_DIR)

    if command == "help":
        print_usage()

    elif command == "video":
        if len(sys.argv) < 3:
            print("Error: URL required for video download")
            print_usage()
            return
        url = sys.argv[2]
        quality = sys.argv[3] if len(sys.argv) > 3 else "best"
        downloader.download_video(url, quality=quality, audio_only=False)

    elif command == "audio":
        if len(sys.argv) < 3:
            print("Error: URL required for audio download")
            print_usage()
            return
        url = sys.argv[2]
        quality = sys.argv[3] if len(sys.argv) > 3 else "best"
        downloader.download_video(url, quality=quality, audio_only=True)

    elif command == "formats":
        if len(sys.argv) < 3:
            print("Error: URL required to list formats")
            print_usage()
            return
        url = sys.argv[2]
        downloader.list_available_formats(url)

    else:
        print(f"Unknown command: {command}")
        print_usage()


if __name__ == "__main__":
    main()
