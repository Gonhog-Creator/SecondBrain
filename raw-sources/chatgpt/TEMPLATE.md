# Chat Conversation Template

Use this template when manually saving important ChatGPT or Claude conversations.

## Filename Format
`YYYY-MM-DD-brief-topic.md`

Examples:
- `2026-05-18-machine-learning-basics.md`
- `2026-05-17-project-planning.md`
- `2026-05-16-debugging-python.md`

## Template

```markdown
---
date: 2026-05-18
source: ChatGPT  # or Claude
platform: web    # or mobile, API
topic: [main topic]
tags: [tag1, tag2, tag3]
---

# [Brief Title of Conversation]

## My Questions
1. [What you asked]
2. [What you asked]

## Key Insights
- [Important point 1]
- [Important point 2]
- [Important point 3]

## Full Conversation

**Me:** [Your question]

**AI:** [AI's response]

**Me:** [Follow-up]

**AI:** [Response]

...

## Action Items
- [ ] [Something to follow up on]
- [ ] [Something to research further]

## Related Topics
- [[topic-1]]
- [[topic-2]]
```

## Tips

- **Be selective**: Don't save every conversation. Save ones where you learned something new.
- **Add context**: Briefly summarize what you were trying to accomplish.
- **Tag it**: Use consistent tags for easier retrieval later.
- **Link it**: Connect to related concepts in your wiki.
- **Date it**: Always include the date - AI knowledge changes over time.

## After Saving

1. Save this file to `raw-sources/chatgpt/` or `raw-sources/claude/`
2. Tell me: "Process the new conversation in raw-sources/"
3. I'll integrate it into your wiki
