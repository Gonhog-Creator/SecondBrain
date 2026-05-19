# Knowledge Expansion Integrations

Tools, services, and methods to expand what Cascade (the AI) can access and process for your Second Brain.

## Current Capabilities

Cascade can currently access:
- Files in your workspace (raw-sources/, wiki/, junk_drawer/)
- Web search results
- URL content (with your approval)
- Terminal commands
- Read terminal output

## Integration Categories

### 1. Source Ingestion (Getting Content In)

#### Obsidian Web Clipper (Essential)
**What:** Browser extension that converts web articles to markdown
**How:** 
- Install in Chrome/Safari/Firefox
- Clip articles directly to `raw-sources/articles/`
- Cascade processes and integrates into wiki

**Best for:**
- Blog posts
- News articles
- Documentation
- Research papers

**Setup:**
1. Install extension
2. Set download folder to `raw-sources/articles/`
3. Use hotkey to clip (Ctrl+Shift+C typical)
4. Tell Cascade: "Process new articles in raw-sources/articles/"

---

#### Readwise Integration (For Readers)
**What:** Syncs Kindle highlights, article highlights to markdown
**How:**
- Readwise → Export to Obsidian
- Creates `raw-sources/books/` with your highlights
- Cascade processes into wiki

**Best for:**
- Book notes
- Article highlights
- Podcast transcripts

**Setup:**
1. Subscribe to Readwise
2. Connect Kindle, Instapaper, etc.
3. Enable "Obsidian Export"
4. Set export folder: `raw-sources/readwise/`

---

#### Zotero + Better BibTeX (For Researchers)
**What:** Reference manager with markdown export
**How:**
- Export papers to `raw-sources/papers/`
- Include PDFs and notes
- Cascade extracts and categorizes

**Best for:**
- Academic papers
- Research PDFs
- Citations

**Setup:**
1. Install Zotero
2. Install Better BibTeX plugin
3. Set auto-export to markdown
4. Point export folder to `raw-sources/papers/`

---

