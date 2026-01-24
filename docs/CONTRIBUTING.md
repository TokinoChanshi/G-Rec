# 🤝 Contributing to G-Rec

We welcome contributions! G-Rec is designed to be evolved by its users.
The best way to contribute is by adding new **Skills**.

## 🚀 How to Create a New Skill

### Step 1: Create the Directory
Create a folder in `skills/` with a descriptive name (snake_case).
```bash
mkdir skills/video_downloader
```

### Step 2: Implement the Tool (`tool.py`)
Write a standalone Python script that performs the action.
- Must use `argparse` for inputs.
- Must output JSON to stdout (optional but recommended) or clear text.
- **Rule**: Do not rely on G-Rec internals. The tool should be runnable manually by a human.

### Step 3: Document the Skill (`SKILL.md`)
Create a markdown file describing *how* and *when* to use the tool.

**Template:**
```markdown
# Skill: Video Downloader

## Description
Downloads videos from YouTube/Bilibili using yt-dlp.

## Usage
- Trigger: "Download video from [url]"
- Command: python skills/video_downloader/tool.py --url "[url]"

## Arguments
- `--url`: The target video link.
- `--format`: (Optional) "mp4" or "mp3".
```

### Step 4: Register (Auto-Discovery)
Just tell G-Rec: **"Scan for new skills."**
The system will automatically find your folder and update `core/SKILL_INDEX.md`.

## 🧪 Testing
Before submitting a PR:
1. Run your `tool.py` manually to ensure it works.
2. Ask G-Rec to use it in a conversation.
