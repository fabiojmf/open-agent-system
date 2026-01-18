# Open Agent System (Kiro CLI Compatible)

> A Kiro CLI compatible version of the [Open Agent System](https://github.com/bladnman/open-agent-system) specification.

## 🙏 Credits

This project is a derivative work based on the original **Open Agent System** by [@bladnman](https://github.com/bladnman):
- **Original Repository**: https://github.com/bladnman/open-agent-system
- **Original Definition**: [OpenAgentDefinition.md](https://github.com/bladnman/open-agent-system/blob/main/OpenAgentDefinition.md)

### What's Different?

This version adds **Kiro CLI** compatibility through the steering folder system, while maintaining full compatibility with Claude Code, Gemini CLI, and Codex.

## 📁 File Structure

```
OpenAgentDefinition/
│
├── README.md                                 # This file
├── OpenAgentDefinition.md                    # 📄 Complete specification (copy this!)
│
└── Templates/                                # Ready-to-use templates
    ├── kiro_steering_agents.md               # .kiro/steering/agents.md
    ├── kiro_steering_product.md              # .kiro/steering/product.md
    ├── kiro_steering_tech.md                 # .kiro/steering/tech.md
    ├── kiro_steering_structure.md            # .kiro/steering/structure.md
    └── kiro_agent_driver.json                # .kiro/agents/{agent}.json template
```

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

1. **Copy the main specification** → `OpenAgentDefinition.md`
2. **Copy the templates** → Use files from `Templates/` in your `.kiro/steering/` and `.kiro/agents/` folders
3. **Customize for your domain** → Update agent definitions, product context, tech stack

## 🔧 Tool Compatibility

| Tool | Entry Point | Status |
|------|-------------|--------|
| Claude Code | `CLAUDE.md` | ✅ Supported |
| Codex | `AGENTS.md` | ✅ Supported |
| Gemini CLI | `GEMINI.md` | ✅ Supported |
| **Kiro CLI** | `.kiro/steering/` + `.kiro/agents/` | ✅ **Now Supported** |

## 📖 What's Included

### Main Specification
The `OpenAgentDefinition.md` file contains:
- What Is an Open Agent System?
- Core Architecture & Pointer Pattern
- Folder Structure
- Agent File Anatomy
- Command System
- INSTRUCTIONS.md File
- Operations Guide
- Adding to Existing Projects
- **Kiro CLI Integration Guide**
- Complete Example

### Templates
Copy these directly to your `.kiro/` folder:

**Steering files** (`.kiro/steering/`):
- **agents.md** - Entry point for Open Agent System
- **product.md** - Product context template
- **tech.md** - Technology stack template
- **structure.md** - Project structure template

**Agent drivers** (`.kiro/agents/`):
- **kiro_agent_driver.json** - Template for agent JSON drivers (points to your MD files)

## 📝 License

This is a derivative work based on the [Open Agent System](https://github.com/bladnman/open-agent-system) specification.

