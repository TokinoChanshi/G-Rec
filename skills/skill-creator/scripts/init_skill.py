#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [Short 1-line description of the skill]
---

# Skill: {skill_title}

## Description
[Detailed description of what this skill does, its inputs, and its outputs.]

## Usage
This skill follows the **G-S Protocol** and is executable via `tool.py`.

```bash
# Basic Usage
python tool.py --action run --input "some input"

# Help
python tool.py --help
```

## Protocol Definitions
- **Entry Point**: `tool.py`
- **Config**: `assets/config.json` (Optional)
- **Logs**: `output/` (Optional)
"""

TOOL_PY_TEMPLATE = """import argparse
import sys
import json
import os

# --- G-S Protocol Standard Header ---
# Force UTF-8 Output for Windows Compatibility
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_action(args):
    print(f"🚀 {skill_title} Running...")
    print(f"📝 Input: {{args.input}}")
    
    # TODO: Implement your logic here
    result = {{"status": "success", "data": "Processed: " + str(args.input)}}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

def main():
    parser = argparse.ArgumentParser(description="{skill_title} Tool")
    parser.add_argument("--action", default="run", help="Action to perform")
    parser.add_argument("--input", help="Input data")
    
    args = parser.parse_args()
    
    if args.action == "run":
        run_action(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
"""

def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with template SKILL.md and tool.py.
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    skill_title = title_case_skill_name(skill_name)

    # 1. Create SKILL.md
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )
    try:
        (skill_dir / 'SKILL.md').write_text(skill_content, encoding='utf-8')
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # 2. Create tool.py (Entry Point)
    tool_content = TOOL_PY_TEMPLATE.format(
        skill_title=skill_title
    )
    try:
        (skill_dir / 'tool.py').write_text(tool_content, encoding='utf-8')
        print("✅ Created tool.py (G-S Protocol Entry Point)")
    except Exception as e:
        print(f"❌ Error creating tool.py: {e}")
        return None

    # 3. Create standard subdirectories
    for subdir in ['scripts', 'assets', 'output']:
        (skill_dir / subdir).mkdir(exist_ok=True)
        
    # Create empty .gitignore
    (skill_dir / '.gitignore').write_text("output/*\n__pycache__/\n*.pyc", encoding='utf-8')

    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print()

    result = init_skill(skill_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
