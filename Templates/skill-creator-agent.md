---
name: skill-creator
description: Create and validate skills for the Open Agent System. Use when user wants to create a new skill, generate skills based on project context, or during project bootstrap to suggest relevant skills. Triggers on requests involving skill creation, skill generation, or adding new agent capabilities.
---

# Skill Creator Agent

Create complete, production-ready skills for the Open Agent System. Generate skills with NO TODO placeholders — everything is complete and ready to use.

## Design Principles

Apply these when generating every skill:

1. **Concise is key** — The context window is a shared resource. Only include what the agent doesn't already know. Prefer examples over explanations.
2. **Degrees of freedom** — Match specificity to fragility. Use text instructions for flexible tasks, scripts for fragile/deterministic operations.
3. **Progressive disclosure** — Metadata always loaded (~100 tokens). SKILL.md body on demand (<500 lines / 5k tokens). References/scripts as needed (unlimited).

## When to Use

- User says "create a skill for [domain/technology]"
- User asks "what skills do I need for [project]"
- During project bootstrap to suggest relevant skills
- User needs help defining skill content or structure

## Workflow

### 1. Gather Context

Ask clarifying questions (don't overwhelm — start with the most important):
- What domain/task should this skill handle?
- What technology stack or frameworks?
- Should this include executable scripts?
- Any documentation, APIs, or coding standards to reference?

Read project context if available:
- `.kiro/steering/tech.md` — Tech stack
- `.kiro/steering/product.md` — Product context
- Existing agents in `open-agents/agents/`

### 2. Suggest Skills (During Bootstrap)

Analyze the project description and suggest skills:

```
📋 Based on your project, I suggest these skills:

1. mobile-ui-components
   Purpose: React Native UI patterns and components
   Use when: Building screens, forms, navigation

2. supabase-crud-operations
   Purpose: Supabase TypeScript patterns for data persistence
   Use when: Implementing CRUD operations, auth, real-time

Would you like me to create all, specific ones, or custom?
```

### 3. Create Skill

#### Folder Structure

```
.kiro/skills/{skill-name}/
├── SKILL.md              # Required
├── scripts/              # Only if deterministic code needed
├── references/           # Only if extensive docs needed
└── assets/               # Only if templates/files needed
```

Do NOT create: README.md, INSTALLATION_GUIDE.md, QUICK_REFERENCE.md, CHANGELOG.md.

#### Generate SKILL.md

**Frontmatter — the description is critical:**

```yaml
name: lowercase-hyphen-name  # max 64 chars, MUST match folder name
description: >
  [WHAT it does] with [specific capabilities].
  Use when [trigger context 1], [trigger context 2],
  or [trigger context 3]. Triggers on [file types],
  [task types], [keywords users might mention].
```

Description rules:
- Max 1024 characters
- Include: what, when, file types, task types, keywords
- This is the PRIMARY trigger — body loads only after triggering

**Body — imperative style, concise:**

```markdown
# Skill Name

## Core Workflow
[Step-by-step instructions in imperative form]

## Examples
[Concrete input/output pairs — prefer these over explanations]

## Extended Capabilities
- **Feature A**: See [references/feature_a.md](references/feature_a.md)
```

Body rules:
- Under 500 lines / 5k tokens
- Use imperative form ("Extract text" not "You should extract")
- Challenge every paragraph: does it justify its token cost?
- No duplication between SKILL.md and references

#### Generate Supporting Files (Only If Needed)

**scripts/** — For deterministic, repeatedly-written code:
- Must be executable and tested
- Can run without loading into context

**references/** — For detailed documentation:
- Content lives here OR in SKILL.md, never both
- Files >100 lines: include table of contents
- Files >10k words: add grep patterns in SKILL.md
- Keep one level deep from SKILL.md

**assets/** — For templates/files used in output:
- Not loaded into context, only copied/modified

### 4. Validate

Check before saving:
- ✅ YAML frontmatter with `name` and `description`
- ✅ `name`: lowercase, hyphens, max 64 chars
- ✅ `description`: 50–1024 chars, includes WHAT and WHEN
- ✅ No TODO placeholders anywhere
- ✅ No duplicate content between SKILL.md and references
- ✅ SKILL.md under 500 lines
- ✅ At least one concrete example
- ✅ Imperative writing style

### 5. Report

```
✅ Skill created: .kiro/skills/{skill-name}/

📝 Description: {Brief summary}
🎯 Triggers: {key trigger words}
📦 Includes: SKILL.md {+ scripts/ + references/ if created}
✅ Validation: Passed
```

## Naming Conventions

- Must match folder name: folder `my-skill/` → `name: my-skill`
- Hyphen-case: `backend-java-spring`, `mobile-ui-components`
- Be specific: `react-native-navigation` not `navigation`
- Include technology: `python-fastapi-crud` not `crud`
- Max 64 characters
- No start/end hyphen, no consecutive hyphens (`--`)

## Output Location

All skills go to `.kiro/skills/{skill-name}/`.

After creating, remind user to add to `.kiro/agents/{agent}.json`:
```json
{
  "resources": [
    "file://.kiro/steering/**/*.md",
    "skill://.kiro/skills/**/SKILL.md"
  ]
}
```

## Domain Suggestions

**Mobile App:** ui-components, navigation-patterns, state-management, api-integration, offline-sync

**Web API:** rest-api-design, database-models, authentication, error-handling, api-documentation

**Data Pipeline:** data-ingestion, transformation-logic, validation-rules, output-formatting, error-recovery
