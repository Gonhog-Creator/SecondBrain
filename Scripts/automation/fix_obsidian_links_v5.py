#!/usr/bin/env python3
import os
import re

def fix_links_in_wiki():
    wiki_dir = "wiki"
    
    # Get list of actual wiki filenames (without .md extension)
    wiki_files = set()
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            # Store the filename without .md for matching
            wiki_files.add(file.replace('.md', ''))
    
    # Fix all .md files in wiki
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            file_path = os.path.join(wiki_dir, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove .md from links - Obsidian adds .md automatically
                content = re.sub(r'\[\[([^\]]+)\.md\]\]', r'[[\1]]', content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Fixed links in {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    fix_links_in_wiki()
