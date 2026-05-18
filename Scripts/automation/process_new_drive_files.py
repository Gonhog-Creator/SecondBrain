#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

def extract_text_from_pdf(pdf_path):
    try:
        output_path = pdf_path + ".txt"
        result = subprocess.run(['pdftotext', pdf_path, output_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            print(f"Error converting {pdf_path}: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return False

def find_new_pdfs(junk_drawer):
    """Find PDFs that don't have corresponding .txt files"""
    new_pdfs = []
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                txt_path = pdf_path + ".txt"
                
                if not os.path.exists(txt_path):
                    new_pdfs.append(pdf_path)
    
    return new_pdfs

def process_new_files():
    junk_drawer = "junk_drawer"
    
    # Find new PDFs
    new_pdfs = find_new_pdfs(junk_drawer)
    print(f"Found {len(new_pdfs)} new PDFs to process")
    
    if not new_pdfs:
        print("No new PDFs to process")
        return
    
    # Extract text from new PDFs
    print("Extracting text from new PDFs...")
    success_count = 0
    for i, pdf_path in enumerate(new_pdfs, 1):
        print(f"  Processing {i}/{len(new_pdfs)}: {os.path.basename(pdf_path)}")
        if extract_text_from_pdf(pdf_path):
            success_count += 1
    
    print(f"Successfully extracted text from {success_count}/{len(new_pdfs)} PDFs")

if __name__ == "__main__":
    process_new_files()
