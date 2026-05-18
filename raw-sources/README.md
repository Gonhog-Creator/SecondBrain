# Raw Sources Directory

This folder contains your unprocessed source materials. The AI reads from these files but never modifies them.

## Folder Structure

```
raw-sources/
├── chatgpt/          # ChatGPT conversation exports
├── claude/           # Claude conversation exports
├── articles/         # Web articles, blog posts
├── books/            # Book notes, highlights
├── papers/           # Research papers, PDFs
├── transcripts/      # Meeting transcripts, podcasts
└── misc/             # Screenshots, random notes
```

## How to Add Chat Conversations

### Option 1: Export from ChatGPT (Recommended)
1. Go to [chat.openai.com](https://chat.openai.com)
2. Click your profile → Settings → Data controls → Export data
3. Wait 24-48 hours for the email
4. Download the ZIP and extract JSON files to `raw-sources/chatgpt/`
5. Tell me: "Process the ChatGPT conversations in raw-sources/chatgpt/"

### Option 2: Copy-Paste Important Chats
1. Open a valuable ChatGPT/Claude conversation
2. Copy the text (Cmd+A, Cmd+C)
3. Create new file: `raw-sources/chatgpt/YYYY-MM-DD-topic.md`
4. Paste and save
5. Tell me to process it

### Option 3: Browser Extension
- Install "ChatGPT to Markdown" browser extension
- Export individual chats as markdown
- Save to appropriate folder

## What Happens Next

When you tell me to process these files, I will:
- Extract key insights, facts, and learnings
- Create or update wiki pages with the knowledge
- Link related concepts together
- Add entries to the log
- Update the index

## Quick Commands

**Process all chat conversations:**
```
Process all conversations in raw-sources/chatgpt/ and raw-sources/claude/
```

**Process specific file:**
```
Process raw-sources/chatgpt/2026-05-18-machine-learning.md
```

**See what's waiting:**
```
What unprocessed files are in raw-sources/?
```
