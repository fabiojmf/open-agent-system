#!/usr/bin/env python3
"""Validate and package a skill into a distributable .skill file."""

import argparse
import zipfile
import re
import yaml
from pathlib import Path

def validate_skill(skill_path: Path) -> list[str]:
    """Validate skill following Anthropic's specifications"""
    errors = []
    
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing SKILL.md file")
        return errors
    
    content = skill_md.read_text()
    
    # Check frontmatter
    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter (must start with ---)")
        return errors
    
    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        errors.append("Invalid frontmatter format")
        return errors
    
    frontmatter_text = match.group(1)
    
    # Parse YAML
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            errors.append("Frontmatter must be a YAML dictionary")
            return errors
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML in frontmatter: {e}")
        return errors
    
    # Check allowed properties
    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'compatibility', 'allowed-tools', 'metadata'}
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        errors.append(
            f"Unexpected key(s): {', '.join(sorted(unexpected_keys))}. "
            f"Allowed: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )
    
    # Check required fields
    if 'name' not in frontmatter:
        errors.append("Missing 'name' in frontmatter")
    if 'description' not in frontmatter:
        errors.append("Missing 'description' in frontmatter")
    
    # Validate name
    if 'name' in frontmatter:
        name = frontmatter['name']
        if not isinstance(name, str):
            errors.append(f"Name must be a string, got {type(name).__name__}")
        else:
            name = name.strip()
            if name:
                # Check naming convention
                if not re.match(r'^[a-z0-9-]+$', name):
                    errors.append(f"Name '{name}' should be hyphen-case (lowercase, digits, hyphens only)")
                if name.startswith('-') or name.endswith('-') or '--' in name:
                    errors.append(f"Name '{name}' cannot start/end with hyphen or have consecutive hyphens")
                if len(name) > 64:
                    errors.append(f"Name too long ({len(name)} chars). Maximum: 64")
                # Check name matches folder
                if name != skill_path.name:
                    errors.append(f"Name '{name}' must match folder name '{skill_path.name}'")
    
    # Validate description
    if 'description' in frontmatter:
        description = frontmatter['description']
        if not isinstance(description, str):
            errors.append(f"Description must be a string, got {type(description).__name__}")
        else:
            description = description.strip()
            if description:
                if '<' in description or '>' in description:
                    errors.append("Description cannot contain angle brackets (< or >)")
                if len(description) > 1024:
                    errors.append(f"Description too long ({len(description)} chars). Maximum: 1024")
                if len(description) < 50:
                    errors.append(f"Description too short ({len(description)} chars). Minimum: 50")
    
    # Check for TODO placeholders
    body = content[match.end():]
    if re.search(r'\bTODO\b', body, re.IGNORECASE):
        errors.append("SKILL.md body contains TODO placeholders — all content must be complete")
    
    return errors

def package_skill(skill_path: Path, output_dir: Path = None):
    skill_path = Path(skill_path).resolve()
    
    if not skill_path.exists():
        print(f"❌ Skill path does not exist: {skill_path}")
        return
    
    # Validate
    errors = validate_skill(skill_path)
    if errors:
        print("❌ Validation failed:")
        for error in errors:
            print(f"   • {error}")
        print("\n💡 Fix these issues and try again")
        return
    
    # Package
    output_dir = Path(output_dir) if output_dir else skill_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{skill_path.name}.skill"
    
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in skill_path.rglob("*"):
            if file.is_file() and not file.name.endswith('.skill'):
                arcname = file.relative_to(skill_path.parent)
                zf.write(file, arcname)
    
    print(f"✅ Skill validated and packaged")
    print(f"📦 Output: {output_file}")
    print(f"📊 Size: {output_file.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate and package a skill")
    parser.add_argument("skill_path", help="Path to the skill directory")
    parser.add_argument("--output", help="Output directory (default: skill parent dir)")
    args = parser.parse_args()
    package_skill(Path(args.skill_path), Path(args.output) if args.output else None)
