# Daily Tasks and Obsidian AI Second Brain Guide

## Core Architecture

### Three-Layer System
**Raw Sources** (`raw-sources/`)
- Your junk drawer - articles, notes, screenshots, meeting transcripts, bookmarks, research, book notes, podcast takeaways
- Do not organize - that's the AI's job
- Files are immutable - AI reads but never modifies
- This is your source of truth

**Wiki** (`wiki/`)
- AI writes the organized version here
- Summaries, concept pages, entity pages, comparisons, overview, synthesis
- AI owns this folder entirely
- You read it, AI writes it - you never edit by hand
- Special files:
  - `index.md` - catalog of everything in wiki with links and summaries
  - `log.md` - chronological record of ingests, queries, health checks

**Schema** (`CLAUDE.md` or `AGENTS.md`)
- Tells AI how wiki is structured
- Defines conventions and workflows
- Key configuration file - makes AI disciplined wiki maintainer
- Co-evolve this with AI over time

## Daily Maintenance Tasks

### Morning Routine
- **Morning briefing**: Run automated digest script if set up
- **Quick capture check**: Review any new items in raw-sources
- **Daily note creation**: Create new daily note with template
- **Task review**: Check overdue tasks and prioritize today's work
- **Wiki health check**: Quick scan of recent additions for any issues

### Evening Routine  
- **Daily note review**: Complete today's daily note, add any missed items
- **Task cleanup**: Mark completed tasks, reschedule if needed
- **Capture inbox empty**: Process all items in your quick capture/inbox
- **Graph view check**: Look at wiki graph to see new connections

## Weekly Tasks
- **Back up your vault**: Commit to git or export backup
- **Health check**: Run lint operation to find contradictions, orphan pages, outdated claims
- **Review orphan pages**: Check graph for disconnected notes
- **Clean up duplicates**: Search for similar notes and merge if needed
- **Update index**: Ensure wiki index reflects current structure
- **Plugin updates**: Check for Obsidian plugin updates

## Core Operations

### INGEST New Sources
**Manual Ingest:**
```
claude -p "I just added an article to /raw-sources/. Read it, extract the key ideas, write a summary page to /wiki/, update index.md with a link and one-line description, and update any existing concept pages that this article connects to. Log what you changed to log.md. Show me every file you touched." --allowedTools Bash,Write,Read
```

**Web Clipper:**
- Install Obsidian Web Clipper browser extension
- Converts web articles to markdown with one click
- Fastest way to get sources into raw collection

**Process:**
1. Clip article or add source to raw-sources/
2. Tell Claude to process it
3. Claude reads, extracts key ideas, writes summary
4. Updates index.md and relevant concept pages
5. Logs changes to log.md
6. One article can touch 10-15 wiki pages

### ASK Your Wiki Questions
**Example Queries:**
- "Based on everything in wiki/, what are the three biggest gaps in my understanding of [topic]?"
- "Compare what source A says about [concept] vs source B. Where do they disagree?"
- "Write me a 500-word briefing on [topic] using only what is in this knowledge base."

**Process:**
1. Claude scans index for relevant pages
2. Pulls right pages and synthesizes answer with citations
3. **Important**: Save good answers back into wiki as new pages
4. Comparisons, analyses, connections should not disappear into chat history
5. Every question makes the next answer better (compounding loop)

### RUN Health Check
**Weekly Lint:**
```
claude -p "Read every file in /wiki/. Find: contradictions between pages, orphan pages with no inbound links, concepts mentioned repeatedly but with no dedicated page, and claims that seem outdated based on newer files in /raw-sources/. Write a health report to /wiki/lint-report.md with specific fixes." --allowedTools Bash,Write,Read
```

**Purpose:**
- Catches errors before they compound
- Quality control for AI-generated content
- Identifies gaps and inconsistencies
- Suggests new questions to investigate
- Recommends new sources to look for

## Essential Obsidian Tips

