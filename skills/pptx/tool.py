import argparse
import sys
import subprocess
import os
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.absolute()
SCRIPTS = SKILL_ROOT / "scripts"

def run_py(script, args):
    cmd = [sys.executable, str(SCRIPTS / script)] + args
    subprocess.run(cmd)

def run_js(script, args):
    # Node.js required
    cmd = ["node", str(SCRIPTS / script)] + args
    try:
        subprocess.run(cmd, shell=True) # shell=True for node path resolution on Windows sometimes
    except FileNotFoundError:
        print("❌ Node.js not found. Please install Node.")

def main():
    parser = argparse.ArgumentParser(description="G-Rec PPTX Automation")
    parser.add_argument("--action", choices=["inspect", "convert"], default="inspect")
    parser.add_argument("--file", required=True, help="Input file (pptx or html)")
    parser.add_argument("--output", help="Output file (for convert)")
    
    args = parser.parse_args()

    if args.action == "inspect":
        run_py("inventory.py", [args.file])
    elif args.action == "convert":
        if not args.output:
            print("❌ --output required for convert")
            return
        run_js("html2pptx.js", [args.file, args.output])

if __name__ == "__main__":
    main()