# Decision Index (Lazy Loading Protocol)

⚠️ **CRITICAL**: Do NOT hypothesize solutions. **Read the Reference Manuals** first.

## 1. Skill Lookup (Feature Requests)
**ACTION**: First, read `G-Rec/core/SKILL_INDEX.md` to see available tools.
- If a matching skill is found -> **STOP & ASK**: "Found skill [Name]. Execute [Entry Point]?"
- If NO matching skill is found -> Check `G-Rec/workflows/` for manual SOPs.

## 2. Auto-Discovery (System Maintenance)
If the user says "Scan skills", "Update tools", or "I added a plugin":
- **ACTION**: Execute the **Auto-Learning Protocol** defined in `SYSTEM_PROMPT.md`.

## 3. Error Troubleshooting (Bug Fixes)
If the user encounters an error, **EXECUTE** `/read_file` on the matching error log:
- **Python / Pip**: `G-Rec/errors/python_env.md`
- **FFmpeg**: `G-Rec/errors/ffmpeg_issues.md`
- **Path/Encoding**: `G-Rec/errors/encoding_paths.md`
