# SeeStar AstroStat 2.0 by Gonhog

**SeeStar AstroStat** is a powerful PowerShell utility designed for astrophotographers using **SeeStar S30/S50** or any FIT/FITS-based imaging workflow. It recursively scans your directory structure, analyzes your imaging sessions, and provides a comprehensive, color-coded summary of your astrophotography data.

---
## Features

- Recursive Scanning - Automatically finds and processes `.fit` files in all subdirectories
- Smart Grouping - Organizes data by object and session
- Expose Analysis - Calculates total frames and exposure time (seconds/minutes/hours)
- Detailed Breakdown - Shows exposure distribution (10s, 20s, 30s, 60s+)
- Color-Coded Output for quick reference:
  - 10s exposures  
  - 20s exposures  
  - 30s exposures  
  - 60s+ exposures
- Storage Analysis - Tracks and displays total file size of all processed files
- Optimized - Fast processing even with thousands of files
- Logging - Optional debug logging to a log file

---

## Quick Start
   ```powershell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Gonhog-Creator/SeeStar-AstroStat-2.0/main/SeeStar_AstroStat_2.0_by_Gonhog.ps1" -OutFile "AstroStat.ps1"
   ```

2. **Run** the script:
   - **Method 1**: Right-click the script → "Run with PowerShell"
   - **Method 2**: Open PowerShell and run:
     ```powershell
     .\SeeStar_AstroStat_2.0_by_Gonhog.ps1
     ```

3. **View Results**: The script will display a summary of all your imaging sessions.

## File Organization

The script works with any folder structure, but here's the recommended organization:
```
AstroPhotos/
├── M31/
│   ├── 2023-11-01_City1/
│   │   ├── lights/
│   │   └── stacked/
│   └── 2023-11-02_DarkSite/
│       ├── lights/
│       └── stacked/
└── Orion_Nebula/
    └── 2023-10-15_Backyard/
        ├── lights/
        └── stacked/
```

## Example Output

```
=== SeeStar AstroStat 2.0 by Gonhog ===

M31
|-- 2023-11-01_City1      |  120 frames |   1200s  0.33h | 120x10s 100%
|-- 2023-11-02_DarkSite   |   80 frames |   2400s  0.67h | 80x30s 100%

Orion_Nebula
|-- 2023-10-15_Backyard   |  150 frames |   1500s  0.42h | 150x10s 100%
|-- 2023-10-16_Backyard   |  200 frames |   2000s  0.56h | 200x10s 100%

--------------------------------------------
Global Summary:
 Total frames: 550
 Total exposure: 7100s | 118.33min | 1.97h
 Total file size: 15.75 GB
 Unique objects: 2
--------------------------------------------
```

## Advanced Usage

### Command Line Options
```powershell
# Run with debug logging
.\SeeStar_AstroStat_2.0_by_Gonhog.ps1 -Verbose

# Specify a custom directory to scan
.\SeeStar_AstroStat_2.0_by_Gonhog.ps1 -Path "D:\AstroPhotos"
```

### File Naming Convention
The script supports standard FIT/FITS naming patterns:
- `Light_10s_001.fit`
- `Stacked_30_10s.fit`
- `M31_20s_001.fit`

## Requirements

- **OS**: Windows 10/11
- **PowerShell**: 5.1 or newer
- **Files**: FIT or FITS format with exposure time in filename

## Troubleshooting

If you encounter any issues:
1. Check the `astrostats_debug.log` file for detailed error messages
2. Ensure your files follow the supported naming conventions
3. Run with `-Verbose` for more detailed output

## License

**MIT License**  
 2023 Gonhog

## Acknowledgments

- Original code by LeoN61ukr
- Modified by Gonhog

---

> Clear skies and happy imaging! 
