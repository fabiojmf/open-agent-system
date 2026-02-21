# Open Agent System

This project uses an **Open Agent System** — a set of markdown-defined agents in `open-agents/`.

## Available Agents

| Agent | Purpose | Trigger Phrase |
|-------|---------|----------------|
| [Agent 1] (`agents/{name}.md`) | [Brief description] | "[typical user request]" |
| [Agent 2] (`agents/{name}.md`) | [Brief description] | "[typical user request]" |
| [Agent 3] (`agents/{name}.md`) | [Brief description] | "[typical user request]" |

## Routing

When a user request matches an agent's domain:

1. Read the full agent definition from `open-agents/agents/{agent}.md`
2. Follow the agent's specified behaviors and output format
3. Save outputs to the designated `open-agents/output-*/` folders
4. Commit changes following the git commit protocol in `open-agents/INSTRUCTIONS.md`

| User says... | Agent to use |
|--------------|--------------|
| "[trigger phrase]" | [Agent name] |
| "[another phrase]" | [Agent name] |

## Operating Principles

### Planning Discipline
- Create a plan before executing any non-trivial task (3+ steps or architectural decisions)
- If execution diverges from the plan, stop and re-plan — don't push through
- Plan verification steps, not just implementation steps

### Autonomous Execution
- When given a bug report or failing test: investigate and fix it without hand-holding
- Point at logs, errors, and root causes — then resolve them
- Minimize context switching required from the user

### Verification Before Done
- Never mark a task complete without demonstrating it works
- Run tests, check logs, verify the build
- Ask: "Would a senior engineer approve this?"

### Quality Standards
- Make every change as simple as possible — impact minimal code
- Find root causes — no temporary fixes
- Changes should only touch what's necessary
- For non-trivial changes, pause and consider if there's a more elegant approach
- Skip this for simple, obvious fixes — don't over-engineer

### Context Management
- Keep the main context lean — use progressive loading
- Offload research and parallel analysis to subagents when available
- One focused task per subagent

### Self-Improvement Loop
- After any correction from the user, update `open-agents/memory/lessons.md`
- Write the lesson as a rule that prevents the same mistake
- Review `open-agents/memory/lessons.md` at session start if it exists

---

**Note:** Full system documentation is in `open-agents/INSTRUCTIONS.md`. Agent definitions are loaded on demand as skills to keep context lean.
