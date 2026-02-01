import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path

try:
    from .config import PROJECT_ROOT, SKILLS_DIR, SKILL_INDEX, force_utf8
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent))
    from config import PROJECT_ROOT, SKILLS_DIR, SKILL_INDEX, force_utf8

# Initialize environment
force_utf8()

def install_local(source_path, skill_name=None):
    """Install skill from local folder (Offline Mode)"""
    src = Path(source_path)
    if not src.exists():
        print(f"❌ Error: Local path not found: {src}")
        return False
        
    if not skill_name:
        skill_name = src.name
        
    target_path = SKILLS_DIR / skill_name
    print(f"📦 Installing local skill: {skill_name}...")
    
    if target_path.exists():
        print(f"⚠️ Skill '{skill_name}' already exists. Skipping copy.")
    else:
        try:
            shutil.copytree(src, target_path)
            print(f"✅ Copied files to {target_path}")
        except Exception as e:
            print(f"❌ Failed to copy: {e}")
            return False

    register_skill(skill_name, f"Local: {source_path}")
    return True

def install_remote(repo_url):
    """Install skill from git (Online Mode) with verbose logging"""
    skill_name = repo_url.split("/")[-1].replace(".git", "")
    target_path = SKILLS_DIR / skill_name
    
    print(f"🚚 Cloning remote skill: {skill_name}...")
    
    if target_path.exists():
        print(f"⚠️ Skill '{skill_name}' already exists.")
        return False

    try:
        # Capture output for debugging
        result = subprocess.run(
            ["git", "clone", repo_url, str(target_path)], 
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        register_skill(skill_name, repo_url)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clone: {e}")
        print(f"📄 Git Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def register_skill(name, source):
    """Smart registration with YAML template and safe index insertion"""
    target_path = SKILLS_DIR / name
    
    # 1. Validate Protocol (Create standardized SKILL.md if missing)
    skill_md_path = target_path / "SKILL.md"
    if not skill_md_path.exists():
        print(f"⚠️ Warning: {name} is missing SKILL.md. Creating standardized template...")
        template = f"""---
name: {name}
description: Auto-generated description for {name}.
---

# Skill: {name}

## Description
Description of {name}.

## Usage
```bash
python tool.py --help
```
"""
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(template)

    # 2. Smart Append to Index (Insert before Footer)
    try:
        if SKILL_INDEX.exists():
            with open(SKILL_INDEX, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            new_lines = []
            inserted = False
            new_entry = f"- **{name}**: {source}\n"
            
            # Find the footer separator ("---") to insert before it
            for line in lines:
                if line.strip() == "---" and not inserted:
                    # Check if previous line is empty, if not add one
                    if new_lines and new_lines[-1].strip() != "":
                        new_lines.append("\n")
                    new_lines.append(new_entry)
                    new_lines.append("\n") # Add spacing before footer
                    new_lines.append(line)
                    inserted = True
                else:
                    new_lines.append(line)
            
            # If no footer found, just append
            if not inserted:
                if lines and lines[-1].strip() != "":
                    new_lines.append("\n")
                new_lines.append(new_entry)
            
            with open(SKILL_INDEX, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
        else:
            # Create new if doesn't exist
            with open(SKILL_INDEX, "w", encoding="utf-8") as f:
                f.write(f"# G-Rec Skill Index\n\n- **{name}**: {source}\n")
                
        print(f"✅ Skill '{name}' successfully registered in SKILL_INDEX.md.")
        
    except Exception as e:
        print(f"❌ Failed to update index: {e}")

def list_skills():
    print("\n📦 Installed G-Rec Skills:")
    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith("_") and not item.name.startswith("."):
            skill_path = item / "SKILL.md"
            status = "✅ Protocol OK" if skill_path.exists() else "⚠️ Missing SKILL.md"
            print(f"- {item.name:<30} [{status}]")

def main():
    parser = argparse.ArgumentParser(description="G-Rec Skill Manager v2.0")
    subparsers = parser.add_subparsers(dest="command")
    
    # Add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("source", help="GitHub URL OR Local Path")
    add_parser.add_argument("--local", action="store_true", help="Treat source as local path")
    
    # List command
    subparsers.add_parser("list")
    
    args = parser.parse_args()
    
    if args.command == "add":
        if args.local:
            install_local(args.source)
        else:
            if os.path.exists(args.source) or "\\" in args.source:
                # User likely forgot --local but passed a path
                print("💡 Detected local path. Switching to Local Install mode...")
                install_local(args.source)
            else:
                install_remote(args.source)
    elif args.command == "list":
        list_skills()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()