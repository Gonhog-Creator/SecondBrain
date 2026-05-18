#!/usr/bin/env python3
import os
import re

def delete_date_based_files():
    junk_drawer = "junk_drawer"
    deleted_count = 0
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.pdf'):
                # Check for date-based pattern _MM_DD_YYYY
                if re.match(r'^_\d{2}_\d{2}_\d{4}', file):
                    pdf_path = os.path.join(root, file)
                    txt_path = pdf_path + '.txt'
                    
                    try:
                        if os.path.exists(pdf_path):
                            os.remove(pdf_path)
                            deleted_count += 1
                            print(f"Deleted: {file}")
                        if os.path.exists(txt_path):
                            os.remove(txt_path)
                    except Exception as e:
                        print(f"Error deleting {file}: {e}")
    
    print(f"Total deleted: {deleted_count} date-based files")

if __name__ == "__main__":
    delete_date_based_files()
