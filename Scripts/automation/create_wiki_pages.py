#!/usr/bin/env python3
import os
import re
from datetime import datetime

def sanitize_filename(filename):
    remove_chars = '[](){}<>:"/\\|?*'
    for char in remove_chars:
        filename = filename.replace(char, '')
    return filename.strip()

def create_summary_from_content(content, max_chars=500):
    """Extract a summary from content"""
    # Take first few lines or paragraphs
    lines = content.split('\n')
    summary = ""
    for line in lines[:10]:
        if line.strip():
            summary += line.strip() + " "
            if len(summary) > max_chars:
                break
    return summary.strip()[:max_chars]

def create_wiki_page(file_info, category, wiki_dir):
    """Create a wiki page for a single file"""
    pdf_path = file_info['pdf']
    txt_path = file_info['txt']
    filename = file_info['filename']
    
    # Read content
    try:
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return None
    
    # Create summary
    summary = create_summary_from_content(content)
    
    # Generate wiki filename
    wiki_filename = sanitize_filename(filename) + ".md"
    wiki_path = os.path.join(wiki_dir, wiki_filename)
    
    # Create wiki content
    wiki_content = f"""# {filename}

Source: {pdf_path}

Category: [[{category}]]

## Summary
{summary}

## Full Content
{content}

## Metadata
- Source file: {pdf_path}
- Extracted: {datetime.now().strftime('%Y-%m-%d')}
- Category: {category}
"""
    
    # Write wiki page
    with open(wiki_path, 'w', encoding='utf-8') as f:
        f.write(wiki_content)
    
    return wiki_filename

def create_category_page(category_name, file_count, wiki_dir):
    """Create a category page"""
    filename = f"{category_name}.md"
    path = os.path.join(wiki_dir, filename)
    
    content = f"""# {category_name}

Category page for {file_count} files.

## Files in this category

"""
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename

def process_all_categories():
    """Process all categories and create wiki pages"""
    junk_drawer = "junk_drawer"
    wiki_dir = "wiki"
    
    # Re-run categorization
    categories = {}
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.txt'):
                txt_path = os.path.join(root, file)
                pdf_path = txt_path.replace('.txt', '')
                
                try:
                    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Simple categorization (same as before)
                    filename_lower = file.lower()
                    if len(content.strip()) < 50:
                        category = "empty"
                    elif any(keyword in filename_lower for keyword in ['resume', 'cv', 'curriculum']):
                        category = "personal-resume"
                    elif any(keyword in filename_lower for keyword in ['transcript', 'gpa', 'academic']):
                        category = "personal-academic"
                    elif any(keyword in filename_lower for keyword in ['hw', 'homework', 'problem set', 'ps', 'worksheet']):
                        category = "academic-homework"
                    elif any(keyword in filename_lower for keyword in ['syllabus', 'syllabi']):
                        category = "academic-syllabus"
                    elif any(keyword in filename_lower for keyword in ['lecture', 'notes', 'handout', 'slide']):
                        category = "academic-lecture"
                    elif any(keyword in filename_lower for keyword in ['lab', 'experiment', 'report']):
                        category = "academic-lab"
                    elif any(keyword in filename_lower for keyword in ['exam', 'test', 'quiz', 'practice', 'final', 'midterm']):
                        category = "academic-exam"
                    elif any(keyword in filename_lower for keyword in ['transcript', 'video']):
                        category = "media-transcript"
                    elif any(keyword in filename_lower for keyword in ['cover letter', 'letter', 'application']):
                        category = "personal-application"
                    elif any(keyword in filename_lower for keyword in ['sds', 'safety', 'data sheet']):
                        category = "technical-safety"
                    elif any(keyword in filename_lower for keyword in ['contract', 'agreement', 'legal']):
                        category = "legal-document"
                    elif any(keyword in filename_lower for keyword in ['invoice', 'tax', 'financial', '1099', 'portfolio']):
                        category = "financial-document"
                    elif any(keyword in filename_lower for keyword in ['article', 'paper', 'research']):
                        category = "research-paper"
                    else:
                        category = "other"
                    
                    if category not in categories:
                        categories[category] = []
                    
                    categories[category].append({
                        'pdf': pdf_path,
                        'txt': txt_path,
                        'filename': file.replace('.txt', '')
                    })
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    
    # Create category pages
    print("Creating category pages...")
    for category, files in categories.items():
        if category != "empty":  # Skip empty files
            create_category_page(category, len(files), wiki_dir)
            print(f"Created category page: {category}")
    
    # Create individual wiki pages (skip empty files)
    print("\nCreating individual wiki pages...")
    total_processed = 0
    for category, files in categories.items():
        if category == "empty":
            continue
        
        print(f"\nProcessing category: {category} ({len(files)} files)")
        for i, file_info in enumerate(files, 1):  # Process ALL files
            wiki_filename = create_wiki_page(file_info, category, wiki_dir)
            if wiki_filename:
                total_processed += 1
                if i % 10 == 0:
                    print(f"  Processed {i}/{len(files)} files...")
    
    print(f"\nDone! Created {total_processed} wiki pages across {len(categories)-1} categories")

if __name__ == "__main__":
    process_all_categories()
