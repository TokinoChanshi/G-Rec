import argparse
import sys
import os
import json
import torch
import whisper
from pathlib import Path
from datetime import timedelta

def format_timestamp(seconds: float):
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    millis = int(td.microseconds / 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, start=1):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")

def run_local_whisper(video_path, model_name, device):
    print(f"🎬 [Local Whisper] Loading model '{model_name}' on {device}...")
    
    try:
        # Load Model
        model = whisper.load_model(model_name, device=device)
        
        # Transcribe
        print(f"🎙️ Transcribing {Path(video_path).name}...")
        result = model.transcribe(video_path)
        
        # Save SRT
        output_path = Path(video_path).with_suffix(".srt")
        write_srt(result["segments"], output_path)
        
        print(f"✅ Subtitles saved to: {output_path}")
        return {
            "status": "success", 
            "subtitle_path": str(output_path),
            "text_preview": result["text"][:100] + "..."
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description="G-Rec Local Whisper Tool")
    parser.add_argument("--video", required=True, help="Path to input video/audio file")
    parser.add_argument("--model", default="medium", help="Model size: tiny, base, small, medium, large")
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu", help="Device: cuda or cpu")
    
    args = parser.parse_args()
    
    # Run
    res = run_local_whisper(args.video, args.model, args.device)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
