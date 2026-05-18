#!/usr/bin/env python3
import os
import re
import shutil

def better_categorize_file(filename, content):
    """Improved categorization for 'other' files"""
    filename_lower = filename.lower()
    
    # Research papers (prioritize these)
    if any(keyword in filename_lower for keyword in ['social construction', 'technology', 'probing transport', 's41467', 'brey', 'curington', 'volti', 'delaney', 'hutchby', 'earth future', 'bitcoin mining', 'graphene', 'biosensors', 'taking charge', 'freedom summer', 'watson', 'moral saints', 'susan wolf']):
        return "research-paper"
    
    # Academic content that was misclassified
    if any(keyword in filename_lower for keyword in ['solution', 'exercise', 'review', 'direction', 'phase', 'substelim', 'worksheet', 'key', 'hw', 'homework', 'problem set', 'ps']):
        return "academic-homework"
    
    if any(keyword in filename_lower for keyword in ['class-', 'lecture', 'notes', 'handout', 'ch223', 'ch225', 'che', 'mse', 'ne', 'eng', 'phi', 'chapter', 'topic']):
        return "academic-lecture"
    
    if any(keyword in filename_lower for keyword in ['spectrophotometry', 'lab', 'experiment', 'turnitin']):
        return "academic-lab"
    
    if any(keyword in filename_lower for keyword in ['syllabus', 'instructions']):
        return "academic-syllabus"
    
    # Personal documents
    if any(keyword in filename_lower for keyword in ['biography', 'autobiography', 'artifact analysis', 'essay', 'reflection', 'personal assessment']):
        return "personal-academic"
    
    # Technical documents
    if any(keyword in filename_lower for keyword in ['data sheet', 'technical', 'sds', 'safety']):
        return "technical-safety"
    
    # Financial documents
    if any(keyword in filename_lower for keyword in ['statement', 'bank', '1098', 'portfolio']):
        return "financial-document"
    
    # Personal documents
    if any(keyword in filename_lower for keyword in ['resume', 'cv']):
        return "personal-resume"
    
    # Gaming/entertainment (delete these)
    if any(keyword in filename_lower for keyword in ['skyfactory', 'minecraft', 'game']):
        return "delete"
    
    # Photography presets (delete these)
    if any(keyword in filename_lower for keyword in ['preset', 'lightroom', 'camera', 'night vibes']):
        return "delete"
    
    # Random hash files (delete these)
    if re.match(r'^[a-f0-9]{32}\.pdf$', filename_lower):
        return "delete"
    
    # Date-based files with no clear content (delete these)
    if re.match(r'^\d{4}-\d{2}-\d{2}', filename_lower) and len(content.strip()) < 100:
        return "delete"
    
    # Corrupted/empty files
    if len(content.strip()) < 50:
        return "delete"
    
    # Keep as other for now
    return "other"

def execute_reorganization():
    junk_drawer = "junk_drawer"
    wiki_dir = "wiki"
    
    files_deleted = []
    files_reclassified = {}
    
    for file in os.listdir(junk_drawer):
        if file.endswith('.pdf'):
            txt_path = os.path.join(junk_drawer, file + '.txt')
            if os.path.exists(txt_path):
                try:
                    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    new_category = better_categorize_file(file, content)
                    
                    if new_category == "delete":
                        # Delete PDF and text file
                        pdf_path = os.path.join(junk_drawer, file)
                        if os.path.exists(pdf_path):
                            os.remove(pdf_path)
                            files_deleted.append(file)
                        if os.path.exists(txt_path):
                            os.remove(txt_path)
                    else:
                        if new_category not in files_reclassified:
                            files_reclassified[new_category] = []
                        files_reclassified[new_category].append(file)
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    
    print(f"Deleted {len(files_deleted)} files")
    print(f"\nReclassified files:")
    for category, files in sorted(files_reclassified.items()):
        print(f"  {category}: {len(files)} files")
    
    return files_deleted, files_reclassified

if __name__ == "__main__":
    execute_reorganization()
