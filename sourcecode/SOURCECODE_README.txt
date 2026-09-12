================================================================================
                    COMPLETE SOURCE CODE PACKAGE
               YouTube Video + Audio Downloader & Merger
================================================================================

Welcome! This folder contains EVERYTHING you need to understand, rebuild, and
customize the YouTube Video Downloader.

Includes:
  ✓ All Python source code
  ✓ PyInstaller build files
  ✓ Compiled executable binary
  ✓ Build artifacts and metadata
  ✓ FFmpeg binaries
  ✓ Build scripts and configuration

================================================================================

FOLDER STRUCTURE
═════════════════════════════════════════════════════════════════════════════

sourcecode/
│
├── dist/                           ← COMPILED EXECUTABLE (USE THIS!)
│   ├── YouTube-Merger.exe          (21.2 MB - Ready to run)
│   └── ffmpeg/                     (FFmpeg binaries)
│       ├── ffmpeg.exe              (98.1 MB)
│       └── ffprobe.exe             (97.9 MB)
│
├── build/                          ← PyInstaller build artifacts
│   └── YouTube-Merger/             (Build intermediate files)
│       ├── PYZ-00.pyz              (Python bytecode archive)
│       ├── base_library.zip        (Python standard library)
│       ├── YouTube-Merger.pkg      (Compiled package)
│       └── ... (other build files)
│
├── ffmpeg/                         ← FFmpeg binaries (original)
│   ├── ffmpeg.exe                  (98.1 MB)
│   └── ffprobe.exe                 (97.9 MB)
│
├── Python Source Code              ← ALL SOURCE FILES
│   ├── yt_download_merger_final.py (12.9 KB - MAIN SCRIPT)
│   ├── yt_video_merger.py          (Alternative version)
│   ├── youtube_downloader.py       (Original downloader)
│   └── youtube_merger.py           (Alternative merger)
│
├── Build Configuration             ← BUILD TOOLS & CONFIG
│   ├── YouTube-Merger.spec         (PyInstaller configuration)
│   ├── requirements.txt            (Python dependencies)
│   ├── build_executable.py         (Build script)
│   ├── install_ffmpeg.py           (FFmpeg installer)
│   └── setup.ps1                   (Windows setup script)
│
└── Documentation                   ← GUIDES & DOCS
    ├── SOURCECODE_README.txt       (This file)
    ├── README.md                   (Project overview)
    ├── MERGER_README.md            (Merger documentation)
    ├── GETTING_STARTED.md          (Quick start)
    ├── RUN_ME.bat                  (Windows launcher)
    └── START_HERE.txt              (Quick reference)

================================================================================

WHAT'S INCLUDED
═════════════════════════════════════════════════════════════════════════════

EXECUTABLE (Ready to Use)
─────────────────────────
  dist/YouTube-Merger.exe (21.2 MB)
    └─ Fully compiled, standalone executable
    └─ Ready to run immediately
    └─ Includes Python + all dependencies bundled
    └─ Download videos with: YouTube-Merger.exe "URL"

BUILD FILES (For Rebuilding)
────────────────────────────
  build/ folder - PyInstaller intermediate files
  YouTube-Merger.spec - PyInstaller configuration
    └─ Complete build metadata
    └─ Can rebuild executable from source
    └─ Modify this to customize compilation

PYTHON SOURCE (For Understanding & Modifying)
──────────────────────────────────────────────
  yt_download_merger_final.py - MAIN SOURCE CODE (12.9 KB)
    └─ ~350 lines of Python
    └─ Well-commented
    └─ Single file, easy to understand
    └─ Edit this to customize functionality

ALTERNATIVE IMPLEMENTATIONS
────────────────────────────
  yt_video_merger.py - Alternative implementation
  youtube_downloader.py - Original downloader
  youtube_merger.py - Alternative merger
    └─ Different approaches to same problem
    └─ Reference implementations

FFMPEG BINARIES (Pre-compiled)
──────────────────────────────
  ffmpeg/ folder - Ready-to-use FFmpeg
  dist/ffmpeg/ - Bundled with executable
    └─ ffmpeg.exe (98.1 MB) - Video/audio processor
    └─ ffprobe.exe (97.9 MB) - Media inspector
    └─ Already compiled for Windows 64-bit

