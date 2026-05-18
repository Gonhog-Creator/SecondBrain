#!/usr/bin/env python3
import os
import re

def rename_merged_pdfs():
    junk_drawer = "junk_drawer"
    renamed_count = 0
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            # Look for merged PDF patterns
            if re.match(r'.*\d{4}-\d{2}-\d{2}.*merged.*\.pdf$', file):
                old_path = os.path.join(root, file)
                txt_path = old_path + '.txt'
                
                # Remove the date and merged indicator
                new_name = re.sub(r'\d{4}-\d{2}-\d{2}.*?merged', 'merged', file)
                new_name = re.sub(r'-+', '-', new_name)  # Clean up multiple dashes
                new_name = new_name.strip('-')
                
                new_path = os.path.join(root, new_name)
                new_txt_path = new_path + '.txt'
                
                try:
                    if os.path.exists(old_path):
                        os.rename(old_path, new_path)
                        renamed_count += 1
                        print(f"Renamed: {file} -> {new_name}")
                    
                    if os.path.exists(txt_path):
                        os.rename(txt_path, new_txt_path)
                except Exception as e:
                    print(f"Error renaming {file}: {e}")
    
    print(f"\nTotal renamed: {renamed_count} merged PDFs")

if __name__ == "__main__":
    rename_merged_pdfs()
