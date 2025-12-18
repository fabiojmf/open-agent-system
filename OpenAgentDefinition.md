# Open Agent System Definition

A comprehensive specification for building and managing Open Agent Systems—project structures that transform AI coding assistants into general-purpose agents for any domain.

**Now fully compatible with Kiro CLI, Claude Code, Gemini CLI, and Codex.**

---

## Table of Contents

1. [What Is an Open Agent System?](#1-what-is-an-open-agent-system)
2. [Core Architecture](#2-core-architecture)
3. [Folder Structure](#3-folder-structure)
4. [Agent File Anatomy](#4-agent-file-anatomy)
5. [The Command System](#5-the-command-system)
6. [The INSTRUCTIONS.md File](#6-the-instructionsmd-file)
7. [Operations Guide](#7-operations-guide)
8. [Adding to an Existing Project](#8-adding-to-an-existing-project)
9. [Kiro CLI Integration](#9-kiro-cli-integration)
10. [Complete Example](#10-complete-example)
11. [Summary](#summary)

---

## 1. What Is an Open Agent System?

### Definition
An **Open Agent System** is a folder structure and set of markdown files that reconfigures AI coding assistants (Claude Code, Gemini CLI, Codex, **Kiro CLI**, etc.) to perform specialized, non-coding tasks. Instead of writing code, the AI manages files, performs research, transforms content, and executes domain-specific workflows.

### The Core Insight
Claude Code, Gemini CLI, Kiro CLI, and similar tools are **general-purpose agent frameworks** that happen to be configured for coding by default. Their fundamental capability is:

- Reading and writing files
- Following complex instructions
- Using tools (web search, shell commands, etc.)
- Managing context across conversations

This capability set works for *any* file-based workflow—not just code. An Open Agent System provides the structure to redirect these capabilities toward your specific domain.

### Why This Pattern Exists
**Problem:** Building custom AI agents requires software engineering—writing code, managing deployments, building UIs, maintaining infrastructure.

**Solution:** Open Agent Systems let you define agent behavior in markdown files. No code required. The AI reads your instructions and becomes that agent.

**Benefit:** You can create sophisticated multi-agent workflows using nothing but folders and markdown files, runnable in any AI coding assistant.

### Tool Agnosticism
A key feature of Open Agent Systems is **tool agnosticism**. The same system works with:
- Claude Code (via `CLAUDE.md`)
- Codex (via `AGENTS.md`)
- Gemini CLI (via `GEMINI.md`)
- **Kiro CLI** (via `.kiro/steering/` + `AGENTS.md`)

All entry points lead to the same `INSTRUCTIONS.md` file. You write your agents once and use them with any tool.

---

## 2. Core Architecture

### The Pointer Pattern
Open Agent Systems use a three-layer architecture:

```
┌───────────────────────────────────────────────────────────────────────────┐
│  CLAUDE.md / AGENTS.md / GEMINI.md / .kiro/steering/                      │
│  (Tool-specific entry points - augmented with pointer)                    │
└────────────────────────────────┬──────────────────────────────────────────┘
                                 │
                                 ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                    open-agents/INSTRUCTIONS.md                             │
│  (Agent index: lists all agents with descriptions)                        │
│  (Routing logic: when to use which agent)                                 │
│  (Loaded into context at conversation start)                              │
└────────────────────────────────┬──────────────────────────────────────────┘
                                 │
                                 ▼ (on demand only)
┌───────────────────────────────────────────────────────────────────────────┐
│  open-agents/agents/researcher.md    transformer.md    ...                │
│  (Full agent definitions - loaded when triggered)                         │
└───────────────────────────────────────────────────────────────────────────┘
```

### Critical: The Mandatory Read Directive
**This is the most important requirement of the entire system.**

Each entry point file MUST include a read directive at the top. Without this, the agent system won't function.

#### Required Format

```markdown
**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**
```

That's it. One line. The AI will read the file and understand the system.

#### Creating Entry Point Files

When setting up an Open Agent System, **always create entry point files if they don't exist**:

| Tool | Entry Point File |
|------|------------------|
| Claude Code | `CLAUDE.md` |
| Codex | `AGENTS.md` |
| Gemini CLI | `GEMINI.md` |
| **Kiro CLI** | `.kiro/steering/agents.md` + `AGENTS.md` |

A minimal entry point file is just:

```markdown
**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**
```

If the project already has these files, add the directive at the top.

### Why This Pattern?
**Progressive Disclosure:** Agent definitions can be large (hundreds of lines). Loading all agents into context at once wastes tokens and creates noise. Instead:

1. At conversation start, only `INSTRUCTIONS.md` is loaded
2. `INSTRUCTIONS.md` contains brief descriptions of each agent
3. Full agent files are loaded only when that agent is triggered

**Context Management:** AI assistants have limited context windows. The pointer pattern keeps initial context small while allowing complex agent definitions.

**Single Source of Truth:** All tool-specific entry points point to the same instructions. Update once, works everywhere.

**Non-Disruptive:** The Open Agent System lives in its own folder (`open-agents/`) and augments existing project files rather than replacing them.

### Layer Responsibilities
| Layer | File(s) | Responsibility |
|-------|---------|----------------|
| Entry | `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.kiro/steering/` | Tool detection, pointer to instructions |
| Index | `open-agents/INSTRUCTIONS.md` | Agent catalog, routing logic, workflow docs |
| Agents | `open-agents/agents/*.md` | Full agent definitions, behaviors, formats |

---

## 3. Folder Structure

### The open-agents/ Container
Open Agent Systems live in a single `open-agents/` folder at the project root. This isolates the agent system from the rest of the project and prevents conflicts with existing files.

```
existing-project/
├── (existing project files...)
├── CLAUDE.md                    # Augmented with pointer
├── AGENTS.md                    # Augmented with pointer
├── GEMINI.md                    # Augmented with pointer
│
├── .kiro/                       # Kiro CLI configuration
│   ├── agents/                  # Kiro agent drivers (JSON)
│   │   └── {agent}.json         # Points to open-agents/agents/{agent}.md
│   └── steering/                # Kiro steering files
│       ├── agents.md            # Open Agent pointer for Kiro
│       ├── product.md           # Optional: Product context
│       ├── tech.md              # Optional: Tech stack
│       └── structure.md         # Optional: Project structure
│
├── .claude/commands/            # Claude Code commands
│   └── {domain}/
│       └── {command}.md
│
├── .gemini/commands/            # Gemini CLI commands
│   └── {domain}/
│       └── {command}.md
│
└── open-agents/                 # The agent system container
    ├── README.md                # Human-readable intro
    ├── INSTRUCTIONS.md          # Agent index and routing
    │
    ├── agents/                  # Agent definitions
    │   ├── researcher.md
    │   ├── transformer.md
    │   └── publisher.md
    │
    ├── tools/                   # Agent-created scripts (optional)
    │   └── (scripts created by agents)
    │
    ├── source/                  # User inputs
    │   └── (raw materials, requests, stubs)
    │
    ├── output-drafts/           # First-stage outputs
    │   └── (initial processing results)
    │
    ├── output-refined/          # Second-stage outputs
    │   └── (refined, reviewed content)
    │
    └── output-final/            # Final deliverables
        └── (publication-ready materials)
```

### Why This Structure?
1. **Isolation:** The entire agent system is contained in one folder
2. **Non-disruptive:** Doesn't overwrite existing project files
3. **Portable:** Can be copied between projects
4. **Clear separation:** Agent system vs. project code is obvious
5. **Kiro Compatible:** `.kiro/steering/` provides native Kiro integration

### Folder Purposes
| Folder | Purpose | Example Contents |
|--------|---------|------------------|
| `agents/` | Agent definitions | `researcher.md`, `transformer.md` |
| `tools/` | Scripts created by agents | `compress_audio.sh`, `resize_image.py` |
| `source/` | Raw inputs from user | Notes, stubs, requests, reference materials |
| `output-drafts/` | First processing stage | Drafts, initial transforms, rough outputs |
| `output-refined/` | Intermediate stage | Reviewed, refined, or transformed outputs |
| `output-final/` | Final deliverables | Publication-ready materials |

### Domain-Specific Naming
Rename output folders to match your domain:

**Video Production:**
```
output-scripts/
output-production/
output-final/
```

**Research Project:**
```
output-notes/
output-analysis/
output-papers/
```

**Content Creation:**
```
output-drafts/
output-reviewed/
output-published/
```

---

## 4. Agent File Anatomy

### What Makes an Agent File
An agent file is a markdown document in `open-agents/agents/` that defines:
- What the agent does
- When it should be activated
- How it should behave
- What output it produces
- Where output goes

### Required Sections
Every agent file should contain these sections:

```markdown
# [Agent Name]

[1-2 sentence description of what this agent does]

---

## Purpose

[Expanded description: what problem does this agent solve?
What is its role in the system? What makes it valuable?]

---

## When to Use This Agent

Use this agent when the user:
- [Trigger phrase or condition]
- [Another trigger]
- [Another trigger]

---

## Core Behaviors

### 1. [First Behavior]
[Description of what the agent does]

### 2. [Second Behavior]
[Description]

### 3. [Third Behavior]
[Description]

---

## Output Format

[Define the structure of what the agent produces.
Use code blocks to show templates if helpful.]

---

## Output Location

Save outputs to: `open-agents/[folder]/[filename_pattern]`

Examples:
- `open-agents/output-drafts/example_filename.ext`
- `open-agents/output-final/another_example.ext`

---

## Examples

[Optional but recommended: show example inputs and outputs]

> Example prompt: "[user request]"
> Example output: [what the agent would produce]
```

### Agent Design Principles
**1. Single Responsibility**
Each agent should do one thing well. If an agent does too much, split it.

**2. Clear Triggers**
Make it obvious when this agent should be used vs. another. The "When to Use" section is critical for routing.

**3. Explicit Output Location**
Always tell the agent where to save its work. Ambiguity causes confusion.

**4. Behavioral, Not Technical**
Describe what the agent should *do*, not how it should *implement*. Let the AI figure out implementation.

**5. Include Examples**
Examples are the most effective way to communicate expectations. Include at least one.

**6. Consider Tool Creation**
Agents may benefit from writing their own scripts/tools for repeatable operations.

### Agent-Created Tools

Agents can create their own scripts and tools to handle repeatable operations more efficiently.

#### When to Create Tools

Consider tool creation when an agent:
- Performs the same file manipulation repeatedly (resize images, compress audio, convert formats)
- Executes complex shell commands that are error-prone to generate each time
- Needs precise, deterministic behavior (not probabilistic LLM output)
- Would benefit from faster execution (scripts run faster than LLM reasoning)

#### Tool Location

Store agent tools in a `tools/` subfolder within `open-agents/`:

```
open-agents/
├── INSTRUCTIONS.md
├── agents/
│   ├── audio_processor.md
│   └── image_optimizer.md
└── tools/
    ├── compress_audio.sh
    ├── resize_image.py
    └── convert_format.js
```

#### Referencing Tools in Agent Files

When an agent has associated tools, document them:

```markdown
## Available Tools

This agent has access to the following scripts:

### `open-agents/tools/compress_audio.sh`
Compresses audio files to a target bitrate.
Usage: `./open-agents/tools/compress_audio.sh <input> <output> <bitrate>`

### `open-agents/tools/normalize_volume.sh`
Normalizes audio volume to -14 LUFS.
Usage: `./open-agents/tools/normalize_volume.sh <input> <output>`

When performing these operations, use the scripts rather than
constructing the ffmpeg commands manually each time.
```

---

## 5. The Command System

### What Commands Are
Commands provide **predictable invocation** of agents. Instead of hoping the AI recognizes a trigger phrase, you can explicitly call:

```
/history research Disney animation
/history html disney_animation.md
/history extract disney_animation.md
```

### Parallel Command Structures
Open Agent Systems maintain commands for multiple tools:

```
.claude/commands/           # Claude Code commands
└── {domain}/
    ├── {command1}.md
    └── {command2}.md

.gemini/commands/           # Gemini CLI commands
└── {domain}/
    └── (same structure)
```

> **Note for Kiro CLI:** Kiro uses the steering system rather than slash commands. See [Section 9: Kiro CLI Integration](#9-kiro-cli-integration).

Commands are organized by domain (e.g., `history/`, `video/`, `research/`).

### Command File Structure
Commands are simple—they instruct the AI to use an agent:

```markdown
[Brief description of what this command does]

Follow the instructions in `open-agents/agents/{name}.md` to complete this task.

$ARGUMENTS
```

The `$ARGUMENTS` placeholder passes any user input after the command name.

### Example Command
`.claude/commands/history/research.md`:
```markdown
Research a historical topic and create a comprehensive article.

Follow the instructions in `open-agents/agents/researcher.md`.

$ARGUMENTS
```

The same file should exist at `.gemini/commands/history/research.md`.

### Why Both Claude and Gemini Commands?
**Tool Agnosticism:** Users should be able to use their preferred tool. Maintaining both command structures ensures the system works regardless of which AI assistant is used.

**Identical Content:** The command files are usually identical between `.claude/` and `.gemini/`. When you create or update a command, update both locations.

### Command Naming Conventions
**Structure:** `.claude/commands/{domain}/{action}.md`
- `{domain}` = the subject area (history, video, research, etc.)
- `{action}` = what the command does (research, transform, publish)

**Examples:**
- `/history research` → `.claude/commands/history/research.md`
- `/video critique` → `.claude/commands/video/critique.md`

---

## 6. The INSTRUCTIONS.md File

### The Heart of the System
`INSTRUCTIONS.md` is the most important file in an Open Agent System. It:
- Describes the system's purpose
- Lists all available agents
- Defines routing logic
- Documents workflow
- Sets behavioral rules (like git commit protocol)

### Required Sections
```markdown
# [System Name]

[Brief description of what this system does]

---

## How This System Works

[Explain the pointer pattern, progressive disclosure]

---

## Project Structure

[Document the folder structure with descriptions]

---

## Available Agents

### 1. [Agent Name] (`agents/file.md`)

**Purpose:** [What it does]

**When to use:**
- [Trigger conditions]

**Output:** [Where results go]

**To use this agent:** Read `open-agents/agents/file.md`

### 2. [Next Agent]
...

---

## Routing Logic

| User says... | Agent to use |
|--------------|--------------|
| "[trigger phrase]" | [Agent name] |
| "[another phrase]" | [Agent name] |

---

## Git Commit Protocol

[Define when and how to commit]

---

## File Naming Conventions

[Define naming patterns]

---

## Quick Start

[Brief getting-started guide]
```

### Agent Descriptions in INSTRUCTIONS.md
Each agent entry should be brief but complete enough for routing:

```markdown
### 1. The Researcher (`agents/researcher.md`)

**Purpose:** Research historical topics and produce rich markdown articles.

**When to use:**
- User asks to "research" a topic
- User asks to "expand" or "deepen" an article
- User asks to "write about" something
- User provides a stub file

**Output:** Markdown files in `open-agents/output-articles/`

**To use this agent:** Read `open-agents/agents/researcher.md`
```

### The Routing Table
The routing table helps the AI decide which agent to invoke:

```markdown
## Routing Logic

| User says... | Agent to use |
|--------------|--------------|
| "Research the history of X" | Researcher |
| "Expand this article" | Researcher |
| "Create an HTML page from this" | HTML Generator |
| "Extract the data into JSON" | Data Extractor |
| "Create all outputs for this" | Researcher → HTML → Extractor (chain) |
```

### Workflow Documentation
If agents can be chained, document the workflow:

```markdown
## Workflow

A common flow through this system:

1. **Research:** User provides a topic → Researcher creates article
2. **Transform:** Article → HTML Generator creates webpage
3. **Extract:** Article → Data Extractor creates JSON

Agents can be used independently or in sequence.
```

---

## 7. Operations Guide

### Creating a New Open Agent System
Follow these steps to create a system from scratch:

#### Step 1: Create Folder Structure

```bash
# Create open-agents structure
mkdir -p open-agents/{agents,tools,source,output-drafts,output-refined,output-final}

# Create command folders for Claude and Gemini
mkdir -p .claude/commands/{domain}
mkdir -p .gemini/commands/{domain}

# Create Kiro folders (for Kiro CLI compatibility)
mkdir -p .kiro/steering
mkdir -p .kiro/agents
```

#### Step 2: Create the README.md

Create `open-agents/README.md`:
```markdown
# Open Agent System

This folder contains an **Open Agent System**—a collection of markdown-defined agents that transform AI coding assistants into specialized tools for [your domain].

## What's Here

- `INSTRUCTIONS.md` — Full documentation, agent index, and routing logic
- `agents/` — Individual agent definitions
- `source/` — Input materials
- `output-*/` — Processing stages

## Quick Start

Read `INSTRUCTIONS.md` for available agents and how to use them.
```

#### Step 3: Create INSTRUCTIONS.md

Create `open-agents/INSTRUCTIONS.md` with:
- System description
- Project structure documentation
- Agent index (initially empty or with planned agents)
- Routing logic
- Git commit protocol

#### Step 4: Create Agent Files

For each agent, create `open-agents/agents/{name}.md` with:
- Purpose
- When to use
- Core behaviors
- Output format
- Output location

#### Step 5: Create Command Files

For each agent, create commands in both:
- `.claude/commands/{domain}/{command}.md`
- `.gemini/commands/{domain}/{command}.md`

#### Step 6: Create Entry Point Files

Create or update the following entry point files at project root:

**CLAUDE.md, AGENTS.md, GEMINI.md:**
```markdown
**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**
```

**For Kiro CLI** - Create `.kiro/steering/agents.md`:
```markdown
# Open Agent System

**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**

This project uses an Open Agent System for specialized, non-coding tasks.
When the user invokes an agent workflow, follow the routing and instructions defined in the INSTRUCTIONS.md file.
```

### Adding an Agent to an Existing System

#### Step 1: Create the Agent File

Create `open-agents/agents/{name}.md` following the agent anatomy template.

#### Step 2: Create Command Files

Create `.claude/commands/{domain}/{command}.md`:
```markdown
[Brief description]

Follow the instructions in `open-agents/agents/{name}.md`.

$ARGUMENTS
```

Create identical file in `.gemini/commands/{domain}/`.

#### Step 3: Update INSTRUCTIONS.md

Add an entry to the "Available Agents" section and add routing entries to the routing table.

#### Step 4: Commit

```bash
git add open-agents/agents/{name}.md
git add .claude/commands/{domain}/{command}.md
git add .gemini/commands/{domain}/{command}.md
git add open-agents/INSTRUCTIONS.md
git commit -m "Add {agent name} agent"
```

### Editing an Existing Agent

1. **Locate Files:** Find both the definition (`open-agents/agents/{name}.md`) and commands
2. **Understand Current Behavior:** Read the files
3. **Make Changes:** Edit the agent file to modify behavior
4. **Update Routing (if needed):** If triggers changed, update `open-agents/INSTRUCTIONS.md`
5. **Commit:** `git commit -m "Update {agent name}: {what changed}"`

### Removing an Agent

```bash
rm open-agents/agents/{name}.md
rm .claude/commands/{domain}/{command}.md
rm .gemini/commands/{domain}/{command}.md
```

Update INSTRUCTIONS.md to remove the entry and routing entries, then commit.

### Redefining the System

To completely change the system's purpose:

1. **Plan the New Configuration:** Decide what agents are needed
2. **Update Folder Structure:** Rename output folders to match the new domain
3. **Replace Agents:** Either modify existing agents or delete and create new ones
4. **Update All Documentation:** INSTRUCTIONS.md, README.md, entry point files
5. **Clean Up:** Remove old content from source and output folders

---

## 8. Adding to an Existing Project

Open Agent Systems are designed to **augment** existing projects without disrupting them.

### The Augmentation Approach
Instead of replacing existing entry point files, **append** a section that points to the Open Agent System:

```markdown
---

## Open Agents

This project includes an **Open Agent System** for [brief description of what the agents do].

**To use the agent system:** Read `open-agents/INSTRUCTIONS.md`

### Quick Reference

| Agent | Trigger | Output |
|-------|---------|--------|
| [Agent 1] | "[trigger phrase]" | `open-agents/output-*/` |
| [Agent 2] | "[trigger phrase]" | `open-agents/output-*/` |
```

### Step-by-Step Integration

1. **Create the open-agents/ folder:** `mkdir -p open-agents/{agents,tools,source,output-drafts,output-refined,output-final}`
2. **Create open-agents/README.md:** Human-readable context
3. **Create open-agents/INSTRUCTIONS.md:** Full instructions file
4. **Create agent files:** Add agents to `open-agents/agents/`
5. **Create slash commands:** Add commands to `.claude/commands/` and `.gemini/commands/`
6. **Create or update entry point files:** Add the mandatory read directive

### What NOT to Do
- **Don't replace** existing `CLAUDE.md` content—append to it
- **Don't put agent files** at project root—keep them in `open-agents/`
- **Don't modify** the project's existing folder structure
- **Don't add** numbered prefixes to existing project folders

### Verifying the Integration
After integration, confirm:

1. `open-agents/README.md` exists and is human-readable
2. `open-agents/INSTRUCTIONS.md` lists all agents
3. Entry point files (`CLAUDE.md`, etc.) have the Open Agents section
4. `.kiro/steering/agents.md` exists (for Kiro compatibility)
5. Slash commands exist in `.claude/commands/` and `.gemini/commands/`
6. Running `/your-domain command` invokes the correct agent

---

## 9. Kiro CLI Integration

### What is Kiro Steering?

**Steering** gives Kiro persistent knowledge about your project through markdown files in `.kiro/steering/`. Instead of explaining your conventions in every chat, steering files ensure Kiro consistently follows your established patterns, libraries, and standards.

### Key Benefits
- **Consistent Code Generation** - Every component follows your team's established patterns
- **Reduced Repetition** - No need to explain project standards in each conversation
- **Team Alignment** - All developers work with the same standards
- **Scalable Project Knowledge** - Documentation grows with your codebase

### Kiro Steering vs Other Entry Points

| Tool | Entry Point | Mechanism |
|------|-------------|-----------|
| Claude Code | `CLAUDE.md` | Root file, auto-read |
| Codex | `AGENTS.md` | Root file, auto-read |
| Gemini CLI | `GEMINI.md` | Root file, auto-read |
| **Kiro CLI** | `.kiro/steering/*.md` | Steering folder, always included |

**Important:** Unlike single entry point files, Kiro uses a **folder of steering files**. Additionally, Kiro automatically imports `AGENTS.md` files from the workspace root.

### Setting Up the Steering Folder

```bash
mkdir -p .kiro/steering
```

### The Agents Steering File

Create `.kiro/steering/agents.md`:

```markdown
# Open Agent System

**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**

This project uses an **Open Agent System** for specialized, non-coding tasks.

## Available Agents

| Agent | Purpose | Trigger Phrase |
|-------|---------|----------------|
| [Agent 1] | [Brief description] | "[typical user request]" |
| [Agent 2] | [Brief description] | "[typical user request]" |

## How to Use

When a user request matches an agent's domain:
1. Read the full agent definition from `open-agents/agents/{agent}.md`
2. Follow the agent's specified behaviors and output format
3. Save outputs to the designated `open-agents/output-*/` folders
```

### Foundational Steering Files (Optional but Recommended)

These files provide Kiro with essential project context:

| File | Purpose |
|------|---------|
| `product.md` | Product's purpose, target users, key features |
| `tech.md` | Frameworks, libraries, technical constraints |
| `structure.md` | File organization, naming conventions |

See the `Templates/` folder for ready-to-use templates.

### Workspace vs Global Steering

| Scope | Location | Use For |
|-------|----------|---------|
| Workspace | `.kiro/steering/` (project root) | Project-specific agents |
| Global | `~/.kiro/steering/` (home) | Universal preferences |
| Team | Downloaded to `~/.kiro/steering/` | Organization-wide standards |

**Priority:** Workspace steering overrides global steering when they conflict.

### The .kiro/agents/ Folder (Driver Pattern)

In addition to steering files, Kiro supports a dedicated agents folder where JSON files act as **Drivers** that point to your agent definitions.

#### The Concept

JSON files in `.kiro/agents/` don't contain intelligence—they only point to the "Source of Truth" (your Markdown files in `open-agents/agents/`).

#### Folder Structure

```
your-project/
├── .kiro/
│   └── agents/
│       ├── architect.json    ← Driver (points to MD using "../../")
│       └── backend.json      ← Driver (points to MD using "../../")
├── open-agents/
│   └── agents/
│       ├── architect.md      ← Brain (actual prompt)
│       └── backend.md        ← Brain (actual prompt)
```

#### The JSON Pattern

Create a `.json` file for each agent in `.kiro/agents/`:

```json
{
  "name": "architect",
  "description": "OCAI Architect - System Design",
  "prompt": "file://../../open-agents/agents/architect.md",
  "allowedTools": ["read_file", "write_file", "list_files"]
}
```

#### Why `../../`?

Kiro resolves paths relative to the JSON file location:

1. First `../` → from `agents/` to `.kiro/`
2. Second `../` → from `.kiro/` to project root
3. From root → `open-agents/agents/architect.md`

#### Setting Up the Agents Folder

```bash
mkdir -p .kiro/agents
```

Then create a JSON driver for each agent you want to expose to Kiro.

### Best Practices for Kiro Integration

1. **Keep Files Focused** - One domain per file
2. **Use Clear Names** - `agents.md`, `api-standards.md`, `testing-patterns.md`
3. **Include Context** - Explain *why* decisions were made
4. **Reference Files** - Use `#[[file:path/to/example.tsx]]` syntax
5. **Security First** - Never include API keys or secrets
6. **Maintain Regularly** - Update after architecture changes

---

## 10. Complete Example

### History Research System

A working Open Agent System for researching historical topics:

#### Folder Structure

```
my-existing-project/
├── src/                         # Existing project code
├── package.json                 # Existing project files
├── CLAUDE.md                    # Augmented with Open Agents section
├── AGENTS.md                    # Augmented with Open Agents section
├── GEMINI.md                    # Augmented with Open Agents section
│
├── .kiro/                       # Kiro CLI configuration
│   ├── agents/                  # Agent drivers
│   │   ├── researcher.json
│   │   ├── html_generator.json
│   │   └── data_extractor.json
│   └── steering/
│       ├── agents.md            # Open Agent pointer
│       ├── product.md           # Product context
│       └── tech.md              # Tech stack
│
├── .claude/commands/
│   └── history/
│       ├── research.md
│       ├── html.md
│       └── extract.md
│
├── .gemini/commands/
│   └── history/
│       └── (same structure)
│
└── open-agents/
    ├── README.md
    ├── INSTRUCTIONS.md
    │
    ├── agents/
    │   ├── researcher.md
    │   ├── html_generator.md
    │   └── data_extractor.md
    │
    ├── source/
    │   ├── disney_animation.md      # Stub file
    │   └── video_games.md           # Stub file
    │
    ├── output-articles/
    ├── output-html/
    └── output-data/
```

#### Entry Point File (CLAUDE.md)

```markdown
**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**

[... any existing project instructions ...]

### Quick Reference

| Agent | Trigger | Output |
|-------|---------|--------|
| Researcher | "research [topic]" | `open-agents/output-articles/` |
| HTML Generator | "create HTML from [file]" | `open-agents/output-html/` |
| Data Extractor | "extract data from [file]" | `open-agents/output-data/` |

### Available Commands

#### Codex
- `/history research [topic]` — Research and create article
- `/history html [file]` — Generate HTML from article
- `/history extract [file]` — Extract structured JSON

#### Kiro CLI
- `kiro-cli --agent researcher` — Research and create article
- `kiro-cli --agent html_generator` — Generate HTML from article
- `kiro-cli --agent data_extractor` — Extract structured JSON

#### Claude Code / Gemini CLI
- "research [topic]" — Research and create article
- "create HTML from [file]" — Generate HTML from article
- "extract data from [file]" — Extract structured JSON
```

#### Kiro Steering File (.kiro/steering/agents.md)

```markdown
# Open Agent System

**CRITICAL: Read `open-agents/INSTRUCTIONS.md` immediately.**

This project includes an Open Agent System for historical research.

## Available Agents

| Agent | Purpose | Trigger |
|-------|---------|---------|
| Researcher | Create comprehensive markdown articles | "research [topic]" |
| HTML Generator | Transform articles into themed webpages | "create HTML from [file]" |
| Data Extractor | Extract structured JSON from articles | "extract data from [file]" |

When the user invokes any agent workflow, follow the routing and instructions defined in `open-agents/INSTRUCTIONS.md`.
```

#### open-agents/INSTRUCTIONS.md

```markdown
# History Research System

An open agent system for researching historical topics.

---

## How This System Works

1. **Entry points** (CLAUDE.md/AGENTS.md/GEMINI.md/.kiro/steering/) point here
2. **This file** is the index—it describes available agents
3. **Agent files** load on demand when triggered

---

## Available Agents

### 1. The Researcher (`agents/researcher.md`)

**Purpose:** Research historical topics and produce rich markdown articles.

**When to use:**
- User asks to "research" a topic
- User asks to "expand" an existing article
- User provides a stub file

**Output:** Markdown files in `open-agents/output-articles/`

### 2. The HTML Generator (`agents/html_generator.md`)

**Purpose:** Transform markdown articles into themed HTML pages.

**When to use:**
- User asks to "create HTML"
- User asks to "make a webpage"

**Output:** HTML files in `open-agents/output-html/`

### 3. The Data Extractor (`agents/data_extractor.md`)

**Purpose:** Extract structured JSON from articles.

**When to use:**
- User asks to "extract data"
- User asks to "create JSON"

**Output:** JSON files in `open-agents/output-data/`

---

## Routing Logic

| User says... | Agent |
|--------------|-------|
| "Research the history of X" | Researcher |
| "Expand this article" | Researcher |
| "Create HTML from this" | HTML Generator |
| "Extract data into JSON" | Data Extractor |
| "Create all outputs" | Researcher → HTML → Extractor |
```

---

## Summary

An Open Agent System consists of:

1. **A container folder** (`open-agents/`) that isolates the system
2. **A README.md** for human-readable orientation
3. **An INSTRUCTIONS.md** that catalogs agents and routes requests
4. **Agent definitions** (`agents/*.md`) that define specialized behaviors
5. **Commands** (`.claude/commands/`, `.gemini/commands/`) for explicit invocation
6. **Kiro steering files** (`.kiro/steering/`) for Kiro CLI compatibility
7. **Structured folders** (`source/`, `output-*/`) for organized workflow
8. **Entry point files** (CLAUDE.md, AGENTS.md, GEMINI.md) with the read directive

**Critical:** Entry points must contain the mandatory read directive at the top. Create these files if they don't exist.

The pattern enables:
- **Tool agnosticism:** Works with Claude Code, Gemini CLI, Codex, Kiro CLI
- **Progressive disclosure:** Only loads what's needed
- **Domain flexibility:** Reconfigurable for any file-based workflow
- **Non-disruptive integration:** Adds to existing projects without conflict
- **Self-modification:** Can add, edit, and remove agents

---

*This definition document describes the Open Agent System specification with Kiro CLI compatibility.*
