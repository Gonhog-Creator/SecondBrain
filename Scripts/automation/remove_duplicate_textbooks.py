#!/usr/bin/env python3
import os
import hashlib
from pathlib import Path

def get_file_hash(file_path):
    """Calculate MD5 hash of file"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except:
        return None

def remove_duplicate_textbooks():
    junk_drawer = Path("junk_drawer")
    
    # Known duplicates to remove (keep the first one, delete the rest)
    duplicates_to_remove = [
        # Materials-Textbook-8th-Edition (keep one, remove 3 duplicates)
        "Materials-Textbook-8th-Edition (1).pdf",
        "Materials-Textbook-8th-Edition (2).pdf", 
        "Materials-Textbook-8th-Edition (3).pdf",
        "Materials-Textbook-8th-Edition (4).pdf",
        # Chemical Reactions and Chemical Reactors (keep one, remove duplicate)
        "George W. Roberts - Chemical Reactions and Chemical Reactors (2008, Wiley) - libgen.li_compressed.pdf",
        # Transport Processes (keep one, remove duplicate)
        "Christie_John_Geankoplis__A._Allen_Hersel__Daniel_H._Lepek_-_Transport_Processes_and_Separation_Process_Principles-Prentice_Hall_2018Z-Lib.io (1).pdf",
        # Understanding Process Dynamics (keep one, remove duplicate)
        "Understanding Process Dynamics and Control -- Costas Kravaris, Ioannis K_ Kookos -- Cambridge University Press, 2021, 1, 2021 -- Cambridge University -- 9781107035584 -- 7b45c62ee2fb81b8284df6654e818dcf -- Anna (1).pdf",
    ]
    
    deleted_count = 0
    saved_space = 0
    
    for filename in duplicates_to_remove:
        file_path = junk_drawer / filename
        txt_path = junk_drawer / (filename + ".txt")
        
        if file_path.exists():
            try:
                file_size = file_path.stat().st_size
                os.remove(file_path)
                deleted_count += 1
                saved_space += file_size
                print(f"Deleted: {filename} ({file_size / (1024*1024):.1f}M)")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
        
        if txt_path.exists():
            try:
                os.remove(txt_path)
            except Exception as e:
                print(f"Error deleting {txt_path}: {e}")
    
    print(f"\nDeleted {deleted_count} duplicate textbooks")
    print(f"Saved {saved_space / (1024*1024):.1f}M of space")

if __name__ == "__main__":
    remove_duplicate_textbooks()
