#!/usr/bin/env python3
import os
from pathlib import Path

def extract_text_from_file(file_path):
    """Extract text from code and documentation files"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except:
        try:
            with open(file_path, 'r', encoding='latin-1', errors='ignore') as f:
                return f.read()
        except:
            return ""

def process_github_files():
    github_dir = Path("junk_drawer/github")
    
    processed_count = 0
    error_count = 0
    
    for root, dirs, files in os.walk(github_dir):
        for file in files:
            file_path = Path(root) / file
            
            # Skip if already has .txt
            if file.endswith('.txt'):
                continue
            
            # Extract text
            content = extract_text_from_file(file_path)
            
            if content and len(content.strip()) > 10:
                txt_path = file_path.with_suffix(file_path.suffix + '.txt')
                try:
                    with open(txt_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    processed_count += 1
                except Exception as e:
                    error_count += 1
                    print(f"Error writing {txt_path}: {e}")
            else:
                error_count += 1
    
    print(f"Processed {processed_count} files")
    print(f"Errors: {error_count}")

if __name__ == "__main__":
    process_github_files()
