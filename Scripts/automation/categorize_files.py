#!/usr/bin/env python3
import os
import re

def categorize_file(filename, text_content):
    """Categorize a file based on filename and content"""
    filename_lower = filename.lower()
    
    # Check if file is essentially empty
    if len(text_content.strip()) < 50:
        return "empty"
    
    # Categorize by filename patterns
    if any(keyword in filename_lower for keyword in ['resume', 'cv', 'curriculum']):
        return "personal-resume"
    elif any(keyword in filename_lower for keyword in ['transcript', 'gpa', 'academic']):
        return "personal-academic"
    elif any(keyword in filename_lower for keyword in ['hw', 'homework', 'problem set', 'ps', 'worksheet']):
        return "academic-homework"
    elif any(keyword in filename_lower for keyword in ['syllabus', 'syllabi']):
        return "academic-syllabus"
    elif any(keyword in filename_lower for keyword in ['lecture', 'notes', 'handout', 'slide']):
        return "academic-lecture"
    elif any(keyword in filename_lower for keyword in ['lab', 'experiment', 'report']):
        return "academic-lab"
    elif any(keyword in filename_lower for keyword in ['exam', 'test', 'quiz', 'practice', 'final', 'midterm']):
        return "academic-exam"
    elif any(keyword in filename_lower for keyword in ['transcript', 'video']):
        return "media-transcript"
    elif any(keyword in filename_lower for keyword in ['cover letter', 'letter', 'application']):
        return "personal-application"
    elif any(keyword in filename_lower for keyword in ['sds', 'safety', 'data sheet']):
        return "technical-safety"
    elif any(keyword in filename_lower for keyword in ['contract', 'agreement', 'legal']):
        return "legal-document"
    elif any(keyword in filename_lower for keyword in ['invoice', 'tax', 'financial', '1099', 'portfolio']):
        return "financial-document"
    elif any(keyword in filename_lower for keyword in ['article', 'paper', 'research']):
        return "research-paper"
    else:
        return "other"

def process_all_files():
    junk_drawer = "junk_drawer"
    categories = {}
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.txt'):
                txt_path = os.path.join(root, file)
                pdf_path = txt_path.replace('.txt', '')
                
                try:
                    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    category = categorize_file(file, content)
                    
                    if category not in categories:
                        categories[category] = []
                    
                    categories[category].append({
                        'pdf': pdf_path,
                        'txt': txt_path,
                        'filename': file.replace('.txt', '')
                    })
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    
    return categories

if __name__ == "__main__":
    categories = process_all_files()
    
    print("File Categories:")
    print("=" * 50)
    for category, files in sorted(categories.items()):
        print(f"\n{category}: {len(files)} files")
        for f in files[:5]:  # Show first 5 files per category
            print(f"  - {f['filename']}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more")
    
    print(f"\nTotal categories: {len(categories)}")
    print(f"Total files: {sum(len(files) for files in categories.values())}")
