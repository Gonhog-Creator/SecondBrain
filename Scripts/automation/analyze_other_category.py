#!/usr/bin/env python3
import os
import re

def analyze_other_category():
    """Analyze files in the 'other' category"""
    junk_drawer = "junk_drawer"
    
    other_files = []
    
    for file in os.listdir(junk_drawer):
        if file.endswith('.pdf'):
            txt_path = os.path.join(junk_drawer, file + '.txt')
            if os.path.exists(txt_path):
                try:
                    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Check if it would be categorized as "other"
                    filename_lower = file.lower()
                    
                    if len(content.strip()) < 50:
                        continue  # Skip empty files
                    
                    is_other = True
                    if any(keyword in filename_lower for keyword in ['resume', 'cv', 'curriculum']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['transcript', 'gpa', 'academic']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['hw', 'homework', 'problem set', 'ps', 'worksheet']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['syllabus', 'syllabi']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['lecture', 'notes', 'handout', 'slide']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['lab', 'experiment', 'report']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['exam', 'test', 'quiz', 'practice', 'final', 'midterm']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['transcript', 'video']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['cover letter', 'letter', 'application']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['sds', 'safety', 'data sheet']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['contract', 'agreement', 'legal']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['invoice', 'tax', 'financial', '1099', 'portfolio']):
                        is_other = False
                    elif any(keyword in filename_lower for keyword in ['article', 'paper', 'research']):
                        is_other = False
                    
                    if is_other:
                        other_files.append({
                            'filename': file,
                            'content': content,
                            'size': len(content)
                        })
                except:
                    continue
    
    # Analyze patterns
    print(f"Found {len(other_files)} files in 'other' category")
    print("\n=== SAMPLE FILES ===")
    for f in other_files[:20]:
        print(f"\n{f['filename']}")
        print(f"  Size: {f['size']} chars")
        print(f"  Preview: {f['content'][:200]}...")
    
    # Identify patterns
    print("\n=== PATTERN ANALYSIS ===")
    
    # Check for duplicates (files with similar names)
    name_groups = {}
    for f in other_files:
        base_name = re.sub(r'\s*\(\d+\)\s*\.pdf$', '', f['filename'])
        base_name = re.sub(r'\.pdf$', '', base_name)
        if base_name not in name_groups:
            name_groups[base_name] = []
        name_groups[base_name].append(f['filename'])
    
    duplicates = {k: v for k, v in name_groups.items() if len(v) > 1}
    print(f"\nPotential duplicates: {len(duplicates)} groups")
    for name, files in list(duplicates.items())[:10]:
        print(f"  {name}: {len(files)} files")
    
    # Check for date-based files
    date_files = [f for f in other_files if re.match(r'\d{4}-\d{2}-\d{2}', f['filename'])]
    print(f"\nDate-based files: {len(date_files)}")
    
    # Check for course codes
    course_files = [f for f in other_files if re.search(r'[A-Z]{2,4}\s*\d{3,4}', f['filename'])]
    print(f"\nCourse code files: {len(course_files)}")
    
    # Check for chapter-based files
    chapter_files = [f for f in other_files if re.search(r'[Cc]hapter\s*\d+', f['filename'])]
    print(f"\nChapter files: {len(chapter_files)}")
    
    return other_files, duplicates, date_files, course_files, chapter_files

if __name__ == "__main__":
    analyze_other_category()