BUILD SCRIPTS
─────────────
  build_executable.py - Automated build script
  install_ffmpeg.py - FFmpeg installation helper
  setup.ps1 - Windows PowerShell setup
  requirements.txt - Python dependencies

================================================================================

QUICK START OPTIONS
═════════════════════════════════════════════════════════════════════════════

OPTION 1: USE EXISTING EXECUTABLE
──────────────────────────────────

Just want to use the program?

  1. Run: dist/YouTube-Merger.exe
  2. Or: YouTube-Merger.exe "https://www.youtube.com/watch?v=VIDEO_ID"
  3. Done!

OPTION 2: RUN PYTHON SCRIPT
───────────────────────────

Want to run as Python without recompiling?

  1. Install dependencies: pip install -r requirements.txt
  2. Run: python yt_download_merger_final.py "https://www.youtube.com/watch?v=VIDEO_ID"
  3. Done!

OPTION 3: REBUILD EXECUTABLE
────────────────────────────

Want to recompile from source?

  1. Install dependencies: pip install -r requirements.txt
  2. Run: pyinstaller YouTube-Merger.spec
  3. New executable: dist/YouTube-Merger.exe
  4. Done!

OPTION 4: MODIFY & REBUILD
──────────────────────────

Want to customize then recompile?

  1. Edit: yt_download_merger_final.py
  2. Test as script: python yt_download_merger_final.py "URL"
  3. When satisfied, rebuild: pyinstaller YouTube-Merger.spec
  4. Use: dist/YouTube-Merger.exe
  5. Done!

================================================================================

FILE DESCRIPTIONS
═════════════════════════════════════════════════════════════════════════════

MAIN SOURCE FILE
────────────────

yt_download_merger_final.py (12.9 KB)
  └─ THE MAIN SOURCE CODE
  └─ ~350 lines of well-commented Python
  └─ YouTubeVideoMerger class with all functionality
  └─ Can run directly as script
  └─ Can be compiled to executable
  
  Methods:
    __init__() - Initialize and setup
    _get_ffmpeg_path() - Find FFmpeg
    _ensure_ffmpeg() - Download FFmpeg if needed
    get_video_info() - Get video metadata
    download_video_stream() - Download video only
    download_audio_stream() - Download audio only
    merge_streams() - Merge video + audio
    download_and_merge() - Main workflow

PYINSTALLER CONFIGURATION
─────────────────────────

YouTube-Merger.spec (0.7 KB)
  └─ PyInstaller configuration file
  └─ Defines how to build executable
  └─ One file, console mode, with all dependencies
  └─ Can modify to customize build
  
  Key settings:
    - name="YouTube-Merger" → Executable name
    - onefile=True → Single .exe file
    - console=True → Shows console window

BUILD ARTIFACTS
───────────────

build/ folder - PyInstaller intermediate files
  └─ YouTube-Merger/ - Build directory
      ├─ PYZ-00.pyz - Python archive
      ├─ base_library.zip - Python standard library
      ├─ YouTube-Merger.pkg - Compiled package
      ├─ Analysis-00.toc - Analysis metadata
      ├─ EXE-00.toc - Executable metadata
      ├─ PKG-00.toc - Package metadata
      └─ ... other files

  These are generated by PyInstaller
  You can delete this folder to save space
  It will be regenerated if you rebuild

COMPILED EXECUTABLE
───────────────────

dist/YouTube-Merger.exe (21.2 MB)
  └─ FINAL COMPILED EXECUTABLE
  └─ Contains Python + all dependencies
  └─ Ready to distribute and use
  └─ No Python installation needed by user

FFMPEG BINARIES
───────────────

ffmpeg/ffmpeg.exe (98.1 MB)
  └─ Video/audio processor
  └─ Pre-compiled for Windows 64-bit
  └─ Used for merging video and audio
  └─ Also bundled in dist/ffmpeg/

ffmpeg/ffprobe.exe (97.9 MB)
  └─ Media inspector
  └─ Analyzes video/audio properties
  └─ Used by yt-dlp and FFmpeg

BUILD SCRIPTS
─────────────

