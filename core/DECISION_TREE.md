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

## 4. 🛡️ Auto-Correction Matrix (The "Immune System" v2.0)
**Instruction**: Match the error pattern to the category. Apply the **Auto-Fix Protocol** silently. If the fix fails, escalate to user.

### 📂 Category A: System & I/O (Windows/Files)
| Error / Symptom | Trigger Pattern | Auto-Fix Protocol |
| :--- | :--- | :--- |
| **Chinese Path** | `FileNotFound` / `cv2.error` on valid path | **Code Fix**: Use `np.fromfile(path, dtype=np.uint8)` + `cv2.imdecode` instead of `imread`. Ensure script uses `sys.argv` encoding fix. |
| **Encoding Crash** | `UnicodeEncodeError: 'gbk' codec...` | **Code Fix**: Add `encoding='utf-8'` to all `open()` calls. If console output fails, set `PYTHONIOENCODING=utf-8`. |
| **File Locked** | `PermissionError: [WinError 32]` | **Action**: Wait 2s, retry. If fail, suggest: "Close file/folder in Explorer". |
| **Max Path** | `File name too long` | **Action**: Move workspace to root (e.g., `C:\G-Rec`). Or use `\\?\` prefix for paths. |

### 🐍 Category B: Python & Logic
| Error / Symptom | Trigger Pattern | Auto-Fix Protocol |
| :--- | :--- | :--- |
| **Missing Lib** | `ModuleNotFoundError: No module named 'X'` | **Action**: `pip install X`. If fails, try `python -m pip install X`. Check `requirements.txt`. |
| **Import Loop** | `ImportError: cannot import name` | **Action**: Check for circular imports. Rename local file if it shadows a library (e.g., `email.py`, `code.py`). |
| **JSON Parse** | `json.decoder.JSONDecodeError` | **Action**: Use a robust parser (Strip comments/markdown ```json tags) before parsing. |
| **Indent Error** | `IndentationError` | **Action**: Re-write the specific code block with strict 4-space indentation. |

### 🎬 Category C: Media & FFmpeg
| Error / Symptom | Trigger Pattern | Auto-Fix Protocol |
| :--- | :--- | :--- |
| **Overwrite** | `File exists` (FFmpeg interactive mode) | **Command Fix**: Always add `-y` flag to FFmpeg commands to force overwrite. |
| **Codec Fail** | `Automatic encoder selection failed` | **Command Fix**: Specify codec explicitly: `-c:v libx264 -c:a aac`. |
| **Size Error** | `height not divisible by 2` | **Command Fix**: Add filter `-vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"`. |
| **Empty Audio** | Output video has no sound | **Command Fix**: Check input streams. Add `-map 0:v -map 1:a` (or similar) to ensure audio stream is mapped. |

### 🌐 Category D: Network & Git
| Error / Symptom | Trigger Pattern | Auto-Fix Protocol |
| :--- | :--- | :--- |
| **Git Lock** | `Another git process seems to be running` | **Action**: Check if `git` is running. If not, delete `.git/index.lock`. |
| **Port In Use** | `EADDRINUSE` / `Address already in use` | **Action**: Find PID `netstat -ano | findstr :[PORT]`. Kill it `taskkill /PID [PID] /F`. |
| **Timeout** | `ReadTimeout` / `ConnectionError` | **Action**: Retry with exponential backoff (wait 2s, 5s, 10s). |

---

## 5. 🏳️ Fallback Protocol (Unknown Errors)
If an error matches **NONE** of the above:
1.  **Isolate**: Create a minimal reproduction script (`repro.py`).
2.  **Log**: Write the full traceback to `errors/latest_crash.log`.
3.  **Search**: Use `google_web_search` with the specific error message (remove local paths).
4.  **Report**: Present findings to user: "Unknown Error X. Online solutions suggest Y."
