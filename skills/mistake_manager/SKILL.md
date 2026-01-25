# Skill: Mistake Manager (Anti-Fragile)

## Description
A system to record, search, and learn from past errors.
Use this skill when:
1. An error occurs -> Add it to the book.
2. Starting a risky task -> Search the book for pitfalls.

## Usage
```bash
# Search for past errors
python skills/mistake_manager/tool.py --action search --keyword "ffmpeg"

# Record a new error
python skills/mistake_manager/tool.py --action add \
  --category "Network" \
  --issue "Pip install timeout" \
  --cause "SSL blocking" \
  --solution "Use offline install"
```

