#!/usr/bin/env python3
"""Initialize a new skill with proper structure."""

import argparse
from pathlib import Path

SKILL_TEMPLATE = """---
name: {name}
description: TODO - Describe what this skill does and when to use it (be comprehensive - this is the primary trigger mechanism)
---

# {title}

## When to Use This Skill

TODO: List specific scenarios when this skill should be triggered

## Core Workflow

TODO: Step-by-step process the agent should follow

## Output Format

TODO: Expected output structure or file format

## Examples

TODO: Concrete examples of usage
"""

SCRIPT_EXAMPLE = """#!/usr/bin/env python3
# Example script - delete if not needed
# Scripts are for deterministic, repeatedly-written code

def main():
    print("Example script")

if __name__ == "__main__":
    main()
"""

REFERENCE_EXAMPLE = """# Example Reference

Delete this file if not needed.

References are for detailed documentation that should be loaded on demand.
Keep SKILL.md lean and move detailed info here.

## When to Use References

- Database schemas
- API documentation  
- Detailed examples
- Domain knowledge
"""

ASSET_README = """# Assets Directory

Place files here that will be used in output (not loaded to context):
- Templates (HTML, React boilerplate)
- Images (logos, icons)
- Fonts
- Sample documents

These files are copied/modified in the final output.
"""

def init_skill(path: str):
    skill_path = Path(path)
    skill_name = skill_path.name
    skill_title = skill_name.replace("-", " ").replace("_", " ").title()
    
    skill_path.mkdir(parents=True, exist_ok=True)
    
    # Create SKILL.md
    (skill_path / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(name=skill_name, title=skill_title)
    )
    
    # Create directories with examples
    scripts_dir = skill_path / "scripts"
    scripts_dir.mkdir(exist_ok=True)
    (scripts_dir / "example_script.py").write_text(SCRIPT_EXAMPLE)
    
    references_dir = skill_path / "references"
    references_dir.mkdir(exist_ok=True)
    (references_dir / "example_reference.md").write_text(REFERENCE_EXAMPLE)
    
    assets_dir = skill_path / "assets"
    assets_dir.mkdir(exist_ok=True)
    (assets_dir / "README.md").write_text(ASSET_README)
    
    print(f"✅ Skill initialized: {skill_path}")
    print(f"📝 Next steps:")
    print(f"   1. Edit {skill_path}/SKILL.md")
    print(f"   2. Add resources to scripts/, references/, or assets/")
    print(f"   3. Delete example files you don't need")
    print(f"   4. Run: python scripts/package_skill.py {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new skill")
    parser.add_argument("--path", required=True, help="Path for the new skill")
    args = parser.parse_args()
    init_skill(args.path)
