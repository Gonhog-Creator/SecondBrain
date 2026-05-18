#!/usr/bin/env python3
import os
import re

def fix_links_in_wiki():
    wiki_dir = "wiki"
    
    # Fix all .md files in wiki
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            file_path = os.path.join(wiki_dir, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace [[filename.pdf]] with [[filename.pdf]] (remove .pdf from link text)
                # Obsidian will automatically resolve this to filename.pdf.md
                content = re.sub(r'\[\[([^\]]+)\.pdf\]\]', r'[[\1]]', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Fixed links in {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    fix_links_in_wiki()
