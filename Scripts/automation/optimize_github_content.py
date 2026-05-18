#!/usr/bin/env python3
import os
from pathlib import Path

# Files to exclude (build artifacts, cache files, etc.)
EXCLUDE_FILES = {
    'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml',
    'gradlew', 'gradlew.bat', 'build.gradle', 'build.gradle.kts',
    'pom.xml', 'mvnw', 'mvnw.cmd',
    'usercache.json', 'usernamecache.json',
    '.DS_Store', 'Thumbs.db',
    'robots.txt', 'sitemap.xml'
}

# Directories to exclude
EXCLUDE_DIRS = {
    'node_modules', '__pycache__', '.git', '.next', '.nuxt', 'dist', 'build',
    'target', 'bin', 'obj', 'coverage', '.pytest_cache', '.mypy_cache',
    'vendor', 'bower_components', '.gradle', 'run', 'cache'
}

def should_exclude_file(filename):
    """Check if file should be excluded"""
    return filename in EXCLUDE_FILES

def should_exclude_dir(dirname):
    """Check if directory should be excluded"""
    return dirname in EXCLUDE_DIRS or dirname.startswith('.')

def optimize_github_content():
    github_dir = Path("junk_drawer/github")
    
    deleted_count = 0
    kept_count = 0
    
    for root, dirs, files in os.walk(github_dir):
        root_path = Path(root)
        
        # Filter directories in-place
        dirs[:] = [d for d in dirs if not should_exclude_dir(d)]
        
        for file in files:
            file_path = root_path / file
            
            # Check if file should be excluded
            if should_exclude_file(file):
                try:
                    # Remove both the file and its .txt version
                    if file_path.exists():
                        os.remove(file_path)
                        deleted_count += 1
                        print(f"Deleted: {file_path}")
                    
                    txt_path = file_path.with_suffix(file_path.suffix + '.txt')
                    if txt_path.exists():
                        os.remove(txt_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            else:
                kept_count += 1
    
    print(f"\nOptimization complete:")
    print(f"Deleted: {deleted_count} build/cache files")
    print(f"Kept: {kept_count} source files")

if __name__ == "__main__":
    optimize_github_content()
