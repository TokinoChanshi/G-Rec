# Skill: Gemini ASR (Native)

## Description
Uses Gemini's native multimodal capabilities to transcribe audio.
This tool extracts audio from video files, preparing them for manual upload to the Gemini chat interface.

## Usage
```bash
python skills/gemini_asr/tool.py --video "path/to/video.mp4"
```

## Workflow
1. Tool extracts audio (`.mp3`).
2. User uploads mp3 to chat.
3. User asks Gemini to transcribe.
