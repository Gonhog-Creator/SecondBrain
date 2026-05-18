# ==============================
# SeeStar AstroStat 2.0 by Gonhog
# A smart PowerShell utility that analyzes astrophotography session data from SeeStar S50 (or similar FIT/FITS datasets).
# It automatically scans _sub and _mosaic_sub folders, counts total frames, exposure times, and failed captures — then outputs a clean, color-coded summary with per-object and global statistics.
# Color refinement + cleaner summary
# ==============================

# Handle command line parameters
param(
    [switch]$Debug
)

# Set error action preference and encoding
$ErrorActionPreference = 'Stop'
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

# Enable detailed error information
$PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

# Set debug preference based on parameter
$DebugPreference = if ($Debug) { 'Continue' } else { 'SilentlyContinue' }

# Add debug logging function
function Write-DebugLog {
    param([string]$Message)
    if ($DebugPreference -ne 'SilentlyContinue') {
        $logMessage = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $Message"
        Write-Host $logMessage -ForegroundColor DarkGray
        Add-Content -Path "$PSScriptRoot\astrostats_debug.log" -Value $logMessage -ErrorAction SilentlyContinue
    }
}

# Get the script's directory
$root = $PSScriptRoot
Write-DebugLog "Script root directory: $root"
Write-DebugLog "Debug mode: $($DebugPreference -eq 'Continue')"

# Check if the directory exists
if (-not (Test-Path -Path $root)) {
    Write-Error "Directory not found: $root"
    exit 1
}

# Regex patterns
$stackPattern  = '^Stacked_(\d+)_(?:.+?)_(\d+\.?\d*)s'
$lightPattern  = '(?:^|_)(\d+\.?\d*)s(?:_|$)'
$failedPattern = '_failed_'

# Containers
$globalData = @{}
$totalFailed = 0
$totalFileSize = 0

Write-Host "`n=== SeeStar AstroStat 2.0 by Gonhog ===`n" -ForegroundColor Cyan

# Get all .fit files recursively, excluding 'other' and 'others' folders
Write-DebugLog "Searching for .fit files in: $root"
try {
    $allFitFiles = Get-ChildItem -Path $root -Filter *.fit -File -Recurse -ErrorAction Stop | 
        Where-Object { $_.FullName -notmatch '\\(other|others)\\' }
    Write-DebugLog "Found $($allFitFiles.Count) .fit files"
} catch {
    Write-Error "Error searching for .fit files: $_"
    exit 1
}

if ($allFitFiles.Count -eq 0) {
    Write-Host "No .fit files found in $root" -ForegroundColor Yellow
    exit 0
}

# Group files by their parent directory
$filesByDirectory = $allFitFiles | Group-Object -Property { $_.Directory.FullName }