#### Kindle Highlights Export
**What:** Tool to export Kindle highlights to markdown
**Tools:**
- [bookcision](https://github.com/bruinrom/bookcision) - Browser extension
- [clippings.io](https://clippings.io/) - Web service
- [readwise](https://readwise.io/) - Paid service (recommended)

**Best for:**
- Book highlights
- Reading notes
- Quotes collection

---

### 2. Conversation Integration (Chat → Wiki)

#### ChatGPT Export (Already Set Up)
**What:** Bulk export all ChatGPT conversations
**How:**
- Settings → Data controls → Export data
- Wait 24-48 hours
- Extract JSON to `raw-sources/chatgpt/`
- Cascade processes all conversations

**Also works with:**
- Copy-paste individual conversations
- Browser extensions for real-time export

#### Claude Project (This System)
**What:** Direct integration - we're building it now
**How:**
- Conversations happen in this IDE
- Important insights get filed to wiki
- Cascade maintains context across sessions

---

### 3. Meeting & Call Integration

#### Otter.ai / Grain / Fireflies
**What:** AI meeting transcription services
**How:**
- Record meetings
- Get transcript
- Export to `raw-sources/transcripts/`
- Cascade extracts decisions and action items

**Best for:**
- Meeting notes
- Action items
- Decision logs

**Setup:**
1. Subscribe to transcription service
2. Export transcripts as markdown
3. Save to `raw-sources/transcripts/YYYY-MM-DD-meeting-name.md`
4. Tell Cascade: "Process the meeting transcript"

#### Manual Recording
**What:** Record meetings yourself, use Whisper
**How:**
- Record audio (with permission)
- Use OpenAI Whisper to transcribe
- Save to `raw-sources/transcripts/`

**Free alternative:**
- Use Mac Dictation or Windows Speech
- Google Docs voice typing

---

### 4. Email Integration

#### Gmail → Markdown Export
**What:** Convert important emails to markdown
**Tools:**
- [gmail-to-obsidian](https://github.com/kepano/gmail-to-obsidian) - Script
- Manual copy-paste for important emails
- Zapier automation (advanced)

**Best for:**
- Important decisions
- Project communications
- Newsletters worth saving

**Setup:**
1. Use script or copy-paste
2. Save to `raw-sources/email/`
3. Cascade processes key information

#### Newsletter Aggregation
**What:** Save valuable newsletters
**How:**
- Forward to dedicated email
- Use tool to convert to markdown
- Process with Cascade

---

### 5. Bookmark & Reading List Integration

#### Raindrop.io
**What:** Bookmark manager with markdown export
**How:**
- Save bookmarks with tags
- Export collections to markdown
- Cascade processes articles

**Best for:**
- Article backlog
- Research collection
- Topic-based organization

#### Pinboard + Export
**What:** Simple bookmarking with export
**How:**
- Save bookmarks
- Export JSON
- Convert to markdown
- Cascade processes

---

### 6. Code & GitHub Integration

#### GitHub Repository Sync
**What:** Clone repos, extract documentation and code
**How:**
- Already set up: `Scripts/automation/process_github_repos.py`
- Clones repos to `junk_drawer/github/`
- Extracts text from code and docs
- Cascade processes into wiki

**Best for:**
- Your own projects
- Open source libraries
- Code research

#### Code Snippet Collection
**What:** Save useful code snippets
**How:**
- Save to `raw-sources/code/`
- Cascade creates language-specific wiki pages
- Cross-reference with projects

---

### 7. Image & Visual Integration

#### Screenshot → Wiki
**What:** Save screenshots with context
**How:**
1. Take screenshot
2. Save to `raw-sources/assets/screenshots/`
3. Create markdown file explaining screenshot
4. Cascade processes and links to relevant pages

#### PDF Extraction (Already Working)
**What:** PDFs in junk_drawer/ automatically processed
**How:**
- `Scripts/automation/rebuild_wiki_after_reorganization.py`
- Extracts text using `pdftotext`
- Creates wiki pages

---

### 8. Web Research & Monitoring

#### Web Search (Already Available)
**What:** I can search the web for current information
**How:**
- Ask me to search
- I find and summarize
- Can save results to wiki

**Best for:**
- Current events
- Recent research
- Fact checking
- Finding sources

#### RSS Feeds (Advanced)
**What:** Monitor blogs and news
**Tools:**
- [RSS to Markdown](https://github.com/nicholaswilde/rss-to-markdown) - Script
- Zapier/Make automation
- Feedly export

**Best for:**
- Following researchers
- Industry news
- Blog monitoring

---

### 9. API Integrations (Developer Level)

#### Notion → Obsidian
**What:** Export Notion pages to markdown
**Tools:**
- [notion-to-obsidian](https://github.com/connertennery/Notion-to-Obsidian-Converter) - Converter
- Notion API + custom script

#### Slack → Markdown
**What:** Export important Slack conversations
**Tools:**
- [slack-export](https://github.com/zach-snell/slack-export) - Export tool
- Manual copy-paste for key threads

#### Trello/Asana → Tasks
**What:** Sync tasks to Obsidian Tasks plugin
**Tools:**
- API integration
- Zapier/Make
- Manual periodic export

---

## Recommended Priority Order

### Phase 1: Essential (Do First)
1. **Obsidian Web Clipper** - Start clipping articles today
2. **ChatGPT Export** - Already requested, process when it arrives
3. **Meeting Transcripts** - Start with Otter.ai free tier

### Phase 2: Power User
4. **Readwise** - If you read a lot of books/articles
5. **Kindle Highlights** - Connect your reading to wiki
6. **GitHub Integration** - Already partially set up

### Phase 3: Advanced
7. **Zotero** - If doing academic research
8. **RSS Monitoring** - For staying current in your field
9. **Email Export** - For important communications

---

## Quick Wins You Can Do Today

### 1. Set Up Web Clipper (5 minutes)
```
1. Install Obsidian Web Clipper browser extension
2. Configure download folder: /Users/josemariabarbeito/PycharmProjects/SecondBrain/raw-sources/articles/
3. Test by clipping this page
4. Tell Cascade: "Process the article I just clipped"
```

### 2. Copy-Paste One ChatGPT Conversation (5 minutes)
```
1. Open your most valuable recent ChatGPT conversation
2. Copy key insights
3. Create file: raw-sources/chatgpt/2026-05-19-valuable-insight.md
4. Tell Cascade: "Process this conversation and integrate into wiki"
```

### 3. Record Tomorrow's Meeting (Setup 10 minutes)
```
1. Sign up for Otter.ai (free tier)
2. Install mobile app or use web
3. Record your next meeting
4. Export transcript to raw-sources/transcripts/
5. Tell Cascade: "Extract decisions and action items"
```

---

## Cascade Processing Commands

Once content is in raw-sources/, use these commands:

```
"Process all new files in raw-sources/articles/"
"Process the ChatGPT conversations in raw-sources/chatgpt/"
"Extract insights from the meeting transcript in raw-sources/transcripts/"
"Integrate my Kindle highlights into the wiki"
"Process the GitHub repositories and create project summaries"
```

---

## What Makes a Good Integration

**Good integrations:**
- Export to markdown automatically
- Preserve metadata (dates, sources, authors)
- Work with your folder structure
- Can be triggered manually or on schedule

**Avoid:**
- Proprietary formats I can't read
- Binary-only exports
- Cloud-only access (I need local files)
- Complex authentication (unless necessary)

---

*Pick 2-3 integrations from Phase 1 and set them up this week. Don't try to do everything at once.*
