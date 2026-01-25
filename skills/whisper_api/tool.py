import argparse
import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load env variables
load_dotenv()

def run_custom_asr(audio_path, api_key, base_url, model):
    print(f"🎬 [Custom API] Transcribing {Path(audio_path).name} using {model}...")
    
    try:
        from openai import OpenAI
    except ImportError:
        return {"status": "error", "message": "Missing dependency: pip install openai"}

    # Initialize client with custom base_url
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    audio_file = Path(audio_path)
    
    try:
        with open(audio_file, "rb") as f:
            # Note: Many custom servers still use "whisper-1" as the endpoint name 
            # even if the underlying model is different. 
            # But we will try the model name provided by user.
            transcript = client.audio.transcriptions.create(
                model=model, 
                file=f,
                response_format="srt"
            )
        
        # Save SRT
        srt_path = audio_file.with_suffix(".srt")
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(transcript)
            
        print(f"✅ Transcription complete!")
        return {"status": "success", "subtitle_path": str(srt_path), "content_preview": transcript[:100] + "..."}

    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--api_key", required=True)
    parser.add_argument("--base_url", required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    
    res = run_custom_asr(args.audio, args.api_key, args.base_url, args.model)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()