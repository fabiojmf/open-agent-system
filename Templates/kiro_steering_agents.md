# Open Agent System

**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**
**At session start:** Review `open-agents/memory/lessons.md` if it exists.

This project uses an **Open Agent System** for specialized, non-coding tasks.

## System Overview

The Open Agent System transforms AI coding assistants into domain-specific agents that:
- Manage files and content
- Perform research and analysis
- Transform documents between formats
- Execute domain-specific workflows

## Available Agents

| Agent | Purpose | Trigger Phrase |
|-------|---------|----------------|
| [Agent 1] | [Brief description] | "[typical user request]" |
| [Agent 2] | [Brief description] | "[typical user request]" |
| [Agent 3] | [Brief description] | "[typical user request]" |

## How to Use

When a user request matches an agent's domain:

1. Read the full agent definition from `open-agents/agents/{agent}.md`
2. Follow the agent's specified behaviors and output format
3. Save outputs to the designated `open-agents/output-*/` folders
4. Commit changes following the git commit protocol in INSTRUCTIONS.md

## Routing

Check `open-agents/INSTRUCTIONS.md` for the complete routing table that maps user requests to specific agents.

## Output Locations

All agent outputs go to subdirectories within `open-agents/`:
- **Drafts**: `open-agents/output-drafts/`
- **Refined**: `open-agents/output-refined/`
- **Final**: `open-agents/output-final/`


---

**Note:** This steering file provides high-level context. Full agent definitions are loaded on demand as skills to keep context lean.
