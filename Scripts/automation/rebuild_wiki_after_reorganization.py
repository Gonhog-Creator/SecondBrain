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
    lines = content.split('\n')
    summary = ""
    for line in lines[:10]:
        if line.strip():
            summary += line.strip() + " "
            if len(summary) > max_chars:
                break
    return summary.strip()[:max_chars]

def better_categorize_file(filename, content, path=None):
    """Improved categorization for better organization"""
    filename_lower = filename.lower()
    path_lower = path.lower() if path else ""
    
    # GitHub code files
    if 'github' in path_lower or 'github' in filename_lower:
        return "github-code"
    
    # Corrupted/empty - check first
    if len(content.strip()) < 50:
        return "delete"
    
    # Video transcripts
    if any(keyword in filename_lower for keyword in ['video-transcript', 'video', 'transcript', 'ozempic', 'marques brownlee', 'crack']):
        return "media-transcript"
    
    # Work - Wolfspeed specific
    if any(keyword in filename_lower for keyword in ['wolfspeed', 'c-zero']):
        return "work-wolfspeed"
    
    # Work - DeltaV/ASP specific
    if any(keyword in filename_lower for keyword in ['delta v', 'deltav', 'para rf', 'asp', 'delta v international', 'deltav international']):
        return "work-deltav"
    
    # Work - general job application materials
    if any(keyword in filename_lower for keyword in ['cover letter', 'offer letter', 'resume', 'cv', 'background check', 'admission letter', 'rec letter', 'biosketch']):
        return "work-general"
    
    # Work - personal academic papers from work
    if any(keyword in filename_lower for keyword in ['critique', 'term paper', 'phi paper', 'jose barbeito', 'jose maria barbeito']):
        return "work-academic"
    
    # Business/company documents
    if any(keyword in filename_lower for keyword in ['company summary', 'company', 'business', 'completed form', 'senior design']):
        return "business-document"
    
    # Research papers (more specific)
    if any(keyword in filename_lower for keyword in ['probing transport', 's41467', 'neutron', 'x-ray', 'tomography', 'graphene', 'biosensors', 'bitcoin mining', 'social construction', 'theorizing technology']):
        return "research-paper"
    
    # Philosophy/ethics papers
    if any(keyword in filename_lower for keyword in ['susan wolf', 'moral saints', 'meditations', 'philosophy', 'ethics', 'utilitarianism']):
        return "academic-paper"
    
    # Academic papers/essays
    if any(keyword in filename_lower for keyword in ['rodriguez', 'mother', 'photographs', 'ford lynch', 'thesis', 'master', 'essay', 'artifact analysis']):
        return "academic-paper"
    
    # Textbooks and course materials
    if any(keyword in filename_lower for keyword in ['textbook', 'materials-textbook', 'understanding process dynamics', 'aiaa template', 'chemical reactions', 'chemical reactors', 'liberty equality power', 'organic chemistry']):
        return "textbook"
    
    # Lab reports and lab materials
    if any(keyword in filename_lower for keyword in ['lab report', 'lab#', 'lab ', 'temperature control', 'heat exchanger', 'batch distillation', 'film cooling', 'elastic deformation', 'exp2_nmr', 'beer law', 'calibration', 'worksheet', 'ws', 'pulstar', 'reactor', 'power defect']):
        return "academic-lab"
    
    # ChE312 course materials
    if any(keyword in filename_lower for keyword in ['che312', 'ch312', 'distillation', 'mass transfer', 'diffusivities']):
        return "academic-lecture"
    
    # Legal documents
    if any(keyword in filename_lower for keyword in ['team contract', 'rubric', 'agreement', 'articles of organization', 'attachment']):
        return "legal-document"
    
    # Personal documents
    if any(keyword in filename_lower for keyword in ['personal', 'biography', 'autobiography', 'iceland itinerary', 'things i learned', 'percorso']):
        return "personal-document"
    
    # Technical data sheets
    if any(keyword in filename_lower for keyword in ['data sheet', 'technical', 'sds', 'safety', 'mss']):
        return "technical-safety"
    
    # Financial documents
    if any(keyword in filename_lower for keyword in ['coinbase', 'gain.loss', 'financial', 'portfolio', '1098', 'tax', 'benefits']):
        return "financial-document"
    
    # Academic homework/solutions/handouts
    if any(keyword in filename_lower for keyword in ['solution', 'hw', 'homework', 'problem set', 'practice', 'exam', 'final', 'quiz', 'test', 'ps', 'ho', 'sample midterm', 'sample final']):
        return "academic-homework"
    
    # Academic lectures/notes
    if any(keyword in filename_lower for keyword in ['lecture', 'notes', 'handout', 'chapter', 'topic', 'review', 'class-']):
        return "academic-lecture"
    
    # Academic syllabus
    if any(keyword in filename_lower for keyword in ['syllabus', 'instructions']):
        return "academic-syllabus"
    
    # Date-based documents (likely miscategorized)
    if re.match(r'^_\d{2}_\d{2}_\d{4}', filename_lower):
        return "delete"
    
    # Keep as other for truly miscellaneous
    return "other"

