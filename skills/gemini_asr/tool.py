import argparse
import sys
import subprocess
import os
from pathlib import Path

def extract_audio(video_path):
    video_file = Path(video_path)
    # Output smaller mp3 for LLM
    audio_file = video_file.with_suffix(".mp3")
    
    # Check if exists
    if audio_file.exists():
        print(f"✅ Audio already exists: {audio_file}")
        return audio_file

    print(f"🎬 Extracting audio from {video_file.name}...")
    
    # Low bitrate to save tokens/bandwidth
    cmd = [
        "ffmpeg", "-v", "error", "-y",
        "-i", str(video_file),
        "-vn", "-ac", "1", "-b:a", "64k",
        str(audio_file)
    ]
    
    try:
        subprocess.run(cmd, check=True)
        return audio_file
    except subprocess.CalledProcessError:
        print("❌ FFmpeg failed.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Prepare video for Gemini ASR")
    parser.add_argument("--video", required=True, help="Input video path")
    args = parser.parse_args()
    
    audio_path = extract_audio(args.video)
    
    if audio_path:
        print("\n" + "="*50)
        print("🤖 **READY FOR GEMINI**")
        print("Please upload this file to the chat:")
        print(f"👉 {audio_path}")
        print("\nAnd use this Prompt:")
        print('"""')
        print("Please transcribe this audio file into SRT format. Ensure accurate timestamps.")
        print('"""')
        print("="*50)

if __name__ == "__main__":
    main()
