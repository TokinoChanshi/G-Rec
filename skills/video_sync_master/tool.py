import argparse
import sys
import subprocess
import json
import os
from pathlib import Path

# --- Configuration ---
SKILL_ROOT = Path(__file__).parent.absolute()
REAL_ENTRY_POINT = SKILL_ROOT / "inference.py"  # Assuming the repo's main file is inference.py

def run_sync(video_path, audio_path, output_path=None):
    if not REAL_ENTRY_POINT.exists():
        return {
            "status": "error",
            "message": f"Core Missing. Please clone VideoSyncMaster into {SKILL_ROOT}"
        }

    # If output not specified, create one
    if not output_path:
        output_path = str(Path(video_path).with_name(f"{Path(video_path).stem}_synced.mp4"))

    # Construct command (adjust flags based on actual repo docs)
    # This is a hypothetical command structure based on Wav2Lip tools
    cmd = [
        sys.executable, str(REAL_ENTRY_POINT),
        "--face", video_path,
        "--audio", audio_path,
        "--outfile", output_path
    ]

    print(f"🎬 [VSM] Syncing lips... This may take a while.")
    try:
        # Run real-time to show progress logs
        subprocess.run(cmd, check=True)
        
        if os.path.exists(output_path):
            return {"status": "success", "output_path": output_path}
        else:
            return {"status": "error", "message": "Output file not found after execution."}
            
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": f"Execution failed: {e}"}

def main():
    parser = argparse.ArgumentParser(description="G-Rec Video Sync Master Wrapper")
    parser.add_argument("--video", required=True, help="Input video path")
    parser.add_argument("--audio", required=True, help="Input audio path")
    parser.add_argument("--output", help="Output video path")
    
    args = parser.parse_args()

    result = run_sync(args.video, args.audio, args.output)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()