def rebuild_wiki():
    junk_drawer = "junk_drawer"
    wiki_dir = "wiki"
    
    # Clear existing wiki files (except index.md, log.md, and concept pages)
    print("Clearing old wiki pages...")
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            # Keep concept pages (they don't have spaces or special chars usually)
            if '-' not in file or file in ['inbox-template.md', 'inbox-sync-conflict.md']:
                os.remove(os.path.join(wiki_dir, file))
    
    # Rebuild wiki pages with new categorization
    categories = {}
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            # Process PDF files with extracted text
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                txt_path = pdf_path + '.txt'
                if os.path.exists(txt_path):
                    try:
                        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        category = better_categorize_file(file, content, root)
                        
                        if category not in categories:
                            categories[category] = []
                        
                        categories[category].append({
                            'pdf': pdf_path,
                            'txt': txt_path,
                            'filename': file
                        })
                    except Exception as e:
                        print(f"Error processing {file}: {e}")
            
            # Process GitHub code files with .txt extensions
            elif file.endswith('.txt') and 'github' in root.lower():
                txt_path = os.path.join(root, file)
                original_file = file.replace('.txt', '')
                
                try:
                    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    category = better_categorize_file(file, content, root)
                    
                    if category not in categories:
                        categories[category] = []
                    
                    categories[category].append({
                        'pdf': txt_path,
                        'txt': txt_path,
                        'filename': original_file
                    })
                except Exception as e:
                    print(f"Error processing GitHub file {file}: {e}")
    
    # Create category pages
    print("Creating category pages...")
    for category, files in categories.items():
        filename = f"{category}.md"
        path = os.path.join(wiki_dir, filename)
        
        content = f"""# {category}

Category page for {len(files)} files.

## Files in this category

"""
        
        for f in files:
            safe_name = sanitize_filename(f['filename'])
            content += f"- [[{safe_name}]]\n"
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  Created: {category}.md ({len(files)} files)")
    
    # Create individual wiki pages
    print("\nCreating individual wiki pages...")
    total_created = 0
    
    for category, files in categories.items():
        print(f"  Processing {category}: {len(files)} files")
        for i, file_info in enumerate(files, 1):
            try:
                with open(file_info['txt'], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                summary = create_summary_from_content(content)
                wiki_filename = sanitize_filename(file_info['filename']) + ".md"
                wiki_path = os.path.join(wiki_dir, wiki_filename)
                
                wiki_content = f"""# {file_info['filename']}

Source: {file_info['pdf']}

Category: [[{category}]]

## Summary
{summary}

## Full Content
{content}

## Metadata
- Source file: {file_info['pdf']}
- Extracted: {datetime.now().strftime('%Y-%m-%d')}
- Category: {category}
"""
                
                with open(wiki_path, 'w', encoding='utf-8') as f:
                    f.write(wiki_content)
                
                total_created += 1
                if i % 50 == 0:
                    print(f"    Created {i}/{len(files)} pages...")
            except Exception as e:
                print(f"    Error creating page for {file_info['filename']}: {e}")
    
    print(f"\nDone! Created {total_created} wiki pages across {len(categories)} categories")
    return categories, total_created

if __name__ == "__main__":
    categories, total = rebuild_wiki()
