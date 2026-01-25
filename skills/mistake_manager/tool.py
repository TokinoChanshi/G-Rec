import argparse
import sys
import os
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
MISTAKE_BOOK = PROJECT_ROOT / "core" / "MISTAKE_BOOK.md"

def search_mistake(keyword):
    if not MISTAKE_BOOK.exists():
        return "📕 Mistake Book is empty."
    
    found = []
    with open(MISTAKE_BOOK, "r", encoding="utf-8") as f:
        content = f.read()
        sections = content.split("## ")
        for sec in sections:
            if keyword.lower() in sec.lower():
                found.append("## " + sec.strip())
    
    if found:
        return "\n\n".join(found)
    else:
        return f"✅ No known mistakes found regarding '{keyword}'."

def add_mistake(category, issue, cause, solution):
    entry = f"""
## {category} (New)
- **Issue**: {issue}
  - **Root Cause**: {cause}
  - **Solution**: {solution}
  - **Prevention**: Added to Mistake Book.
"""
    with open(MISTAKE_BOOK, "a", encoding="utf-8") as f:
        f.write(entry)
    return "📝 Mistake recorded."

def main():
    parser = argparse.ArgumentParser(description="G-Rec Mistake Manager")
    parser.add_argument("--action", choices=["search", "add"], required=True)
    parser.add_argument("--keyword", help="Search keyword")
    
    # Add args
    parser.add_argument("--category", help="Error category (e.g., Python)")
    parser.add_argument("--issue", help="What went wrong")
    parser.add_argument("--cause", help="Why it happened")
    parser.add_argument("--solution", help="How to fix it")

    args = parser.parse_args()

    if args.action == "search":
        print(search_mistake(args.keyword))
    elif args.action == "add":
        if not (args.issue and args.cause and args.solution):
            print("❌ Error: --issue, --cause, and --solution are required for adding.")
        else:
            print(add_mistake(args.category, args.issue, args.cause, args.solution))

if __name__ == "__main__":
    main()