### Core Workflow Tips
- **Quick capture**: Set up hotkey (e.g., Ctrl+N) for instant note creation
- **Daily notes**: Use daily notes as primary capture and review mechanism
- **Inbox zero**: Process inbox daily, don't let it accumulate
- **Link everything**: Use `[[wikilinks]]` to connect related concepts
- **Tag consistently**: Develop consistent tagging system for easy retrieval
- **Graph view**: Best way to see wiki shape - what's connected, hubs, orphans

### Organization Tips
- **PARA method**: Organize into Projects, Areas, Resources, Archives
- **Zettelkasten**: Create atomic notes with clear titles and connections
- **MOCs (Maps of Content)**: Create index notes for major topics
- **Date-based notes**: Use YYYY-MM-DD format for daily notes
- **Folder structure**: Keep it simple - don't over-organize

### Plugin Recommendations

#### Essential Plugins
- **Templater**: Automate daily note creation with templates
- **Dataview**: Query notes with SQL-like syntax, generate dynamic tables
- **Tasks**: Enhanced task management with recurring tasks
- **Calendar**: Visual calendar view of daily notes
- **Graph Analysis**: Analyze wiki structure and connections

#### Useful Plugins
- **Obsidian Web Clipper**: Save web content as markdown
- **Excalidraw**: Draw diagrams and sketches
- **Advanced Tables**: Better table editing
- **Kanban**: Visual task boards
- **Marp**: Create presentations from markdown

### Search and Navigation Tips
- **Global search**: Use Ctrl+Shift+F for full-text search
- **Ribbon search**: Use Ctrl+P for quick file navigation
- **Linked mentions**: See all notes linking to current note (backlinks panel)
- **Graph view**: Visualize connections between notes
- **Starred files**: Mark frequently accessed notes for quick access

### Productivity Tips
- **Templates**: Create templates for different note types (daily, meeting, project)
- **Hotkeys**: Customize hotkeys for most common actions
- **Split view**: Use split pane to reference multiple notes
- **Command palette**: Use Ctrl+P for quick access to all commands
- **Workspaces**: Save different panel layouts for different workflows

## Automation Examples

### Morning Briefing Script
**Setup:**
```
claude -p "Write a Python script called morning_digest.py that: 1) reads Memory.md and surfaces any open actions due today 2) reads any new files added to /raw-sources/ in the last 24 hours 3) prints a clean briefing to the terminal. Then schedule it as a cron job every morning at 7:30am." --allowedTools Bash,Write
```

**Result:**
- Every morning you get a summary of what needs attention
- Shows new knowledge added in last 24 hours
- Set up once, never stops working

### Call Transcript Processing
**After meetings:**
```
claude -p "Read the transcript in /raw-sources/call-today.md. Extract every decision made, every action item with owner and deadline, and a 3-bullet summary. Add actions to /wiki/action-tracker.md, log decisions to /wiki/decision-log.md, and create a topic page linking back to this transcript." --allowedTools Bash,Write,Read
```

**Result:**
- Every decision filed
- Every action tracked
- Nothing lost to chat history

## Initial Setup Steps

### STEP 1: Create Your Vault
- Open Obsidian and create new vault
- Create folders:
  - `raw-sources/` - your junk drawer
  - `wiki/` - AI writes organized version here
- Create special files in wiki/:
  - `index.md` - catalog of everything
  - `log.md` - chronological record

### STEP 2: Add Schema File
- Create `CLAUDE.md` (if using Claude Code) or `AGENTS.md` (if using OpenAI Codex)
- This tells AI how wiki is structured
- Most important step - makes AI disciplined wiki maintainer
- Co-evolve this with AI over time

### STEP 3: Fill Raw Sources
- Don't stare at empty directory
- Dump everything you already have:
  - Articles saved and never re-read
  - Book highlights from Kindle
  - Podcast notes
  - Meeting transcripts
  - Project docs
  - Research before big decisions
  - Old project notes
  - Lessons from failures
  - YouTube rabbit hole notes
  - Screenshots
