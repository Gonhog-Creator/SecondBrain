#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# File extensions to process (code and documentation)
CODE_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h', '.cs', '.go', 
    '.rs', '.rb', '.php', '.swift', '.kt', '.scala', '.dart', '.lua', '.r', '.m',
    '.sh', '.bash', '.zsh', '.ps1', '.bat', '.cmd', '.sql', '.html', '.css', '.scss',
    '.sass', '.less', '.json', '.yaml', '.yml', '.xml', '.toml', '.ini', '.cfg', '.conf',
    '.md', '.markdown', '.rst', '.txt', '.readme', '.license', '.gitignore', '.dockerfile'
}

# File extensions to exclude (images, binaries, etc.)
EXCLUDE_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico', '.webp', '.tiff',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip', '.tar', '.gz',
    '.rar', '.7z', '.exe', '.dll', '.so', '.dylib', '.a', '.lib', '.o', '.obj',
    '.mp3', '.mp4', '.avi', '.mov', '.wav', '.flac', '.ogg', '.wma', '.m4a', '.m4v',
    '.ttf', '.otf', '.woff', '.woff2', '.eot', '.pem', '.crt', '.key', '.p12', '.pfx'
}

# Directories to exclude
EXCLUDE_DIRS = {
    'node_modules', '__pycache__', '.git', '.vscode', '.idea', 'venv', 'env', 
    'dist', 'build', 'target', 'bin', 'obj', '.next', '.nuxt', 'coverage',
    '.pytest_cache', '.mypy_cache', 'vendor', 'bower_components', '.gradle'
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def should_process_file(file_path):
    """Check if file should be processed"""
    ext = file_path.suffix.lower()
    
    # Skip excluded extensions
    if ext in EXCLUDE_EXTENSIONS:
        return False
    
    # Only process code/documentation files
    if ext not in CODE_EXTENSIONS:
        return False
    
    # Skip large files
    try:
        if file_path.stat().st_size > MAX_FILE_SIZE:
            return False
    except:
        return False
    
    return True

def should_process_dir(dir_path):
    """Check if directory should be processed"""
    dir_name = dir_path.name
    return dir_name not in EXCLUDE_DIRS and not dir_name.startswith('.')

def process_github_repos():
    source_dir = Path("temp_github_clone")
    target_dir = Path("junk_drawer/github")
    
    # Create target directory
    target_dir.mkdir(exist_ok=True)
    
    processed_files = 0
    skipped_files = 0
    skipped_large = 0
    skipped_images = 0
    
    for repo_dir in source_dir.iterdir():
        if not repo_dir.is_dir():
            continue
        
        repo_name = repo_dir.name
        print(f"Processing repository: {repo_name}")
        
        # Create repository subdirectory
        repo_target = target_dir / repo_name
        repo_target.mkdir(exist_ok=True)
        
        # Walk through repository
        for root, dirs, files in os.walk(repo_dir):
            root_path = Path(root)
            
            # Filter directories in-place
            dirs[:] = [d for d in dirs if should_process_dir(Path(d))]
            
            for file in files:
                file_path = root_path / file
                
                if not should_process_file(file_path):
                    if file_path.suffix.lower() in EXCLUDE_EXTENSIONS:
                        skipped_images += 1
                    else:
                        skipped_files += 1
                    
                    # Check if it's a large file
                    try:
                        if file_path.stat().st_size > MAX_FILE_SIZE:
                            skipped_large += 1
                    except:
                        pass
                    
                    continue
                
                # Create relative path
                rel_path = file_path.relative_to(repo_dir)
                target_file = repo_target / rel_path
                
                # Create parent directories
                target_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy file
                try:
                    shutil.copy2(file_path, target_file)
                    processed_files += 1
                except Exception as e:
                    print(f"Error copying {file_path}: {e}")
    
    print(f"\nProcessing complete:")
    print(f"Processed files: {processed_files}")
    print(f"Skipped images/binaries: {skipped_images}")
    print(f"Skipped large files (>5MB): {skipped_large}")
    print(f"Skipped other files: {skipped_files}")
    print(f"Total repositories processed: {len(list(source_dir.iterdir()))}")

if __name__ == "__main__":
    process_github_repos()
