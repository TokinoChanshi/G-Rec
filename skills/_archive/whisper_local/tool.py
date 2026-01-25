import argparse
import sys
import os
import json
from pathlib import Path

def format_timestamp(seconds: float):
    x = seconds
    hours = int(x // 3600)
    x %= 3600
    minutes = int(x // 60)
    x %= 60
    seconds = int(x)
    milliseconds = int((x - seconds) * 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def run_faster_whisper(audio_path, model_size="small", device="cpu"):
    print(f"🎬 [G-Rec] Initializing model '{model_size}' via ModelScope...")
    
    try:
        from faster_whisper import WhisperModel
        from modelscope import snapshot_download
    except ImportError:
        return {"status": "error", "message": "Missing dependency: pip install faster-whisper modelscope"}

    try:
        # Step 1: Download from ModelScope (Faster in China)
        # small: https://modelscope.cn/models/Yueyang/faster-whisper-small
        model_id = f"Yueyang/faster-whisper-{model_size}"
        print(f"📦 Downloading {model_id} from ModelScope...")
        model_dir = snapshot_download(model_id)
        
        # Step 2: Load Model
        print(f"🚀 Loading model from {model_dir}...")
        model = WhisperModel(model_dir, device=device, compute_type="int8")
        
        print(f"🎤 [Whisper] Transcribing: {audio_path}...")
        segments, info = model.transcribe(audio_path, beam_size=5)
        
        output_file = Path(audio_path).with_suffix(".srt")
        with open(output_file, "w", encoding="utf-8") as f:
            for i, segment in enumerate(segments):
                start = format_timestamp(segment.start)
                end = format_timestamp(segment.end)
                text = segment.text.strip()
                f.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

        return {
            "status": "success", 
            "subtitle_path": str(output_file),
            "language": info.language
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--model", default="small") # Small is accurate enough
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()
    
    res = run_faster_whisper(args.audio, args.model, args.device)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()