build_executable.py (2 KB)
  └─ Automated build script
  └─ Runs PyInstaller with correct options
  └─ Alternative to manual command

install_ffmpeg.py (3.2 KB)
  └─ FFmpeg installation helper
  └─ Downloads and extracts FFmpeg
  └─ Manual FFmpeg setup if needed

setup.ps1 (2.1 KB)
  └─ Windows PowerShell setup script
  └─ Installs Python dependencies
  └─ Verifies FFmpeg installation

requirements.txt
  └─ Python package dependencies
  └─ yt-dlp - YouTube downloader
  └─ pyinstaller - Executable builder

DOCUMENTATION
──────────────

SOURCECODE_README.txt (This file)
  └─ Complete guide to this package
  └─ Folder structure and file descriptions
  └─ Build instructions and customization

README.md, MERGER_README.md, GETTING_STARTED.md
  └─ Additional documentation
  └─ Usage examples and troubleshooting

================================================================================

HOW TO REBUILD EXECUTABLE
═════════════════════════════════════════════════════════════════════════════

STEP 1: INSTALL DEPENDENCIES
────────────────────────────

  pip install -r requirements.txt

This installs:
  - yt-dlp (YouTube downloader)
  - pyinstaller (executable builder)

STEP 2: REBUILD FROM SPEC
─────────────────────────

  pyinstaller YouTube-Merger.spec

This uses the spec file to rebuild executable with same settings as original.

Takes: 5-15 minutes (first time slower)

STEP 3: FIND NEW EXECUTABLE
───────────────────────────

  dist/YouTube-Merger.exe

Your new executable is ready to use!

STEP 4: TEST IT
──────────────

  dist/YouTube-Merger.exe "https://www.youtube.com/watch?v=VIDEO_ID"

If it works, you're done!

================================================================================

HOW TO MODIFY CODE
═════════════════════════════════════════════════════════════════════════════

QUICK TEST (No Rebuild Needed)
──────────────────────────────

Edit yt_download_merger_final.py and test as script:

  1. Edit file: yt_download_merger_final.py
  2. Test: python yt_download_merger_final.py "URL"
  3. See changes immediately
  4. No recompilation needed

THEN REBUILD WHEN SATISFIED
────────────────────────────

Once happy with changes:

  1. Run: pyinstaller YouTube-Merger.spec
  2. New executable: dist/YouTube-Merger.exe
  3. Done!

MODIFICATION EXAMPLES
─────────────────────

Change Default Quality:
  In yt_download_merger_final.py, find:
    quality = sys.argv[2] if len(sys.argv) > 2 else "best"
  
  Change to:
    quality = sys.argv[2] if len(sys.argv) > 2 else "720"

Add New Quality Level:
  In _get_video_stream(), find quality_map:
    quality_map = {
        "best": "bestvideo",
        "720": "bestvideo[height<=720]",
        ...
    }
  
  Add:
    "1080": "bestvideo[height<=1080]",

Change Output Format:
  In merge_streams(), find:
    '-c:a', 'aac',
  
  Change to:
    '-c:a', 'libmp3lame',  # For MP3 output

Add Features:
  See DEVELOPER_GUIDE.txt for more examples
  (If you have it in your build)

================================================================================

BUILD CUSTOMIZATION
═════════════════════════════════════════════════════════════════════════════

Modify YouTube-Merger.spec to customize build:

Change executable name:
  name='YouTube-Merger'  →  name='MyDownloader'

Change to multiple files:
  onefile=True,  →  onefile=False,

Hide console:
  console=True,  →  console=False,

Add icon:
  icon=None,  →  icon='myicon.ico',

Add data files:
  datas=[],  →  datas=[('ffmpeg', 'ffmpeg')],

Then rebuild:
  pyinstaller YouTube-Merger.spec

================================================================================

DISTRIBUTION OPTIONS
═════════════════════════════════════════════════════════════════════════════

Option 1: Share Executable Only
────────────────────────────────

  Share: dist/YouTube-Merger.exe (21.2 MB)
  
  Pros: Simple, small, user-friendly
  Cons: No source code visible

Option 2: Share Source Code + Executable
─────────────────────────────────────────

  Share: Everything in this folder
  
  Pros: Full transparency, allows customization
  Cons: Large (~300 MB with FFmpeg and build artifacts)

