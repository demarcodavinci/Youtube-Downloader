#!/usr/bin/env python3
"""
Build standalone executable using PyInstaller
Creates a single .exe file that includes all dependencies
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
MERGER_SCRIPT = SCRIPT_DIR / "yt_video_merger.py"


def install_pyinstaller():
    """Install PyInstaller if not present"""
    print("[*] Checking PyInstaller...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "show", "pyinstaller"],
            capture_output=True,
            check=True
        )
        print("[+] PyInstaller already installed")
    except subprocess.CalledProcessError:
        print("[*] Installing PyInstaller...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyinstaller"],
            check=True
        )
        print("[+] PyInstaller installed")


def build_exe():
    """Build the executable"""
    print("\n[*] Building executable with PyInstaller...")
    print("[*] This may take a few minutes...")
    
    cmd = [
        sys.executable,
        "-m", "pyinstaller",
        "--onefile",                                    # Single file
        "--icon=NONE",                                  # No icon
        "--name=YouTube-Video-Merger",                  # Output name
        "--console",                                    # Show console
        "--add-data", f"{SCRIPT_DIR}:.",                # Add data files
        str(MERGER_SCRIPT)
    ]
    
    result = subprocess.run(cmd, cwd=str(SCRIPT_DIR))
    
    if result.returncode == 0:
        exe_path = SCRIPT_DIR / "dist" / "YouTube-Video-Merger.exe"
        if exe_path.exists():
            print(f"\n[SUCCESS] Executable created: {exe_path}")
            print(f"[+] Size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
            return True
    
    print("[ERROR] Build failed")
    return False


def main():
    print("="*70)
    print("YouTube Video Merger - Executable Builder")
    print("="*70 + "\n")
    
    install_pyinstaller()
    build_exe()


if __name__ == "__main__":
    main()
