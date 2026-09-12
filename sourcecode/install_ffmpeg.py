#!/usr/bin/env python3
"""
Install FFmpeg for YouTube Merger
Downloads and extracts FFmpeg to the local directory
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
from pathlib import Path

FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
SCRIPT_DIR = Path(__file__).parent
FFMPEG_DIR = SCRIPT_DIR / "ffmpeg"
FFMPEG_EXE = FFMPEG_DIR / "ffmpeg.exe"


def download_ffmpeg():
    """Download FFmpeg"""
    print("[*] Downloading FFmpeg (this may take a few minutes)...")
    zip_path = SCRIPT_DIR / "ffmpeg.zip"
    
    try:
        urllib.request.urlretrieve(FFMPEG_URL, zip_path)
        print("[+] FFmpeg downloaded successfully")
        return zip_path
    except Exception as e:
        print(f"[-] Failed to download FFmpeg: {e}")
        return None


def extract_ffmpeg(zip_path):
    """Extract FFmpeg"""
    print("[*] Extracting FFmpeg...")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(SCRIPT_DIR / "ffmpeg_temp")
        
        # Find ffmpeg.exe and copy to ffmpeg/
        FFMPEG_DIR.mkdir(exist_ok=True)
        
        for root, dirs, files in os.walk(SCRIPT_DIR / "ffmpeg_temp"):
            if "ffmpeg.exe" in files:
                src = Path(root) / "ffmpeg.exe"
                dst = FFMPEG_DIR / "ffmpeg.exe"
                # Copy the file
                import shutil
                shutil.copy2(src, dst)
                print(f"[+] FFmpeg extracted to {dst}")
                return True
            
            if "ffprobe.exe" in files:
                src = Path(root) / "ffprobe.exe"
                dst = FFMPEG_DIR / "ffprobe.exe"
                import shutil
                shutil.copy2(src, dst)
                print(f"[+] FFprobe extracted to {dst}")
        
        # Cleanup temp folder
        import shutil
        shutil.rmtree(SCRIPT_DIR / "ffmpeg_temp", ignore_errors=True)
        zip_path.unlink()
        
        return True
        
    except Exception as e:
        print(f"[-] Failed to extract FFmpeg: {e}")
        return False


def verify_ffmpeg():
    """Verify FFmpeg installation"""
    try:
        result = subprocess.run(
            [str(FFMPEG_EXE), "-version"],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0:
            print("[+] FFmpeg is working correctly")
            return True
    except Exception:
        pass
    
    print("[-] FFmpeg verification failed")
    return False


def main():
    print("\n" + "="*60)
    print("FFmpeg Installation Tool")
    print("="*60 + "\n")
    
    if FFMPEG_EXE.exists():
        print("[INFO] FFmpeg already exists at:", FFMPEG_EXE)
        if verify_ffmpeg():
            print("[SUCCESS] FFmpeg is ready to use!")
            return 0
    
    # Download
    zip_path = download_ffmpeg()
    if not zip_path:
        return 1
    
    # Extract
    if not extract_ffmpeg(zip_path):
        return 1
    
    # Verify
    if verify_ffmpeg():
        print("\n[SUCCESS] FFmpeg installation complete!")
        print(f"Location: {FFMPEG_DIR}")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
