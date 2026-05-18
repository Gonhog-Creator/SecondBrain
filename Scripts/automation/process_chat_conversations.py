#!/usr/bin/env python3
"""
Process ChatGPT and Claude conversation exports from raw-sources/.
Extracts key insights and prepares them for wiki integration.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

RAW_SOURCES = Path("/Users/josemariabarbeito/PycharmProjects/SecondBrain/raw-sources")
CHATGPT_DIR = RAW_SOURCES / "chatgpt"
CLAUDE_DIR = RAW_SOURCES / "claude"

def find_conversations():
    """Find all conversation files in raw-sources."""
    conversations = []
    
    for directory in [CHATGPT_DIR, CLAUDE_DIR]:
        if not directory.exists():
            continue
            
        for file in directory.iterdir():
            if file.suffix in ['.json', '.md', '.txt'] and file.name != 'TEMPLATE.md':
                conversations.append(file)
    
    return conversations

def process_chatgpt_json(filepath):
    """Process ChatGPT export JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        conversations = []
        for chat in data:
            title = chat.get('title', 'Untitled')
            messages = chat.get('messages', [])
            
            # Extract key content
            content_parts = []
            for msg in messages:
                if msg.get('role') == 'user':
                    content_parts.append(f"**Question:** {msg.get('content', '')[:200]}...")
                elif msg.get('role') == 'assistant':
                    content_parts.append(f"**Answer:** {msg.get('content', '')[:500]}...")
            
            conversations.append({
                'title': title,
                'content': '\n\n'.join(content_parts),
                'date': chat.get('create_time', 'Unknown'),
                'source': 'ChatGPT'
            })
        
        return conversations
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []

def process_markdown(filepath):
    """Process markdown conversation files."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return [{
            'title': filepath.stem,
            'content': content,
            'date': filepath.stem[:10] if len(filepath.stem) > 10 else 'Unknown',
            'source': 'ChatGPT' if 'chatgpt' in str(filepath) else 'Claude'
        }]
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []

def main():
    print("=" * 60)
    print("Chat Conversation Processor")
    print("=" * 60)
    print()
    
    # Find all conversations
    conversations = find_conversations()
    
    if not conversations:
        print("No conversation files found in raw-sources/chatgpt/ or raw-sources/claude/")
        print()
        print("To add conversations:")
        print("1. Export from ChatGPT: Settings → Data controls → Export data")
        print("2. Or copy-paste important conversations to raw-sources/chatgpt/")
        print("3. See raw-sources/chatgpt/TEMPLATE.md for formatting")
        return
    
    print(f"Found {len(conversations)} conversation file(s):")
    for conv in conversations:
        print(f"  - {conv.name}")
    print()
    
    # Process each file
    all_extracted = []
    for filepath in conversations:
        print(f"Processing: {filepath.name}")
        
        if filepath.suffix == '.json':
            extracted = process_chatgpt_json(filepath)
        else:
            extracted = process_markdown(filepath)
        
        all_extracted.extend(extracted)
        print(f"  Extracted {len(extracted)} conversation(s)")
    
    print()
    print("=" * 60)
    print(f"Total conversations ready for wiki integration: {len(all_extracted)}")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review the extracted content above")
    print("2. Tell Claude: 'Integrate these conversations into the wiki'")
    print("3. Claude will create/update wiki pages with the insights")

if __name__ == "__main__":
    main()
