# 📕 G-Rec Mistake Book (Anti-Fragile Knowledge Base)

> **SYSTEM MAINTENANCE INSTRUCTION**: 
> 1. **Keep it Lean**: This file is for *Patterns*, not *Logs*. Do NOT paste full stack traces here.
> 2. **Format**: Use `Issue -> Root Cause -> Solution`. Max 5 lines per entry.
> 3. **Search First**: Before adding, check if a similar pattern exists. Merge if possible.
> 4. **Pruning**: If this file exceeds 500 lines, the [Librarian] role must condense it.

## 🐍 Python & Environment
- **Issue**: `pip install` fails with SSL/TLS errors.
  - **Root Cause**: Network restriction/firewall blocking HuggingFace/PyPI.
  - **Solution**: Use mirrors (aliyun) or pre-downloaded wheels.
  - **Prevention**: Always check `G-Rec/errors/python_env.md` first.

## 🎬 FFmpeg & Media
- **Issue**: `ffmpeg` command not found.
  - **Root Cause**: Not in system PATH.
  - **Solution**: Use absolute path defined in `tool.py` config.

## 🧠 Logic & Context
- **Issue**: "I am in Desktop/astrofox and cannot read G-Rec files."
  - **Root Cause**: Sandbox restriction on cross-directory reads.
  - **Solution**: Use **Boomerang Protocol** (Jump -> Load -> Return).

---
*Append new mistakes below using `skills/mistake_manager/tool.py`*