- Copy-paste articles into .md or .txt files
- Do not rename or clean up - just get it all in
- No existing material? Have 20-minute Claude chat about your work/goals, save as Memory.md

### STEP 4: Tell Claude to Build Wiki
```
claude -p "Read everything in /raw-sources/. Compile a wiki in /wiki/ following the rules in CLAUDE.md. Create an index.md first, then one .md file per major topic. Link related topics using [[topic-name]] format. Summarize every source. Log everything to log.md." --allowedTools Bash,Write,Read
```

### STEP 5: Use It Every Day
- INGEST: Add new sources regularly
- ASK: Query your wiki for insights
- LINT: Run weekly health checks

### STEP 6: Set Up Automations (Optional)
- Morning briefing script
- Call transcript processing
- Custom workflows for your needs

## Advanced Tips

### Performance Optimization
- **Limit graph view nodes**: Adjust settings if graph gets slow
- **Disable heavy plugins**: Turn off plugins you don't use regularly
- **Clean attachments**: Regularly review and clean attachment folder
- **Compress images**: Use image optimization for large attachments
- **Archive old notes**: Move inactive notes to archive folder

### Optional CLI Tools
- **qmd**: Local search engine for markdown files
  - Hybrid BM25/vector search with LLM re-ranking
  - All on-device
  - CLI for LLM to shell out to
  - MCP server for native tool integration
- **Custom scripts**: LLM can help vibe-code simple search tools

### Image Handling
- **Download locally**: In Obsidian Settings → Files and links
  - Set "Attachment folder path" to fixed directory (e.g., `raw/assets/`)
  - In Settings → Hotkeys, bind "Download attachments for current file" to Ctrl+Shift+D
  - After clipping article, hit hotkey to download all images locally
- **Why**: Lets LLM view images directly instead of relying on URLs that may break
- **Note**: LLMs can't natively read markdown with inline images in one pass
  - Workaround: Have LLM read text first, then view referenced images separately

### Version Control
- **Git repo**: Wiki is just markdown files
- Get version history, branching, collaboration for free
- Commit regularly for backups
- Track changes over time

## What You Can Build

### Personal Knowledge Base
- Track goals, health, self-improvement
- File journal entries, articles, podcast notes
- Build structured picture of yourself over time

### Research Wiki
- Go deep on topic over weeks/months
- Read papers, articles, reports
- Incrementally build comprehensive wiki with evolving thesis

### Book Companion Wiki
- File each chapter as you read
- Build pages for characters, themes, plot threads
- Show connections between elements
- Rich companion wiki makes re-reading unnecessary

### Business/Team Wiki
- Internal wiki fed by Slack threads, meeting transcripts, project docs, customer calls
- Wiki stays current because AI does maintenance nobody wants to do
- Possibly with humans reviewing updates

### Competitive Analysis Vault
- Monitor competitor pricing, features, hiring, positioning
- Every new data point integrated automatically

### Client Knowledge Vault
- Everything about each client in searchable system
- Updates itself automatically

### Course Notes
- Build comprehensive study wiki as you take course
- AI cross-references concepts across lectures

## Resources

