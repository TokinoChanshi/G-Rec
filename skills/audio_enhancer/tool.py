import argparse
import sys
import subprocess
import shutil
import json
import uuid
import os
from pathlib import Path

# --- Force CPU Mode for absolute stability ---
os.environ["CUDA_VISIBLE_DEVICES"] = "-1" 

from dotenv import load_dotenv

# --- Configuration ---
load_dotenv() # Load environment variables from .env
SKILL_ROOT = Path(__file__).parent.absolute()

# DSP Chain Parameters (The "Secret Sauce")
EQ_OPTS = "highpass=f=90,equalizer=f=250:t=q:w=1.0:g=-3,equalizer=f=500:t=q:w=1.2:g=-1.5,equalizer=f=3000:t=q:w=1.0:g=2,equalizer=f=10000:t=q:w=1.0:g=1.5"
COMP_OPTS = "acompressor=threshold=-18dB:ratio=2.5:attack=15:release=120"
LOUD_OPTS = "loudnorm=I=-16:TP=-1:LRA=11"


# aggressive: DeepFilter -> Gate -> Highpass/Lowpass -> Gentle EQ -> Comp -> Loudnorm
AGGRESSIVE_OPTS = "highpass=f=100,agate=range=0.15:threshold=-50dB,lowpass=f=10000,equalizer=f=250:t=q:w=1.0:g=-3,equalizer=f=3000:t=q:w=1.0:g=1"
AGGRESSIVE_COMP = "acompressor=threshold=-20dB:ratio=2:attack=10:release=100"

def get_cmd(name, env_var):
    """Helper to find command from Env or System PATH"""
    path = os.environ.get(env_var)
    if path and os.path.exists(path):
        return path
    return name

def run_processing(input_path: str, preset: str):
    """
    Runs the audio enhancement pipeline with the selected preset.
    """
    input_file = Path(input_path)
    if not input_file.exists():
        return {"status": "error", "message": f"Input file not found: {input_path}"}

    # Resolve binaries
    FFMPEG_BIN = get_cmd("ffmpeg", "FFMPEG_PATH")
    DEEPFILTER_BIN = get_cmd("deepFilter", "DEEPFILTER_PATH")

    # Setup temporary workspace
    session_id = str(uuid.uuid4())[:8]
    work_dir = SKILL_ROOT / f"tmp_{session_id}"
    work_dir.mkdir(exist_ok=True)
    
    # Force MP4 output to avoid WebM/H.264/AAC incompatibility
    output_file = input_file.with_name(f"{input_file.stem}_cleaned.mp4")

    try:
        # Step 1: Extract Audio (to 48k wav)
        raw_wav = work_dir / "voice_raw.wav"
        subprocess.run([
            FFMPEG_BIN, "-v", "error", "-y",
            "-i", str(input_file),
            "-vn", "-ac", "1", "-ar", "48000",
            "-c:a", "pcm_s16le",
            str(raw_wav)
        ], check=True)

        # Step 2: DeepFilterNet (AI Denoise)
        # DeepFilterNet creates a file with a specific suffix
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = "" # Force CPU to avoid CUDA/cuDNN errors
        subprocess.run([DEEPFILTER_BIN, str(raw_wav), "-o", str(work_dir)], env=env, check=True)
        
        # Determine the name of the file DeepFilter just created
        # Usually it appends _DeepFilterNet3.wav
        denoised_wav = next(work_dir.glob("*_DeepFilterNet*.wav"), None)
        if not denoised_wav:
             return {"status": "error", "message": "DeepFilterNet failed to produce an output file."}

        # Step 3: Apply DSP Chain based on Preset
        final_wav = work_dir / "voice_final.wav"
        
        if preset == "aggressive":
            filter_chain = f"{AGGRESSIVE_OPTS},{AGGRESSIVE_COMP},{LOUD_OPTS}"
        else:
            filter_chain = f"{EQ_OPTS},{COMP_OPTS},{LOUD_OPTS}"
        
        subprocess.run([
            FFMPEG_BIN, "-v", "error", "-y",
            "-i", str(denoised_wav),
            "-af", filter_chain,
            str(final_wav)
        ], check=True)

        # Step 4: Remux (Combine original video + new audio)
        # We use -map 0:v? to handle audio-only sources gracefully
        subprocess.run([
            FFMPEG_BIN, "-v", "error", "-y",
            "-i", str(input_file),
            "-i", str(final_wav),
            "-map", "0:v?", # Map original video if exists
            "-map", "1:a:0", # Map processed audio
            "-map_metadata", "0", # Copy global metadata
            "-c:v", "copy",  # Fast copy video stream
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", # Better for web streaming
            "-shortest",
            str(output_file)
        ], check=True)

        return {
            "status": "success",
            "output_path": str(output_file)
        }

    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Subprocess failed: {e}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        # Cleanup
        if work_dir.exists():
            shutil.rmtree(work_dir)

def main():
    parser = argparse.ArgumentParser(description="G-Rec Audio Enhancer Standard Tool")
    parser.add_argument("--preset", choices=["broadcast", "aggressive"], default="broadcast", help="Processing preset")
    parser.add_argument("--input", required=True, help="Path to input video/audio file")
    
    args = parser.parse_args()
    
    result = run_processing(args.input, args.preset)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()