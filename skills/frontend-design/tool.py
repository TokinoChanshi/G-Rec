import argparse
import sys
import os
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="G-Rec Frontend Design Rule Enforcer")
    parser.add_argument("--apply", help="Apply design rules to this file (logic handled by LLM)")
    args = parser.parse_args()

    if args.apply:
        print(f"🎨 [Design] Rules from SKILL.md are now active for: {args.apply}")
        print("💡 TIP: Just ask G-Rec to 'Refactor this file using frontend-design rules'.")
    else:
        print("🎨 Frontend Design rules are loaded in G-Rec context.")

if __name__ == "__main__":
    main()