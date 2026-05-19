# Daily Notes Directory

This folder contains daily notes, research suggestions, and ongoing tracking.

## Files

- **YYYY-MM-DD.md** - Daily notes created from template
- **research-suggestions.md** - Log of daily paper suggestions
- **action-tracker.md** - Running action items (if created)
- **decision-log.md** - Important decisions (if created)

## Daily Research Paper System

### Quick Start

**Run manually:**
```bash
cd /Users/josemariabarbeito/PycharmProjects/SecondBrain
python3 Scripts/automation/daily_research_paper.py
```

**Or ask Cascade:**
```
"Give me today's research paper suggestion"
```

### How It Works

1. **Analyzes your wiki** - Checks coverage across 7 knowledge domains:
   - Machine Learning
   - Process Engineering
   - Materials Science
   - Ballistics/Protection
   - Software Engineering
   - Data Science
   - History/Politics

2. **Identifies gaps** - Finds domains with low coverage

3. **Suggests a paper** - Based on gaps, suggests a specific paper to read

4. **Logs the suggestion** - Saves to `research-suggestions.md`

### Setting Up Automation

**Option 1: Run when you open daily note**
Add to your morning routine:
1. Create daily note from template
2. Run the script
3. Read suggestion
4. Decide to pursue or skip

**Option 2: Cron job (Mac/Linux)**
```bash
# Edit crontab
crontab -e

# Add line for 8am daily:
0 8 * * * cd /Users/josemariabarbeito/PycharmProjects/SecondBrain && python3 Scripts/automation/daily_research_paper.py
```

**Option 3: Cascade command**
Just ask Cascade each morning:
```
"What's my research paper for today?"
```

### After Reading a Paper

1. **Download PDF** to `raw-sources/papers/`
2. **Tell Cascade**: "Process the paper I just downloaded"
3. **Cascade will**:
   - Read and summarize
   - Create wiki page
   - Link to relevant topics
   - Update your knowledge graph

### Finding Papers

**Recommended sources by domain:**

**Machine Learning:**
- arXiv (cs.LG, cs.AI)
- Papers with Code
- Distill.pub

**Engineering:**
- Google Scholar
- ResearchGate
- AIChE Journal

**History/Politics:**
- JSTOR
- Google Scholar
- University library access

**General:**
- [arXiv.org](https://arxiv.org)
- [Google Scholar](https://scholar.google.com)
- [Semantic Scholar](https://www.semanticscholar.org)
- [Papers With Code](https://paperswithcode.com)

### Customizing Domains

Edit `Scripts/automation/daily_research_paper.py` to:
- Add new knowledge domains
- Update keywords
- Change suggested papers
- Add new sources

### Tracking Progress

Your research log shows:
- All suggestions with dates
- Which you've read
- Knowledge gaps filled over time

Review monthly:
```
"Analyze my research progress this month. What domains did I strengthen?"
```

---

*The goal: Read one paper a day that expands your knowledge in underrepresented areas.*
