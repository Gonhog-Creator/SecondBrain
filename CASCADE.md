# LLM Wiki Schema for SecondBrain

This schema file tells Cascade (the AI agent) how to maintain the knowledge base. This is the key configuration file — it's what makes the AI a disciplined wiki maintainer rather than a generic chatbot. The user and AI co-evolve this over time.

## The Core Idea

Instead of retrieving from raw documents on every query, the AI incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the AI reads it, extracts key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, and strengthening the evolving synthesis.

The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. It gets richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the AI writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The AI does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time.

In practice, the user has the AI agent open on one side and Obsidian open on the other. The AI makes edits based on conversation, and the user browses the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the AI is the programmer; the wiki is the codebase.

## Architecture

There are three layers:

**raw-sources/** — Curated collection of source documents. Articles, papers, images, data files, ChatGPT conversations, Cascade conversations, meeting transcripts, research notes, book highlights, podcast notes. These are immutable — the AI reads from them but never modifies them. This is the source of truth. Organized into subdirectories by source type.

**junk_drawer/** — Legacy raw sources from initial wiki setup. Contains 900+ PDF files and other documents. Gradually being migrated to raw-sources/ structure.

**wiki/** — AI-generated markdown files. Summaries, entity pages, concept pages, comparisons, overviews, synthesis. The AI owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the AI writes it.

**CASCADE.md** — This schema file. It tells the AI how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki.

## Directory Structure

```
SecondBrain/
├── raw-sources/           # New curated sources (preferred)
│   ├── chatgpt/          # ChatGPT conversation exports
│   ├── claude/           # Claude conversation exports
│   ├── articles/         # Web articles, blog posts
│   ├── books/            # Book notes, highlights
│   ├── papers/           # Research papers
│   ├── transcripts/      # Meeting transcripts, podcasts
│   └── misc/             # Screenshots, random notes
├── junk_drawer/          # Legacy raw sources (900+ PDFs)
├── wiki/                 # AI-generated organized knowledge
│   ├── index.md          # Catalog of all wiki pages
│   ├── log.md            # Chronological record
│   ├── lint-report.md    # Health check findings
│   └── [category-pages]/ # Organized by topic
├── Scripts/automation/   # Helper scripts
├── daily-tasks.md        # User reference guide
└── CASCADE.md           # This file - AI instructions
```

## Operations

### INGEST - Process New Sources

When the user adds a new source to raw-sources/ or junk_drawer/ and asks to process it:

**Workflow:**
1. Read the source completely
2. Discuss key takeaways with the user
3. Write a summary page in wiki/
4. Update wiki/index.md with a link and one-line description
5. Update any existing concept/entity pages that this source connects to
6. Flag contradictions with existing knowledge
7. Append an entry to wiki/log.md in format: `## [YYYY-MM-DD] ingest | Source Name`

**Important:** A single source might touch 10-15 wiki pages. Stay involved — read the summaries, check the updates, and guide the AI on what to emphasize.

**For raw-sources/chatgpt/ and raw-sources/claude/:**
- Extract key insights, questions asked, and answers received
- Identify recurring themes across conversations
- Create/update concept pages for topics discussed
- Note where AI conversations contradict other sources
- Tag with `source: ChatGPT` or `source: Claude` and date

### QUERY - Answer Questions from Wiki

When the user asks questions against the wiki:

**Workflow:**
1. Read wiki/index.md first to find relevant pages
2. Read those pages
3. Synthesize an answer with citations using [[page-name]] format
4. **Important insight:** Good answers can be filed back into the wiki as new pages

**Answer formats:**
- Markdown pages for explanations
- Comparison tables for contrasts
- Slide decks (Marp format) for presentations
- Charts (matplotlib) for data
- Analysis summaries for discoveries

**Compounding principle:** A comparison you generate, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

### LINT - Health Check the Wiki

Periodically (weekly recommended) run health checks. Look for:

- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Important concepts mentioned but lacking dedicated pages
- Missing cross-references
- Data gaps that could be filled with web search

**Output:** Write findings to wiki/lint-report.md with specific fixes needed.

**Purpose:** Catches errors before they compound. If the AI writes something slightly wrong and you save it back, the next answer builds on that mistake. The health check is your quality control.

## Special Files

**wiki/index.md** — Content-oriented catalog. Each page listed with a link, one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The AI updates it on every ingest. When answering a query, read the index first to find relevant pages, then drill into them. This works surprisingly well even with hundreds of pages and avoids the need for embedding-based RAG infrastructure.

**wiki/log.md** — Chronological record. Append-only timeline of what happened and when — ingests, queries, lint passes. Format: `## [YYYY-MM-DD] operation_type | Description`

**Useful tip:** If each entry starts with a consistent prefix (e.g., `## [2026-05-18] ingest | Article Title`), the log becomes parseable with simple unix tools — `grep "^## \[" log.md | tail -5` gives you the last 5 entries.

**wiki/lint-report.md** — Health check findings. Written during LINT operations. Contains specific issues found and recommended fixes.

**daily-tasks.md** — User reference guide. Contains workflows, tips, templates, and quick reference. Lives at root level for easy access.

**raw-sources/README.md** — Guide for adding new sources. Explains folder structure and integration methods.

## Automation Examples

The AI can create and help set up automation scripts:

### Morning Briefing Script
Setup command:
```
Write a Python script called morning_digest.py that:
1. Reads Memory.md and surfaces any open actions due today
2. Reads any new files added to /raw-sources/ in the last 24 hours
3. Prints a clean briefing to the terminal
Then schedule it as a cron job every morning at 7:30am.
```

### Call Transcript Processing
After meetings:
```
Read the transcript in /raw-sources/transcripts/call-today.md.
Extract every decision made, every action item with owner and deadline,
and a 3-bullet summary. Add actions to /wiki/action-tracker.md,
log decisions to /wiki/decision-log.md, and create a topic page
linking back to this transcript.
```

### Bulk Processing
Process multiple sources:
```
Process all new files in /raw-sources/articles/ and integrate
into the wiki. Update index.md and log all changes.
```

## Page Conventions

**Linking:**
- Use `[[page-name]]` for internal wiki links
- Use `[text](URL)` for external links
- Create links liberally — cross-references are valuable

**Headings:**
- Use `#` for page title
- Use `##` for major sections
- Use `###` for subsections

**Content:**
- Keep pages focused on single topics
- Start with a one-paragraph summary
- Use bullet points for lists
- Add citations back to sources: `(Source: [[source-page]])`
- Include dates for time-sensitive information

**Frontmatter (optional but useful):**
```markdown
---
date: 2026-05-18
source: [original source]
tags: [tag1, tag2]
---
```

## File Naming

- Use lowercase with hyphens: `concept-name.md`
- Use descriptive names that indicate content
- Avoid spaces in filenames
- For sources, include date prefix: `2026-05-18-article-title.md`
- For daily notes: `YYYY-MM-DD.md`
- For category pages: use category name directly

## Categorization Guidelines

Current wiki categories (maintain consistency):
- **academic-homework** — Homework assignments, problem sets
- **academic-lecture** — Lecture notes, slides
- **academic-exam** — Exams, quizzes, practice tests
- **academic-syllabus** — Course syllabi
- **academic-lab** — Lab manuals, experiment notes
- **research-paper** — Research papers, journal articles
- **technical-safety** — Safety documentation, protocols
- **personal-resume** — Resumes, CVs
- **personal-application** — Job applications, cover letters
- **legal-document** — Legal papers, contracts
- **financial-document** — Financial records, statements
- **media-transcript** — Podcast transcripts, video transcripts
- **github-code** — Code from GitHub repositories
- **other** — Uncategorized items (minimize this)

When creating new category pages, follow existing format in wiki/.

## Troubleshooting

### Wiki Getting Too Large
- Archive old completed projects to `wiki/archive/`
- Remove duplicate notes (check for similar titles)
- Clean up unused attachments in raw-sources/
- Consider splitting into multiple vaults by topic

### Graph View Too Complex
- Filter by tag or folder in Obsidian
- Adjust node size and connection strength settings
- Use local graph view for specific topics instead of global
- Archive old notes to reduce node count

### Search Not Finding Notes
- Check wiki/index.md is up to date (run INGEST on recent sources)
- Use more specific search terms
- Try regex search for patterns: `/pattern/`
- Search in content vs filenames (Ctrl+Shift-F)

### AI Not Following Schema
- This file (CASCADE.md) is the authority — check that AI is reading it
- Add more specific examples to CASCADE.md
- Be explicit in your prompts: "Following CASCADE.md guidelines..."
- Co-evolve this file with the AI based on what works

### Duplicate Processing
- Check log.md for what's already been processed
- Use consistent source naming to avoid duplicates
- Archive processed files to `raw-sources/archive/`

## Tips and Tricks

**Obsidian Web Clipper** — Browser extension that converts web articles to markdown. Very useful for quickly getting sources into raw-sources/articles/.

**Download images locally** — In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g., `raw-sources/assets/`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g., Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded locally. This lets the AI view images directly instead of relying on URLs that may break.

**Obsidian's graph view** — The best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.

**Marp** — Markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.

**Dataview** — Obsidian plugin that runs queries over page frontmatter. If the AI adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.

**Git version control** — The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free. Commit regularly.

## Why This Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value.

**LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.** The wiki stays maintained because the cost of maintenance is near zero.

**Human's job:** Curate sources, direct analysis, ask good questions, think about what it all means.
**AI's job:** Everything else — summarizing, cross-referencing, filing, bookkeeping, keeping the wiki consistent.

The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.

---

*Note: This document is a living schema. It should be updated as the system evolves and new patterns emerge. The user and AI co-evolve it over time.*

*Last updated: 2026-05-18*
