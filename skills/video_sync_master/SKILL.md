# Skill: Video Sync Master (VSM)

## Description
A powerful tool for **Lip-Syncing** and **Video Translation**.
It uses Wav2Lip technology to synchronize a video's lip movements to match a new audio track (dubbing).

## Usage Cases
1.  **Dubbing**: Replace the original voice with a translated TTS voice and fix the lips.
2.  **Repair**: Fix bad lip-sync in existing footage.

## How to Run (G-S Protocol)
Use the `tool.py` wrapper to interact with the underlying `inference.py`.

```bash
python skills/video_sync_master/tool.py --video "path/to/video.mp4" --audio "path/to/new_audio.wav"
```

## Arguments
- `--video`: (Required) Path to the source video (face).
- `--audio`: (Required) Path to the target audio (voice).
- `--quality`: (Optional) "Fast", "High", "Enhanced". Default: "Enhanced".
- `--output`: (Optional) Path to save result.

## Dependency Note
This tool requires **PyTorch** and **FFmpeg**. 
Ensure `requirements.txt` is installed.
