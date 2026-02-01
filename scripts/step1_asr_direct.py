import sys
import os
import json

# Add backend to path
sys.path.append(r"skills/video_sync_master/backend")
from asr import run_asr

video_path = r"..\转录其他语言\recording-1769339953970_cleaned.mp4"
# Ensure we pass the absolute path or correct relative path
video_path = os.path.abspath(video_path)

print(f"Running ASR on: {video_path}")
segments = run_asr(video_path, service="openai_whisper")

if segments:
    with open("segments.json", "w", encoding="utf-8") as f:
        json.dump(segments, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(segments)} segments to segments.json")
else:
    print("ASR returned empty segments.")