foreach ($dirGroup in $filesByDirectory) {
    $path = $dirGroup.Name
    $folder = (Get-Item $path).Name
    
    # Use the full path as the base name to maintain folder structure
    $baseName = $path.Replace($root, '').Trim('\')
    
    # Check if this is a mosaic or regular sub folder
    $isMosaic = $folder -match '_mosaic_sub$'
    
    # Extract the base target name (without _sub or _mosaic_sub)
    $targetName = $baseName -replace '\\_mosaic_sub$|\\_sub$|_mosaic_sub$|_sub$', ''
    $targetName = $targetName.Trim()
    
    if (-not $globalData.ContainsKey($targetName)) {
        $globalData[$targetName] = @{
            sub = $null
            mosaic = $null
            path = $baseName
        }
    }

    # Collect data
    $data = @{
        Frames = 0
        Seconds = 0.0
        Failed = 0
        FileSize = 0
        Exposures = @{}
    }

    # Process all .fit files in this directory
    $dirGroup.Group | ForEach-Object {
        $file = $_.BaseName
        $data.FileSize += $_.Length
        if ($file -match $stackPattern) {
            $frames = [int]$matches[1]
            $exp = [double]$matches[2]
            $data.Frames += $frames
            $data.Seconds += ($frames * $exp)
            if (-not $data.Exposures.ContainsKey($exp)) { $data.Exposures[$exp] = 0 }
            $data.Exposures[$exp] += $frames
        }
        elseif ($file -match $lightPattern) {
            $exp = [double]$matches[1]
            if ($file -match $failedPattern) {
                $data.Failed++
                $totalFailed++
            } else {
                $data.Frames++
                $data.Seconds += $exp
                if (-not $data.Exposures.ContainsKey($exp)) { $data.Exposures[$exp] = 0 }
                $data.Exposures[$exp]++
            }
        }
    }

    if ($isMosaic) {
        $globalData[$targetName].mosaic = $data
    } else {
        $globalData[$targetName].sub = $data
    }
}

# ==== Output per object ====
$totalFrames = 0
$totalSeconds = 0.0

function Get-ColorForExp($exp) {
    switch ($exp) {
        10 { return 'Green' }       # 🟩
        20 { return 'Yellow' }      # 🟨
        30 { return 'DarkYellow' }  # 🟧
        default { return 'Cyan' }   # 🩵 (60s+)
    }
}

function Format-FolderOutput {
    param ($label, $info, $isSubfolder = $false, $isTopLevel = $false)
    $sec = $info.Seconds
    $hrs = $sec / 3600
    $summaryParts = @()
    $script:totalFileSize += $info.FileSize
    
    # Calculate the maximum label width for alignment
    $maxLabelWidth = 40
    $indent = if ($isSubfolder) { "    " } else { "" }
    $displayLabel = if ($isSubfolder) { "|-- $label" } else { $label }
    
    # Format the exposure parts
    foreach ($kv in ($info.Exposures.GetEnumerator() | Sort-Object Name)) {
        $exp = $kv.Key
        $count = $kv.Value
        $share = if ($sec -gt 0) { [math]::Round(($exp * $count / $sec) * 100) } else { 0 }
        $color = Get-ColorForExp $exp
        $part = ("{0}x{1}s {2}%" -f $count, $exp, $share)
        $summaryParts += @{ text = $part; color = $color }
    }

    # Build the output string
    $output = ("{0,-$maxLabelWidth} | {1,4} frames | {2,8:N0}s {3,6:N2}h | " -f $displayLabel, $info.Frames, $sec, $hrs)
    
    # Add the exposure parts with colors
    $first = $true
    foreach ($item in $summaryParts) {
        if (-not $first) { $output += ", " }
        $output += $item.text
        $first = $false
    }
    
    # Add failed count if any
    if ($info.Failed -gt 0) {
        $output += " Failed: $($info.Failed)"
    }
    
    # Output with appropriate color
    if ($isTopLevel) {
        Write-Host $indent -NoNewline
        Write-Host $displayLabel -ForegroundColor Magenta -NoNewline
        Write-Host $output.Substring($displayLabel.Length + $indent.Length)
    } else {
        Write-Host $indent$output
    }
}

# Group by first-level folder
$groupedData = @{}

# First pass: group by first-level folder
foreach ($key in $globalData.Keys) {
    $firstLevel = $key.Split('\')[0]
    if (-not $groupedData.ContainsKey($firstLevel)) {
        $groupedData[$firstLevel] = @()
    }
    $groupedData[$firstLevel] += @{
        key = $key
        data = $globalData[$key]
        isSubfolder = $key -ne $firstLevel
    }
}

# Second pass: output grouped by first-level folder
foreach ($firstLevel in ($groupedData.Keys | Sort-Object)) {
    $entries = $groupedData[$firstLevel]
    $hasMultiple = $entries.Count -gt 1
    
    if ($hasMultiple) {
        # Output main folder name with total
        Write-Host "$firstLevel" -ForegroundColor Magenta
        
        # Output each subfolder
        foreach ($entry in $entries) {
            $obj = $entry.data
            $key = $entry.key
            $isSubfolder = $entry.isSubfolder
            
            if ($obj.sub) {
                $displayName = $key.Replace("$firstLevel\", "")
                Format-FolderOutput $displayName $obj.sub -isSubfolder $true
                $totalFrames += $obj.sub.Frames
                $totalSeconds += $obj.sub.Seconds
            }
            if ($obj.mosaic) {
                $displayName = "$($key.Replace("$firstLevel\", '')) (mosaic)"
                Format-FolderOutput $displayName $obj.mosaic -isSubfolder $true
                $totalFrames += $obj.mosaic.Frames
                $totalSeconds += $obj.mosaic.Seconds
            }
        }
        Write-Host ""  # Add empty line between object groups
    } else {
        # Single entry for this object, output with top-level color
        $obj = $entries[0].data
        $key = $entries[0].key
        
        if ($obj.sub) {
            Format-FolderOutput $key $obj.sub -isTopLevel $true
            $totalFrames += $obj.sub.Frames
            $totalSeconds += $obj.sub.Seconds
        }
        if ($obj.mosaic) {
            $displayName = "$key (mosaic)"
            Format-FolderOutput $displayName $obj.mosaic -isTopLevel $true
            $totalFrames += $obj.mosaic.Frames
            $totalSeconds += $obj.mosaic.Seconds
        }
    }
}

# ==== Global summary ====
Write-Host "`n--------------------------------------------"
Write-Host "Global Summary:" -ForegroundColor Green
if ($totalFailed -gt 0) {
    Write-Host (" Total failed frames: {0}" -f $totalFailed)
}
Write-Host (" Total files: {0}" -f $allFitFiles.Count)
Write-Host (" Total exposure: {0}s | {1}min | {2:N2}h" -f ([int]$totalSeconds), ([int]($totalSeconds/60)), ($totalSeconds/3600))
Write-Host (" Total file size: {0:N2} GB" -f ($totalFileSize / 1GB))
Write-Host (" Unique objects: {0}" -f $globalData.Count)
Write-Host "--------------------------------------------`n"
Write-Host "Press Enter to close..."
Read-Host

