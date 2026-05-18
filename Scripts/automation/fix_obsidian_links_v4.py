#!/usr/bin/env python3
import os
import re

def fix_links_in_wiki():
    wiki_dir = "wiki"
    
    # Get list of actual wiki filenames (with .md extension)
    wiki_files = set()
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            wiki_files.add(file)
    
    # Fix all .md files in wiki
    for file in os.listdir(wiki_dir):
        if file.endswith('.md') and file not in ['index.md', 'log.md']:
            file_path = os.path.join(wiki_dir, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find all [[links]] and fix them to match actual filenames
                def fix_link(match):
                    link_text = match.group(1)
                    # Try to find matching wiki file (exact match)
                    if link_text + '.md' in wiki_files:
                        return f"[[{link_text}.md]]"
                    # If no match, return original
                    return match.group(0)
                
                content = re.sub(r'\[\[([^\]]+)\]\]', fix_link, content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Fixed links in {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    fix_links_in_wiki()
