#!/usr/bin/env python3
import os
import re

def better_categorize_file(filename, content):
    """Improved categorization for better organization"""
    filename_lower = filename.lower()
    
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

def analyze_other_category():
    junk_drawer = "junk_drawer"
    
    categories = {}
    
    for root, dirs, files in os.walk(junk_drawer):
        for file in files:
            if file.endswith('.pdf'):
                txt_path = os.path.join(root, file + '.txt')
                if os.path.exists(txt_path):
                    try:
                        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        category = better_categorize_file(file, content)
                        
                        if category not in categories:
                            categories[category] = []
                        
                        categories[category].append(file)
                    except:
                        continue
    
    print("Improved categorization results:")
    print("=" * 50)
    for category, files in sorted(categories.items()):
        print(f"{category}: {len(files)} files")
    
    return categories

if __name__ == "__main__":
    analyze_other_category()
