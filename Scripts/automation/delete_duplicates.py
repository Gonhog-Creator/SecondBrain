#!/usr/bin/env python3
import os
import re

def find_and_delete_duplicates():
    junk_drawer = "junk_drawer"
    deleted_count = 0
    kept_count = 0
    
    # Group files by base name (remove version indicators)
    file_groups = {}
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.pdf'):
                # Remove version indicators like " 1", " 2", " (1)", etc.
                base_name = re.sub(r'\s*\(\d+\)\s*$', '', file)
                base_name = re.sub(r'\s+\d+\s*$', '', base_name)
                base_name = re.sub(r'\.pdf$', '', base_name)
                
                if base_name not in file_groups:
                    file_groups[base_name] = []
                
                file_groups[base_name].append({
                    'full_name': file,
                    'path': os.path.join(root, file),
                    'txt_path': os.path.join(root, file + '.txt')
                })
    
    # For each group, keep the latest version (highest number) or the one without number
    for base_name, files in file_groups.items():
        if len(files) > 1:
            # Sort by version number, keep highest
            files.sort(key=lambda x: x['full_name'])
            
            # Keep the last one (highest version)
            to_keep = files[-1]
            to_delete = files[:-1]
            
            for f in to_delete:
                try:
                    if os.path.exists(f['path']):
                        os.remove(f['path'])
                        deleted_count += 1
                        print(f"Deleted duplicate: {f['full_name']}")
                    if os.path.exists(f['txt_path']):
                        os.remove(f['txt_path'])
                except Exception as e:
                    print(f"Error deleting {f['full_name']}: {e}")
            
            kept_count += 1
            print(f"Kept: {to_keep['full_name']}")
    
    print(f"\nTotal deleted: {deleted_count} duplicate files")
    print(f"Total kept: {kept_count} unique files")

if __name__ == "__main__":
    find_and_delete_duplicates()
