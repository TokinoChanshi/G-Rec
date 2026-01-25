import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
SKILLS_DIR = PROJECT_ROOT / "skills"
SKILL_INDEX = PROJECT_ROOT / "core" / "SKILL_INDEX.md"

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
    """Install skill from git (Online Mode)"""
    skill_name = repo_url.split("/")[-1].replace(".git", "")
    target_path = SKILLS_DIR / skill_name
    
    print(f"🚚 Cloning remote skill: {skill_name}...")
    
    if target_path.exists():
        print(f"⚠️ Skill '{skill_name}' already exists.")
        return False

    try:
        subprocess.run(["git", "clone", repo_url, str(target_path)], check=True)
        register_skill(skill_name, repo_url)
        return True
    except Exception as e:
        print(f"❌ Failed to clone: {e}")
        return False

def register_skill(name, source):
    """Common registration logic"""
    target_path = SKILLS_DIR / name
    
    # Validate Protocol
    if not (target_path / "SKILL.md").exists():
        print(f"⚠️ Warning: {name} is missing SKILL.md. Creating template...")
        with open(target_path / "SKILL.md", "w", encoding="utf-8") as f:
            f.write(f"# Skill: {name}\n\nDescription of {name}.")

    # Append to Index
    with open(SKILL_INDEX, "a", encoding="utf-8") as f:
        f.write(f"\n- **{name}**: {source}")
        
    print(f"✅ Skill '{name}' successfully registered in SKILL_INDEX.md.")

def list_skills():
    print("\n📦 Installed G-Rec Skills:")
    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith("_") and not item.name.startswith("."):
            status = "✅ Protocol OK" if (item / "SKILL.md").exists() else "⚠️ Missing SKILL.md"
            print(f"- {item.name:<20} [{status}]")

def main():
    parser = argparse.ArgumentParser(description="G-Rec Skill Manager")
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