Option 3: Share Source Only
──────────────────────────

  Share: *.py files + requirements.txt
  
  Pros: Small, open source
  Cons: Requires Python and compilation

Option 4: Clean Build Package
─────────────────────────────

For distribution, consider creating clean package:

  1. Copy dist/YouTube-Merger.exe
  2. Delete dist/ffmpeg (user will download on first run)
  3. Include: QUICKSTART.txt
  4. Result: ~21 MB package

Then FFmpeg auto-downloads on first use (100 MB, one time)

================================================================================

COMPILATION NOTES
═════════════════════════════════════════════════════════════════════════════

PyInstaller Details:
  - Version: 6.0.0+
  - Mode: --onefile (single executable)
  - Console: --console (shows output)
  - Platform: Windows 64-bit

Build Process:
  1. Analyzes yt_download_merger_final.py
  2. Finds all imports (yt-dlp, requests, etc.)
  3. Bundles Python 3.14 interpreter
  4. Includes all dependencies
  5. Creates standalone .exe

Executable Size: 21.2 MB
  └─ Includes Python + all dependencies
  └─ This is normal for PyInstaller
  └─ User still needs FFmpeg (auto-downloads)

Build Time: 5-15 minutes first time, faster after

Clean Before Rebuild:
  1. Delete build/ folder (safe to delete)
  2. Delete dist/ folder (safe to delete)
  3. Delete YouTube-Merger.spec (will regenerate)
  4. Then rebuild: pyinstaller YouTube-Merger.spec

================================================================================

TROUBLESHOOTING BUILD ISSUES
═════════════════════════════════════════════════════════════════════════════

Issue: "pyinstaller: command not found"
Solution: pip install pyinstaller

Issue: "yt-dlp: No module named"
Solution: pip install yt-dlp

Issue: Build fails
Solution:
  1. Delete build/ folder
  2. Delete dist/ folder
  3. Run: pyinstaller YouTube-Merger.spec again

Issue: Executable won't run
Solution:
  1. Run as Administrator
  2. Check Windows Defender isn't blocking
  3. Test Python script first: python yt_download_merger_final.py "URL"

Issue: Very large executable (100+ MB)
Solution: This is normal with PyInstaller
  - Includes Python interpreter + all dependencies
  - Can't reduce much without complex configuration
  - FFmpeg (~100 MB) downloads separately

================================================================================

GETTING HELP
═════════════════════════════════════════════════════════════════════════════

This Package Includes:
  - Complete source code with comments
  - Build files and configuration
  - FFmpeg binaries
  - Multiple documentation files

For Questions:
  1. Read the inline comments in yt_download_merger_final.py
  2. Check YouTube-Merger.spec for build configuration
  3. Review other .md and .txt files for documentation
  4. Look at alternative implementations (yt_video_merger.py, etc.)

External Resources:
  - PyInstaller: https://pyinstaller.readthedocs.io/
  - yt-dlp: https://github.com/yt-dlp/yt-dlp
  - FFmpeg: https://ffmpeg.org/documentation.html
  - Python: https://docs.python.org/3/

================================================================================

NEXT STEPS
═════════════════════════════════════════════════════════════════════════════

You have three choices:

1. USE THE EXECUTABLE
   └─ Run: dist/YouTube-Merger.exe
   └─ No setup needed, just download videos!

2. RUN AS PYTHON SCRIPT
   └─ Install: pip install -r requirements.txt
   └─ Run: python yt_download_merger_final.py "URL"
   └─ Easy to test modifications

3. REBUILD & CUSTOMIZE
   └─ Edit: yt_download_merger_final.py
   └─ Install: pip install -r requirements.txt
   └─ Rebuild: pyinstaller YouTube-Merger.spec
   └─ Use: dist/YouTube-Merger.exe

Ready? Choose your path above!

================================================================================

You have everything a developer needs:
  ✓ Source code
  ✓ Compiled executable
  ✓ Build files
  ✓ FFmpeg binaries
  ✓ Build scripts
  ✓ Configuration files
  ✓ Documentation

Happy coding! 🚀

================================================================================
