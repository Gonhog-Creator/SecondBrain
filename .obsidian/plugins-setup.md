# Obsidian Plugins Setup Guide

Essential plugins for the AI Second Brain workflow.

## Required Plugins

### 1. Templater
**Purpose:** Dynamic templates with date/time variables

**Setup:**
1. Install from Community Plugins
2. Enable plugin
3. Settings → Template folder location: `Templates/`
4. Set "Trigger on new file creation" → ON
5. Set "Trigger on file rename" → ON (optional)

**Hotkeys to configure:**
- Insert template: `Ctrl+Alt+T`
- Jump to next cursor location: `Tab`

**Template variables used:**
- `{{date:YYYY-MM-DD}}` - Date in ISO format
- `{{date:dddd}}` - Day name
- `{{sunday:YYYY-MM-DD}}` - Week start
- `{{yesterday}}`, `{{tomorrow}}` - Relative dates

---

### 2. Dataview
**Purpose:** Query and display wiki content dynamically

**Setup:**
1. Install from Community Plugins
2. Enable plugin
3. Enable "Enable JavaScript Queries" (for advanced use)
4. Enable "Enable Inline JavaScript Queries"

**Example queries for your wiki:**

**List all files in a category:**
```dataview
LIST
FROM #ballistics-armor
SORT file.name ASC
```

**Show recent daily notes:**
```dataview
LIST
FROM #daily
SORT file.name DESC
LIMIT 7
```

**Show incomplete tasks:**
```dataview
TASK
WHERE !completed
SORT due ASC
```

**Show files by source:**
```dataview
TABLE source, date
FROM "wiki"
WHERE source = "ChatGPT"
SORT date DESC
```

**Dashboard query (put in index.md):**
```dataview
TABLE file.mtime as "Last Modified", file.size as "Size"
FROM "wiki"
SORT file.mtime DESC
LIMIT 20
```

---

### 3. Tasks
**Purpose:** Task management with due dates, recurrence, queries

**Setup:**
1. Install from Community Plugins
2. Enable plugin
3. Settings → Global filter: (optional, leave blank for now)
4. Enable "Set done date on completion"

**Hotkeys to configure:**
- Toggle task: `Ctrl+Enter`
- Create or edit task: (assign custom)

**Task formats to use:**
```markdown
- [ ] Regular task
- [ ] Task with due date 📅 2026-05-20
- [ ] Task with reminder ⏰ 2026-05-20
- [ ] Recurring task 🔁 every day
- [ ] High priority ⏫
- [ ] Low priority 🔽
```

**Task queries (for daily notes):**
```tasks
not done
due before tomorrow
sort by due
```

**Overdue tasks:**
```tasks
not done
due before today
sort by due
```

---

### 4. Calendar
**Purpose:** Visual calendar for navigating daily notes

**Setup:**
1. Install from Community Plugins
2. Enable plugin
3. Settings:
   - Week start: Sunday (or Monday, your preference)
   - Daily note format: `YYYY-MM-DD`
   - Daily note folder: `Daily/` (or `wiki/daily/`)

**Usage:**
- Click any date to open/create daily note
- Red dot indicates existing note
- Shows current day highlighted

---

### 5. Graph View Customization
Already built into Obsidian core, but configure:

**Settings:**
1. Core plugins → Graph view → Enable
2. View graph → Settings (gear icon):
   - Node size: by "Links"
   - Highlight nearest: ON
   - Show orphans: OFF (cleaner view)
   - Filters: exclude `junk_drawer/`, `.obsidian/`, `.venv/`

---

## Recommended Additional Plugins

### 6. Advanced Tables
**Purpose:** Easy table editing
- Tab to navigate cells
- Auto-format on save

### 7. Excalidraw
**Purpose:** Hand-drawn style diagrams
- Create concept maps
- Visual thinking
- Export to PNG

### 8. Kanban
**Purpose:** Project boards
- Alternative to pure task lists
- Good for visual project tracking

### 9. Marp
**Purpose:** Markdown slide decks
- Create presentations from wiki content
- Export to PDF/PPTX

---

## Hotkey Summary (Configure These)

| Action | Hotkey |
|--------|--------|
| New note | Ctrl+N |
| Quick switcher | Ctrl+O |
| Global search | Ctrl+Shift+F |
| Graph view | Ctrl+G |
| Toggle edit/preview | Ctrl+E |
| Insert link | Ctrl+K |
| Insert template | Ctrl+Alt+T |
| Toggle task | Ctrl+Enter |
| Open daily note | (assign custom) |

---

## Folder Structure for Templates

```
Templates/
├── daily-note.md
├── weekly-review.md
├── meeting-note.md
├── project-note.md
├── book-note.md
└── article-note.md
```

## Daily Workflow with Plugins

**Morning:**
1. Open Calendar → Click today → Creates daily note from template
2. Tasks plugin shows overdue/ today's tasks
3. Check Dataview dashboard for priorities

**During day:**
1. Use hotkey to toggle tasks complete
2. Quick capture to daily note
3. Create meeting notes from template

**Evening:**
1. Review completed tasks
2. Fill in evening review section
3. Check graph view for new connections

---

*Setup this once, use forever.*
