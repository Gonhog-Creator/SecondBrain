#!/usr/bin/env python3
import os
import re
import shutil

def better_categorize_file(filename, content):
    """Improved categorization for 'other' files"""
    filename_lower = filename.lower()
    
    # Research papers (prioritize these)
    if any(keyword in filename_lower for keyword in ['social construction', 'technology', 'probing transport', 's41467', 'brey', 'curington', 'volti', 'delaney', 'hutchby', 'earth future', 'bitcoin mining', 'graphene', 'biosensors']):
        return "research-paper"
    
    # Academic content that was misclassified
    if any(keyword in filename_lower for keyword in ['solution', 'exercise', 'review', 'direction', 'phase', 'substelim', 'worksheet', 'key']):
        return "academic-homework"
    
    if any(keyword in filename_lower for keyword in ['class-', 'lecture', 'notes', 'handout', 'ch223', 'ch225', 'che', 'mse', 'ne', 'eng', 'phi']):
        return "academic-lecture"
    
    if any(keyword in filename_lower for keyword in ['spectrophotometry', 'lab', 'experiment', 'turnitin']):
        return "academic-lab"
    
    if any(keyword in filename_lower for keyword in ['syllabus', 'instructions']):
        return "academic-syllabus"
    
    # Personal documents
    if any(keyword in filename_lower for keyword in ['biography', 'autobiography', 'artifact analysis', 'essay', 'reflection']):
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
    if any(keyword in filename_lower for keyword in ['preset', 'lightroom', 'camera']):
        return "delete"
    
    # Random hash files (delete these)
    if re.match(r'^[a-f0-9]{32}\.pdf$', filename_lower):
        return "delete"
    
    # Corrupted/empty files
    if len(content.strip()) < 50:
        return "delete"
    
    # Keep as other for now
    return "other"

def find_duplicates(junk_drawer):
    """Find duplicate files"""
    name_groups = {}
    for file in os.listdir(junk_drawer):
        if file.endswith('.pdf'):
            base_name = re.sub(r'\s*\(\d+\)\s*$', '', file)
            base_name = re.sub(r'\.pdf$', '', base_name)
            if base_name not in name_groups:
                name_groups[base_name] = []
            name_groups[base_name].append(file)
    
    duplicates = {k: v for k, v in name_groups.items() if len(v) > 1}
    return duplicates

def reorganize_files():
    junk_drawer = "junk_drawer"
    wiki_dir = "wiki"
    
    # Find duplicates
    duplicates = find_duplicates(junk_drawer)
    print(f"Found {len(duplicates)} duplicate groups")
    
    # Re-categorize all files
    reclassified = {}
    files_to_delete = []
    
    for file in os.listdir(junk_drawer):
        if file.endswith('.pdf'):
            txt_path = os.path.join(junk_drawer, file + '.txt')
            if os.path.exists(txt_path):
                try:
                    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    new_category = better_categorize_file(file, content)
                    
                    if new_category not in reclassified:
                        reclassified[new_category] = []
                    
                    reclassified[new_category].append(file)
                    
                    if new_category == "delete":
                        files_to_delete.append(file)
                except:
                    continue
    
    print("\n=== RECLASSIFICATION RESULTS ===")
    for category, files in sorted(reclassified.items()):
        print(f"{category}: {len(files)} files")
    
    print(f"\nFiles to delete: {len(files_to_delete)}")
    if files_to_delete:
        print("\nFiles marked for deletion:")
        for f in files_to_delete[:20]:
            print(f"  - {f}")
        if len(files_to_delete) > 20:
            print(f"  ... and {len(files_to_delete) - 20} more")
    
    return reclassified, files_to_delete, duplicates

if __name__ == "__main__":
    reclassified, files_to_delete, duplicates = reorganize_files()
