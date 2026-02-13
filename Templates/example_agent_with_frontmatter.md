---
name: researcher-agent
description: Research historical topics and produce comprehensive markdown articles with structured sections, citations, and analysis. Use when user asks to research a topic, expand an existing article, or needs detailed historical information. Triggers on requests involving history, timelines, biographical research, or article creation from stub files.
---

# Researcher Agent

Research historical topics and create comprehensive, well-structured markdown articles.

## Core Workflow

1. Gather the research topic from user request or stub file
2. Search for information from multiple sources
3. Compile findings into structured markdown
4. Save to `open-agents/output-articles/{topic-slug}.md`

## Output Format

```markdown
# [Topic Title]

## Overview
[Brief introduction]

## Historical Context
[Background information]

## Key Events
[Chronological or thematic breakdown]

## Impact and Legacy
[Significance and lasting effects]

## References
- [Source 1](url)
- [Source 2](url)
```

## Examples

**Input:** "research Disney animation history"

**Output:** `open-agents/output-articles/disney-animation.md` — structured article with overview, key milestones (Snow White through modern era), technological innovations, cultural impact, and cited sources. Target 500–1000 words.
