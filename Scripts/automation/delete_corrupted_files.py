#!/usr/bin/env python3
import os

def delete_corrupted_files():
    junk_drawer = "junk_drawer"
    deleted_count = 0
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.pdf'):
                txt_path = os.path.join(root, file + '.txt')
                if os.path.exists(txt_path):
                    try:
                        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        if len(content.strip()) < 50:
                            pdf_path = os.path.join(root, file)
                            os.remove(pdf_path)
                            os.remove(txt_path)
                            deleted_count += 1
                            print(f"Deleted: {file}")
                    except Exception as e:
                        print(f"Error processing {file}: {e}")
    
    print(f"Total deleted: {deleted_count} files")

if __name__ == "__main__":
    delete_corrupted_files()
