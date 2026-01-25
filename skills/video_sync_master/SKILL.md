# Skill: Video Sync Master (VSM)

## Description
A powerful tool for **Lip-Syncing**, **Translation**, and **Dubbing**.
It integrates WhisperX (ASR), Qwen (Translation), and MaskGCT (TTS) into a single pipeline.

## Usage (Subcommands)

### 1. Extract Subtitles (ASR)
```bash
python skills/video_sync_master/tool.py asr --video "input.mp4" --service jianying
```

### 2. Translate Text
```bash
python skills/video_sync_master/tool.py translate --text "Hello" --lang "Chinese"
```

### 3. Full Dubbing (Translate + TTS + LipSync)
```bash
python skills/video_sync_master/tool.py dub --video "input.mp4" --lang "Japanese" --tts indextts
```

### 4. Lip Sync Only
```bash
python skills/video_sync_master/tool.py sync --video "face.mp4" --audio "voice.wav"
```

## Arguments
- `asr`: Extract text. Supports `whisperx` (local) or `jianying` (cloud).
- `dub`: Full flow. Requires local models in `models/`.
- `sync`: Wav2Lip logic only.

## Dependency Note
Requires `requirements.txt` and `models/` folder for offline features.