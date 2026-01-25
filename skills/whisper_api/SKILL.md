# Skill: Whisper ASR (Lightweight)

## Description
A lightweight subtitle extractor using OpenAI's Whisper model.
It auto-downloads the necessary model (small/medium) and runs locally.

## Usage
```bash
python skills/whisper_api/tool.py --video "path/to/video.mp4" --model small
```

## Arguments
- `--video`: Path to input file.
- `--model`: `tiny`, `base`, `small` (Recommended), `medium`, `large`.
- `--device`: `cuda` (GPU) or `cpu`.

## Dependencies
- `pip install openai-whisper`
- `ffmpeg` (System PATH)
