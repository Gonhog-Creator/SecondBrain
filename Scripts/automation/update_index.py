#!/usr/bin/env python3
import os
from datetime import datetime

def update_index():
    wiki_dir = "wiki"
    index_path = os.path.join(wiki_dir, "index.md")
    
    # Get all markdown files in wiki
    wiki_files = []
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            wiki_files.append(file)
    
    wiki_files.sort()
    
    # Categorize files
    categories = {
        'Sources': [],
        'Categories': [],
        'Concepts': [],
        'Entities': []
    }
    
    for file in wiki_files:
        if file.endswith('.md'):
            if any(cat in file for cat in ['academic-', 'personal-', 'research-', 'technical-', 'legal-', 'financial-', 'media-']):
                categories['Sources'].append(file)
            elif file in ['inbox-template.md', 'inbox-sync-conflict.md']:
                categories['Sources'].append(file)
            else:
                categories['Categories'].append(file)
    
    # Update index.md
    content = """# Wiki Index

This is the catalog of everything in the wiki.

*Last updated: {}

## Categories

""".format(datetime.now().strftime('%Y-%m-%d %H:%M'))
    
    # Add category pages
    content += "### Category Pages\n"
    for file in categories['Categories']:
        name = file.replace('.md', '')
        content += f"- [[{name}]]\n"
    
    content += "\n"
    
    # Add source pages by category
    content += "### Source Pages\n\n"
    
    # Group by category
    academic_files = [f for f in categories['Sources'] if f.startswith('academic-')]
    personal_files = [f for f in categories['Sources'] if f.startswith('personal-')]
    research_files = [f for f in categories['Sources'] if f.startswith('research-')]
    technical_files = [f for f in categories['Sources'] if f.startswith('technical-')]
    legal_files = [f for f in categories['Sources'] if f.startswith('legal-')]
    financial_files = [f for f in categories['Sources'] if f.startswith('financial-')]
    media_files = [f for f in categories['Sources'] if f.startswith('media-')]
    other_files = [f for f in categories['Sources'] if not any(f.startswith(p) for p in ['academic-', 'personal-', 'research-', 'technical-', 'legal-', 'financial-', 'media-'])]
    
    if academic_files:
        content += f"#### Academic ({len(academic_files)} files)\n"
        for file in academic_files[:20]:  # Show first 20
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        if len(academic_files) > 20:
            content += f"- ... and {len(academic_files) - 20} more\n"
        content += "\n"
    
    if personal_files:
        content += f"#### Personal ({len(personal_files)} files)\n"
        for file in personal_files[:20]:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        if len(personal_files) > 20:
            content += f"- ... and {len(personal_files) - 20} more\n"
        content += "\n"
    
    if research_files:
        content += f"#### Research ({len(research_files)} files)\n"
        for file in research_files:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        content += "\n"
    
    if technical_files:
        content += f"#### Technical ({len(technical_files)} files)\n"
        for file in technical_files:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        content += "\n"
    
    if legal_files:
        content += f"#### Legal ({len(legal_files)} files)\n"
        for file in legal_files:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        content += "\n"
    
    if financial_files:
        content += f"#### Financial ({len(financial_files)} files)\n"
        for file in financial_files:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        content += "\n"
    
    if media_files:
        content += f"#### Media ({len(media_files)} files)\n"
        for file in media_files:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        content += "\n"
    
    if other_files:
        content += f"#### Other ({len(other_files)} files)\n"
        for file in other_files[:20]:
            name = file.replace('.md', '')
            content += f"- [[{name}]]\n"
        if len(other_files) > 20:
            content += f"- ... and {len(other_files) - 20} more\n"
        content += "\n"
    
    content += f"""
---
**Total files in wiki: {len(wiki_files)}**
- Category pages: {len(categories['Categories'])}
- Source pages: {len(categories['Sources'])}
"""
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated index.md with {len(wiki_files)} files")

if __name__ == "__main__":
    update_index()
