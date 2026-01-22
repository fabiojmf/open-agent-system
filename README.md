# Open Agent System (Kiro CLI Compatible)

> Transform AI coding assistants into specialized domain agents using markdown files and folder structure. No code required.

This is a Kiro CLI compatible version of the [Open Agent System](https://github.com/bladnman/open-agent-system), enhanced with Anthropic's skill-creator tooling for advanced use cases.

---

## 🎯 What Is This?

**The Problem:**  
Building custom AI agents requires software engineering—code, deployments, UIs, infrastructure.

**The Solution:**  
Open Agent System lets you define multi-agent workflows in markdown files. The AI reads your instructions and becomes that agent.

**This Version:**  
- ✅ Full Open Agent System specification
- ✅ Kiro CLI integration (steering + agents)
- ✅ Skills support (progressive loading)
- ✅ Skill Creator tooling (bundled resources)
- ✅ Compatible with Claude Code, Gemini CLI, Codex

---

## 🙏 Credits

**Open Agent System** by [@bladnman](https://github.com/bladnman):
- **Repository**: https://github.com/bladnman/open-agent-system
- **Original Definition**: [OpenAgentDefinition.md](https://github.com/bladnman/open-agent-system/blob/main/OpenAgentDefinition.md)

**Skill Creator** by [Anthropic](https://github.com/anthropics/skills):
- **Repository**: https://github.com/anthropics/skills/tree/main/skills/skill-creator
- **Documentation**: https://code.claude.com/docs/en/skills

---

## 🚀 Quick Start

### Using This to Bootstrap a New Project

You can use this Open Agent System to generate the complete agent infrastructure for your new software project. Simply provide this repository URL to your AI assistant:

**Example prompt:**

```
Create a Python + FastAPI project for managing poker game groups and tournaments. 
Use https://github.com/fabiojmf/open-agent-system as the foundation to set up 
the complete Open Agent System structure with:

- Agent definitions for architecture, backend, and testing
- Kiro CLI configuration with skills and proper tool permissions
- Steering files for product context and tech stack
- YAML frontmatter for progressive context loading

Then scaffold the FastAPI application structure around it.
```

**What you'll get:**
- ✅ Complete `.kiro/` configuration (agents, steering, skills)
- ✅ `open-agents/` folder with agent definitions
- ✅ Entry point files (AGENTS.md, CLAUDE.md, GEMINI.md)
- ✅ Your software project structure
- ✅ Ready to use with Kiro CLI, Claude Code, Codex, or Gemini CLI

### Manual Setup

```bash
# 1. Create your project structure
project/
├── open-agents/
│   ├── INSTRUCTIONS.md      # Router with agent routing logic
│   └── agents/
│       ├── researcher.md    # Agent definitions
│       └── architect.md
└── .kiro/
    ├── steering/
    │   └── agents.md        # Points to INSTRUCTIONS.md
    └── agents/
        └── default.json     # Kiro agent configuration
```

```json
// .kiro/agents/default.json
{
  "prompt": "file://../../open-agents/INSTRUCTIONS.md",
  "resources": [
    "skill://../../open-agents/agents/*.md"
  ]
}
```

**Learn more:** Follow the complete guide in `OpenAgentDefinition.md`

---

## 📚 Core Concepts

### 1. Open Agent System (The Foundation)

Multi-agent routing with explicit control:

```
open-agents/
├── INSTRUCTIONS.md          # Central router
└── agents/
    ├── researcher.md        # Specialized agents
    ├── architect.md
    └── backend.md
```

**When to use:** You need multiple specialized agents with explicit routing logic.

**Learn more:** Sections 1-9 in OpenAgentDefinition.md

---

### 2. Skills (Progressive Loading)

Add YAML frontmatter to agent files for on-demand loading:

```markdown
---
name: researcher
description: Research topics and create articles. Use when user asks to research.
---

# Researcher Agent
[Full definition loaded only when needed]
```

**When to use:** Keep context lean by loading agent definitions on demand.

**Learn more:** Section 4.1 in OpenAgentDefinition.md

---

### 3. Skill Creator (Advanced Tooling)

**Two approaches available:**

#### Approach A: Skill Creator Agent (Recommended)

Interactive, intelligent skill creation with no manual editing:

```
User: "create a skill for backend in Java, Spring Boot"

Agent:
✅ Asks clarifying questions
✅ Generates complete content (NO TODOs)
✅ Creates supporting files if needed
✅ Validates automatically
✅ Reports completion

Result: Production-ready skill, no manual editing required
```

**During project bootstrap:**
```
User: Create study routine app using https://github.com/fabiojmf/open-agent-system

AI:
✅ Project structure created
📋 Suggested skills based on your description:
   1. mobile-ui-components
   2. study-analytics
   3. notification-scheduler
   
Would you like me to create these? (yes)

✅ All skills created and validated
🎯 Your Open Agent System is ready!
```

**Learn more:** See `Templates/skill-creator-agent.md`

#### Approach B: Python Scripts (Optional)

For users who prefer command-line tools or need CI/CD integration:

```bash
# 1. Create skill structure (generates template)
python scripts/init_skill.py --path ./skills/pdf-editor

# Structure created:
skills/pdf-editor/
├── SKILL.md              # Template with TODOs - YOU EDIT THIS
├── scripts/              # Add your Python/Bash scripts here
├── references/           # Add detailed docs here
└── assets/               # Add templates/files here

# 2. Edit SKILL.md manually
# Replace TODOs with your actual skill content:
# - Update description (this triggers the skill)
# - Write "When to Use" scenarios
# - Define the workflow
# - Add code examples/patterns

# 3. Validate (checks for TODOs and format)
python scripts/quick_validate.py ./skills/pdf-editor

# 4. Package for distribution
python scripts/package_skill.py ./skills/pdf-editor
# Creates: pdf-editor.skill (distributable zip)
```

**When to use scripts:**
- CI/CD pipelines (automated validation)
- Distribution (packaging skills)
- Prefer command-line tools

**When to use agent:**
- Interactive creation
- Need help with content
- Want automatic suggestions
- Bootstrap new projects

---

## 🔧 Usage Patterns

### Pattern A: Open Agent System Only
```
Use INSTRUCTIONS.md for routing
Define agents in markdown files
No YAML frontmatter needed
```

### Pattern B: Open Agent System + Skills
```
Use INSTRUCTIONS.md for routing
Add YAML frontmatter to agent files
Agents load progressively on demand
```

### Pattern C: Open Agent System + Skills + Skill Creator
```
Use INSTRUCTIONS.md for routing
Add YAML frontmatter to agent files
Use tooling for complex agents with bundled resources
Package and distribute skills
```

**Most projects use Pattern B** (Open Agent System + Skills)

---

## 📁 File Structure

```
OpenAgentDefinition/
│
├── README.md                     # This file
├── OpenAgentDefinition.md        # Complete specification
├── LICENSE
│
├── scripts/                      # Skill Creator tooling (optional)
│   ├── init_skill.py             # Create skill structure
│   ├── quick_validate.py         # Validate skill (Anthropic spec)
│   └── package_skill.py          # Package skill for distribution
│
└── Templates/                    # Kiro CLI templates
    ├── kiro_steering_agents.md
    ├── kiro_steering_product.md
    ├── kiro_steering_tech.md
    ├── kiro_steering_structure.md
    ├── kiro_agent_driver.json
    ├── example_agent_with_frontmatter.md
    └── skill-creator-agent.md    # Intelligent skill creation agent
```

---

## 🔍 When to Use What

```
Starting a new project with multiple agents?
└─ Use Open Agent System (Pattern B)
   └─ Add Skills for progressive loading
   
Need scripts or bundled resources?
└─ Add Skill Creator tooling (Pattern C)

Just want simple skills without routing?
└─ Use basic YAML frontmatter (Section 4.1)
```

---

## 🎓 Learning Path

1. **Read the specification** → `OpenAgentDefinition.md`
2. **Copy templates** → Use files from `Templates/` in your `.kiro/` folders
3. **Create agents** → Define your specialized agents in `open-agents/agents/`
4. **Add routing** → Create `INSTRUCTIONS.md` with routing logic
5. **Enhance with skills** → Add YAML frontmatter for progressive loading
6. **Use tooling** → Run `init_skill.py` for complex agents

---

## 🔧 Tool Compatibility

| Tool | Entry Point | Status |
|------|-------------|--------|
| **Kiro CLI** | `.kiro/steering/` + `.kiro/agents/` | ✅ Primary |
| Claude Code | `CLAUDE.md` | ✅ Supported |
| Codex | `AGENTS.md` | ✅ Supported |
| Gemini CLI | `GEMINI.md` | ✅ Supported |

---

## 📖 What's in OpenAgentDefinition.md

- What Is an Open Agent System?
- Core Architecture & Pointer Pattern
- Folder Structure & Agent Anatomy
- INSTRUCTIONS.md Router
- Command System
- Kiro CLI Integration
- Skills & Progressive Loading
- Knowledge Bases
- Complete Examples

---

## 📝 License

This is a derivative work based on the [Open Agent System](https://github.com/bladnman/open-agent-system) specification.
