#!/usr/bin/env python3
import os
import sys
import subprocess
import re

def extract_text_from_pdf(pdf_path):
    try:
        output_path = pdf_path + ".txt"
        result = subprocess.run(['pdftotext', pdf_path, output_path], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            with open(output_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return f"Error converting PDF: {result.stderr}"
    except Exception as e:
        return f"Error reading PDF: {e}"

def sanitize_filename(filename):
    remove_chars = '[](){}<>:"/\\|?*'
    for char in remove_chars:
        filename = filename.replace(char, '')
    return filename.strip()

def process_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    txt_path = pdf_path + ".txt"
    return txt_path

if __name__ == "__main__":
    junk_drawer = "junk_drawer"
    
    pdf_files = []
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    
    print(f"Found {len(pdf_files)} PDF files")
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"Processing {i}/{len(pdf_files)}: {os.path.basename(pdf_path)}")
        process_pdf(pdf_path)
    
    print(f"Done! Extracted text to .txt files alongside PDFs")
