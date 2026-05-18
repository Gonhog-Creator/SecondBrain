#!/usr/bin/env python3
import os
import re
from collections import defaultdict

def extract_entities_from_content(content):
    """Extract potential entities from content"""
    entities = {
        'institutions': [],
        'technologies': [],
        'people': [],
        'concepts': []
    }
    
    # Institution patterns
    institution_patterns = [
        r'North Carolina State University',
        r'NCSU',
        r'Wolfspeed',
        r'Doble W Servicios',
        r'BEE Educated'
    ]
    
    # Technology patterns
    technology_patterns = [
        r'Silicon Carbide',
        r'SiC',
        r'Chemical Vapor Deposition',
        r'CVD',
        r'Statistical Process Control',
        r'SPC',
        r'Design of Experiment',
        r'DOE',
        r'LEAN',
        r'Measurement Systems Analysis',
        r'MSA',
        r'Fourier Transform Infrared Spectrometer'
    ]
    
    # Concept patterns
    concept_patterns = [
        r'Chemical Engineering',
        r'Material Science Engineering',
        r'Process Engineering',
        r'Process Change Review Boards',
        r'PCRB',
        r'Gauge Repeatability and Reproducibility',
        r'GR&R'
    ]
    
    for pattern in institution_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            entities['institutions'].append(pattern)
    
    for pattern in technology_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            entities['technologies'].append(pattern)
    
    for pattern in concept_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            entities['concepts'].append(pattern)
    
    return entities

def create_concept_page(concept_name, entity_type, related_files, wiki_dir):
    """Create a concept/entity page"""
    safe_name = concept_name.replace(' ', '-').replace('/', '-')
    filename = f"{safe_name}.md"
    path = os.path.join(wiki_dir, filename)
    
    content = f"""# {concept_name}

Type: [[{entity_type}]]

## Description
{concept_name} is a key concept/entity found across multiple documents in the knowledge base.

## Related Files

"""
    
    for file in related_files[:10]:  # Show first 10
        file_name = file.replace('.md', '')
        content += f"- [[{file_name}]]\n"
    
    if len(related_files) > 10:
        content += f"- ... and {len(related_files) - 10} more files\n"
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename

def analyze_and_create_concepts():
    """Analyze wiki files and create concept pages"""
    wiki_dir = "wiki"
    
    # Collect all entities from wiki files
    all_entities = defaultdict(list)
    
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            path = os.path.join(wiki_dir, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                entities = extract_entities_from_content(content)
                
                for entity_type, entity_list in entities.items():
                    for entity in entity_list:
                        all_entities[(entity, entity_type)].append(file)
            except:
                continue
    
    # Create concept pages for entities found in multiple files
    print("Creating concept pages...")
    created = 0
    
    for (entity, entity_type), files in all_entities.items():
        if len(files) >= 2:  # Only create pages for entities found in 2+ files
            try:
                filename = create_concept_page(entity, entity_type, files, wiki_dir)
                print(f"Created: {filename} ({len(files)} references)")
                created += 1
            except:
                continue
    
    print(f"\nCreated {created} concept pages")

if __name__ == "__main__":
    analyze_and_create_concepts()
