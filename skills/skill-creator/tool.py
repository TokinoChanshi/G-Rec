import argparse
import sys
import subprocess
import os
from pathlib import Path

# --- Configuration ---
SKILL_ROOT = Path(__file__).parent.absolute()
SCRIPTS_DIR = SKILL_ROOT / "scripts"

def run_script(script_name, args_list):
    """Run an internal Skill Creator script"""
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        return {"status": "error", "message": f"Script not found: {script_name}"}

    # Force UTF-8 only for I/O (prevents crash on Emojis, safe for Paths)
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    cmd = [sys.executable, str(script_path)] + args_list
    print(f"🛠️ [Skill-Creator] Running {script_name}...")
    
    try:
        # These scripts usually take interactive input or produce files
        # Using errors='replace' to prevent crash on non-utf8 windows output
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
        if result.returncode == 0:
            print(result.stdout)
            return {"status": "success", "output": result.stdout}
        else:
            print(f"❌ Error: {result.stderr}")
            return {"status": "error", "message": result.stderr}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description="G-Rec Skill Creator - Make your own skills!")
    parser.add_argument("--action", choices=["init", "validate", "package"], default="init")
    parser.add_argument("--name", help="Name of the new skill")
    parser.add_argument("--path", help="Output path for the new skill (default: skills/)")
    
    args = parser.parse_args()

    # Default path to G-Rec skills folder if not provided
    base_skills_dir = SKILL_ROOT.parent
    output_path = args.path if args.path else str(base_skills_dir)

    if args.action == "init":
        if not args.name:
            print("❌ Error: Please provide --name for the new skill.")
            return
        run_script("init_skill.py", [args.name, "--path", output_path])
    elif args.action == "validate":
        target = args.path if args.path else str(SKILL_ROOT) # Validate self by default or specific path
        run_script("quick_validate.py", [target])
    elif args.action == "package":
        if not args.name:
            print("❌ Error: Please provide --name (path to skill folder) to package.")
            return
        run_script("package_skill.py", [args.name])

if __name__ == "__main__":
    main()