### Essential Reading
- [How to Build an AI Second Brain with Claude and Obsidian](https://docs.google.com/document/d/1vZRw778fqTlwfRSBenwL2Qz2e26LI1WhVloiq9YOzag/mobilebasic)
- [Andrej Karpathy's Personal Knowledge Base](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Engineers Guide to Building a Second Brain in Obsidian](https://ps11.hashnode.dev/engineers-guide-to-building-a-second-brain-in-obsidian-practical-tips)

### Community Resources
- [Obsidian Forum](https://forum.obsidian.md/) - Community discussions and workflows
- [Obsidian Discord](https://discord.gg/obsidian-md) - Real-time help and tips
- [Obsidian Publish](https://publish.obsidian.md/) - Publish vault as website
- [Obsidian Sync](https://obsidian.md/sync) - Cross-device synchronization

### Tools
- [Obsidian](https://obsidian.md/) - Free markdown editor
- [Claude Code](https://claude.com/product/claude-code) - AI agent for wiki maintenance
- [qmd](https://github.com/tobi/qmd) - Local markdown search engine

## Quick Reference

### Common Hotkeys
- `Ctrl+N`: New note
- `Ctrl+O`: Quick switcher
- `Ctrl+Shift+F`: Global search
- `Ctrl+G`: Graph view
- `Ctrl+E`: Toggle edit/preview mode
- `Ctrl+K`: Insert link
- `Ctrl+Shift+K`: Insert wikilink

### Daily Note Template
```markdown
---
date: {{date}}
tags: daily
---

## Tasks
- [ ] 

## Notes
- 

## Reflection
- 
```

### Weekly Review Template
```markdown
---
week: {{week}}
tags: review
---

## Completed
- 

## In Progress
- 

## Blocked
- 

## Next Week
- 
```

### Claude Commands
**Initial Wiki Build:**
```
claude -p "Read everything in /raw-sources/. Compile a wiki in /wiki/ following the rules in CLAUDE.md. Create an index.md first, then one .md file per major topic. Link related topics using [[topic-name]] format. Summarize every source. Log everything to log.md." --allowedTools Bash,Write,Read
```

**Ingest New Source:**
```
claude -p "I just added an article to /raw-sources/. Read it, extract the key ideas, write a summary page to /wiki/, update index.md with a link and one-line description, and update any existing concept pages that this article connects to. Log what you changed to log.md. Show me every file you touched." --allowedTools Bash,Write,Read
```

**Health Check:**
```
claude -p "Read every file in /wiki/. Find: contradictions between pages, orphan pages with no inbound links, concepts mentioned repeatedly but with no dedicated page, and claims that seem outdated based on newer files in /raw-sources/. Write a health report to /wiki/lint-report.md with specific fixes." --allowedTools Bash,Write,Read
```

## Troubleshooting

### Wiki Getting Too Large
- Archive old completed projects
- Remove duplicate notes
- Clean up unused attachments
- Consider splitting into multiple vaults

### Graph View Too Complex
- Filter by tag or folder
- Adjust node size and connection settings
- Focus on specific subgraphs
- Use local graph views for specific topics

### Search Not Finding Notes
- Check for typos in search terms
- Use regex search for patterns
- Search in content vs filenames
- Check that notes aren't in excluded folders

### AI Not Following Schema
- Update CLAUDE.md with clearer instructions
- Add more examples of desired behavior
- Be more specific in your prompts
- Check that AI has access to schema file

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or thinking - it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value.

**LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.** The wiki stays maintained because the cost of maintenance is near zero.

**Human's job**: Curate sources, direct analysis, ask good questions, think about what it all means
**LLM's job**: Everything else

Related to Vannevar Bush's Memex (1945) - personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with connections between documents as valuable as documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

## Integrating ChatGPT Conversations

### Why Sync ChatGPT Chats
Your ChatGPT conversations contain valuable insights, questions, answers, and knowledge that should be part of your Second Brain. Integrating them ensures:
- No valuable insights lost in chat history
- Cross-references between AI conversations and your wiki
- Ability to query across all your AI interactions
- Compounding knowledge from multiple AI sources

### Methods to Connect ChatGPT

#### Method 1: ChatGPT Built-in Export (Bulk)
**Best for**: Initial bulk import of all historical chats

**Steps:**
1. Go to ChatGPT → Settings → Data controls → Export data
2. Request data export (takes 24-48 hours)
3. Download the ZIP file when ready
4. Extract conversations to `raw-sources/chatgpt/`
5. Tell Claude to process them:
   ```
   claude -p "Process all ChatGPT conversations in /raw-sources/chatgpt/. Extract key insights, questions asked, important answers, and integrate into wiki. Create topic pages for recurring themes. Update index.md and log.md." --allowedTools Bash,Write,Read
   ```

#### Method 2: Browser Extensions (Ongoing)
**Best for**: Continuous sync of new conversations

**Recommended Extensions:**
- **ChatGPT to Markdown**: Exports individual conversations to markdown
- **Obsidian Web Clipper**: Can capture ChatGPT conversations
- **Save ChatGPT**: Dedicated extension for saving chats

**Workflow:**
1. Install extension
2. After important ChatGPT conversation, export to markdown
3. Save to `raw-sources/chatgpt/`
4. Process with Claude as needed

#### Method 3: Copy-Paste Important Exchanges (Manual)
**Best for**: Selective, high-value conversations only

**When to use:**
- After especially insightful conversations
- When you asked complex questions with detailed answers
- When ChatGPT helped you solve a difficult problem

**Process:**
1. Copy the conversation (or key parts)
2. Create new file: `raw-sources/chatgpt/YYYY-MM-DD-topic.md`
3. Paste and add frontmatter:
   ```markdown
   ---
   date: 2026-05-18
   source: ChatGPT
   topic: [topic name]
   ---
   ```
4. Process with Claude to integrate into wiki

#### Method 4: Zapier/Make Automation (Advanced)
**Best for**: Automated ongoing sync

**Setup:**
1. Use ChatGPT API (requires Plus subscription)
2. Set up webhook or automation tool
3. Auto-export new conversations periodically
4. Save to your vault automatically

**Note**: This requires technical setup and potentially API costs.

### Processing ChatGPT Conversations

When Claude processes your ChatGPT conversations, it should:

1. **Extract key insights**: Pull out important facts, concepts, solutions
2. **Identify questions**: Note what you asked and what you learned
3. **Find recurring themes**: Group related conversations by topic
4. **Create/update wiki pages**: Add to relevant concept/entity pages
5. **Cross-reference**: Link to existing wiki content
6. **Flag contradictions**: Note where ChatGPT and other sources disagree
7. **Log the ingest**: Record in log.md

### Example Integration Workflow

**Daily:**
- After important ChatGPT conversation, export it
- Save to `raw-sources/chatgpt/`
- Tell Claude to process new files

**Weekly:**
- Batch process accumulated conversations
- Review what was integrated
- Check for new connections in graph view

**Monthly:**
- Bulk export all ChatGPT data
- Do comprehensive integration
- Archive processed raw files

### ChatGPT vs Claude in Your Second Brain

**ChatGPT conversations:**
- Often more casual, exploratory
- May contain brainstorming and iterations
- Good for capturing questions and thought process
- Sometimes outdated information (check dates)

**Claude conversations (in this system):**
- Focused on wiki maintenance and structured knowledge
- More systematic and consistent
- Real-time integration as you work

**Best practice:** Use both but distinguish them in your wiki with source tags:
```markdown
---
source: ChatGPT
conversation_date: 2026-05-18
topic: machine-learning
---
```

### Recommended Folder Structure

```
raw-sources/
├── chatgpt/
│   ├── 2026-05-18-ml-concepts.md
│   ├── 2026-05-17-project-ideas.md
│   └── archive/ (processed conversations)
├── claude/
│   └── (Claude conversation exports if any)
└── ...other sources
```

### Tools and Resources

**Export Tools:**
- [ChatGPT Exporter](https://github.com/pionxzh/chatgpt-exporter) - Browser extension
- [ChatGPT to Markdown](https://chrome.google.com/webstore) - Chrome extension
- Official ChatGPT data export (Settings → Data controls)

**Processing Tips:**
- Not all conversations are worth keeping - be selective
- Focus on conversations where you learned something new
- Tag with topics for easier retrieval
- Regular cleanup of raw-sources/chatgpt/ folder

---
*Last updated: 2026-05-18*
*Source: Complete "How to Build an AI Second Brain with Claude and Obsidian" guide + community best practices*
