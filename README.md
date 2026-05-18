# SecondBrain

A synchronized Obsidian vault for personal knowledge management with cross-device support via Syncthing and Git backups.

## Vault Structure

```
SecondBrain/
├── .obsidian/              # Obsidian vault configuration
├── .stignore              # Syncthing ignore patterns
├── .gitignore             # Git ignore patterns
├── Knowledge/             # Long-form knowledge and reference notes
│   └── Inbox.md           # Rapid capture inbox
├── Projects/              # Project-specific notes and work
│   └── Templates/         # Note templates
│       ├── daily-note.md
│       ├── research-note.md
│       ├── project-note.md
│       └── meeting-note.md
├── Daily/                 # Daily notes (YYYY-MM-DD.md format)
├── Scripts/               # Automation and utility scripts
│   ├── automation/        # Automation scripts
│   │   └── inbox_capture.py
│   ├── indexing/          # Future: indexing scripts
│   └── rag/               # Future: RAG scripts
└── AI/                    # AI-related content and configuration
    ├── AgentMemory/       # AI context and rules
    │   └── system-context.md
    ├── Prompts/           # Stored prompts
    ├── Embeddings/        # Future: vector embeddings
    └── Scratchpad/        # Temporary AI output
        └── temp/          # Volatile temp files
```

## Sync Setup

### Syncthing Configuration

The vault is synchronized across devices using Syncthing.

**Folder Settings:**
- Folder Type: Send & Receive
- Watch for Changes: Enabled
- Rescan Interval: 60 seconds
- Filesystem Watching: Enabled
- Ignore Permissions: Enabled
- Versioning: Staggered File Versioning (30 days)

**Shared Folder:**
- SecondBrain/ (vault root only)
- NOT shared: desktop, documents, home directory

**Ignored Files:**
- Obsidian volatile state (workspace.json, cache)
- Temporary files (*.tmp, *.temp)
- Logs (*.log)
- Python cache (__pycache__/, *.pyc)
- Node modules (node_modules/)
- AI temp output (AI/Scratchpad/temp/)
- Syncthing conflict files (*.sync-conflict*)

### Git Backup

The vault is backed up to a private GitHub repository.

**Commands:**
```bash
git add .
git commit -m "Update vault"
git push
```

**Ignored Files:**
- Obsidian workspace state
- Cache directories
- Environment files
- Temporary AI output

## Obsidian Plugins

Install the following plugins from the Obsidian Community Plugins store:

- **Dataview** - Structured querying and data views
- **Templater** - Dynamic templates with scripting
- **QuickAdd** - Fast capture and workflow automation
- **Calendar** - Daily notes calendar view
- **Tasks** - Task management with queries
- **Omnisearch** - Better search functionality
- **Smart Connections** - AI semantic linking
- **Excalidraw** - Visual thinking and diagrams

## Templates

Templates are located in `Projects/Templates/`:

- **daily-note.md** - Daily journal with tasks, notes, ideas, project links
- **research-note.md** - Research notes with sources and findings
- **project-note.md** - Project tracking with goals and tasks
- **meeting-note.md** - Meeting notes with action items

## Automation

### Inbox Capture Script

Quick CLI capture to append timestamped notes to the inbox:

```bash
python Scripts/automation/inbox_capture.py "Your note here"
```

## Daily Notes Configuration

Configure Obsidian Daily Notes plugin:
- Format: YYYY-MM-DD.md
- Location: Daily/
- Template: Projects/Templates/daily-note.md

## Windsurf Integration

The vault is configured as a Windsurf workspace with:
- Markdown file indexing enabled
- Script access to Scripts/ directory
- Relative path preservation
- No absolute machine-specific paths

## AI Context Rules

AI agents follow these rules (see AI/AgentMemory/system-context.md):
- Use relative paths only
- Prefer markdown outputs
- Store long-form notes in Knowledge/
- Store project work in Projects/
- Store prompts in AI/Prompts/
- Never overwrite notes automatically
- Append rather than replace
- Preserve wikilinks
- Use ISO dates YYYY-MM-DD

## Recovery Steps

If synchronization fails:

1. Check Syncthing status on both devices
2. Verify folder paths match
3. Check for .sync-conflict files
4. Resolve conflicts manually
5. Use Git history for version recovery

## Backup Strategy

- **Primary:** Syncthing real-time sync between devices
- **Secondary:** Git push to private GitHub repository
- **Tertiary:** Local file system backups

Recommended: Commit to Git weekly or after major changes.

## Future Expansion

Prepared directories for Phase 2 enhancements:

- **Scripts/indexing/** - Custom indexing scripts
- **Scripts/rag/** - RAG orchestration
- **AI/Embeddings/** - Vector embeddings storage

Potential tools:
- Ollama (local LLMs)
- ChromaDB (vector database)
- LlamaIndex (RAG orchestration)

## Validation Checklist

Verify setup is complete:
- [ ] Syncthing connected on both devices
- [ ] Obsidian opens successfully
- [ ] Vault syncs both directions
- [ ] Markdown edits propagate
- [ ] No .sync-conflict files
- [ ] Git repository functional
- [ ] Windsurf indexes vault correctly

## Conflict Prevention

AI agents must:
- NEVER auto-edit currently open files
- NEVER auto-edit workspace state files
- ALWAYS append to notes
- ALWAYS create backups
- ALWAYS preserve frontmatter
