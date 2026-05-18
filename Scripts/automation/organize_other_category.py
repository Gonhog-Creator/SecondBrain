#!/usr/bin/env python3
"""
Organize the 'other' category files into more specific categories.
Analyzes filenames and content to determine better categorization.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

WIKI_DIR = Path("/Users/josemariabarbeito/PycharmProjects/SecondBrain/wiki")
JUNK_DIR = Path("/Users/josemariabarbeito/PycharmProjects/SecondBrain/junk_drawer")

# Define categorization patterns
CATEGORIES = {
    'history-us-politics': {
        'patterns': [
            r'ww1', r'ww2', r'world war', r'korean war', r'cold war', r'gulf war',
            r'reagan', r'bush', r'immigration', r'progressives', r'empire',
            r'liberty.*equality', r'1920s', r'interwar', r'freedom summer'
        ],
        'description': 'US History and politics documents, wars, immigration, political movements'
    },
    'ballistics-armor': {
        'patterns': [
            r'ballistic', r'armor', r'kevlar', r'nij', r'argentina.*rb',
            r'chaleco', r'placa.*rb', r'pad', r'tyvek', r'stop iii',
            r'body.*armor', r'protection.*research', r'soldier.*monitoring'
        ],
        'description': 'Ballistics research, body armor standards, protection materials'
    },
    'job-application': {
        'patterns': [
            r'cover.?letter', r'offer.?letter', r'jd', r'job description',
            r'assembly technician', r'solicitation', r'degree audit',
            r'barbeito.*jose', r'articles?.*organization', r'ownership.*control',
            r'requirement.*report', r'beneficial ownership', r'taa form',
            r'team assessment', r'academic integrity'
        ],
        'description': 'Job applications, offer letters, resumes, career documents'
    },
    'chemical-engineering': {
        'patterns': [
            r'transport.*process', r'separation.*process', r'geankoplis',
            r'fluidized.?bed', r'chemical.*engineering', r'process.*dynamics',
            r'separation.*vandeemter', r'analytical.*separation'
        ],
        'description': 'Chemical engineering textbooks, transport phenomena, separation processes'
    },
    'lab-coursework': {
        'patterns': [
            r'lab.?manual', r'che 330', r'che 331', r'che 450', r'lab.?report',
            r'209_212', r'ne235', r'lect.*slides', r'formula sheet',
            r'differential.*equations', r'continuous.*variable',
            r'chart of nuclides', r'temperature.?control', r'effectiveness.?factor'
        ],
        'description': 'Lab manuals, coursework, assignments, lab reports'
    },
    'literature-humanities': {
        'patterns': [
            r'baldwin.*sonny', r'girl.*jamaica', r'kincaid', r'watson.*freedom',
            r'lopate.*yourself', r'joyce.*oates', r'virtual scrapbook',
            r'primary text.*rslm', r'religion.*science.*life', r'framework.*ethically',
            r'hutchby.*technologies'
        ],
        'description': 'Literature, humanities, ethics, philosophy readings'
    },
    'materials-science': {
        'patterns': [
            r'polymeric.*material', r'brazel', r'polymers.*young',
            r'material.*propert', r'magnetic.*propert',
            r'visco', r'bonding.*acid', r'substelim'
        ],
        'description': 'Materials science, polymers, material properties'
    },
    'physics-research': {
        'patterns': [
            r'probing.*transport', r'two.?dimensi', r'spm experiment',
            r'bertelli', r'hp water.*ink'
        ],
        'description': 'Physics research papers and experimental data'
    }
}

def categorize_file(filename):
    """Categorize a file based on its name."""
    filename_lower = filename.lower()
    
    for category, config in CATEGORIES.items():
        for pattern in config['patterns']:
            if re.search(pattern, filename_lower):
                return category
    
    return 'other'

def main():
    print("=" * 70)
    print("Organizing 'other' category files")
    print("=" * 70)
    print()
    
    # Read the other.md file to get the list
    other_file = WIKI_DIR / 'other.md'
    if not other_file.exists():
        print("Error: other.md not found")
        return
    
    with open(other_file, 'r') as f:
        content = f.read()
    
    # Extract filenames
    files = re.findall(r'\[\[([^\]]+)\]\]', content)
    
    print(f"Found {len(files)} files in 'other' category")
    print()
    
    # Categorize files
    categorized = defaultdict(list)
    for filename in files:
        category = categorize_file(filename)
        categorized[category].append(filename)
    
    # Print results
    for category, file_list in sorted(categorized.items()):
        if category == 'other':
            continue
        desc = CATEGORIES.get(category, {}).get('description', '')
        print(f"\n## {category} ({len(file_list)} files)")
        print(f"{desc}")
        print("-" * 50)
        for f in sorted(file_list)[:10]:  # Show first 10
            print(f"  - {f}")
        if len(file_list) > 10:
            print(f"  ... and {len(file_list) - 10} more")
    
    # Show remaining 'other' files
    other_files = categorized.get('other', [])
    print(f"\n\n## Remaining 'other' ({len(other_files)} files)")
    print("Files that don't match specific categories:")
    print("-" * 50)
    for f in sorted(other_files):
        print(f"  - {f}")
    
    print()
    print("=" * 70)
    print(f"Summary: {len(files) - len(other_files)} files categorized, {len(other_files)} remain in 'other'")
    print("=" * 70)
    
    # Generate category content
    print("\n\n# Proposed New Category Pages\n")
    
    for category, file_list in sorted(categorized.items()):
        if category == 'other' or not file_list:
            continue
        
        desc = CATEGORIES.get(category, {}).get('description', '')
        print(f"## {category}.md")
        print(f"""
# {category.replace('-', ' ').title()}

{desc}

## Files ({len(file_list)} total)
""")
        for f in sorted(file_list):
            print(f"- [[{f}]]")
        print()

if __name__ == "__main__":
    main()
