import sys
import json
import subprocess
import argparse
import os
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
SKILLS_DIR = PROJECT_ROOT / "skills"
OUTPUT_DIR = PROJECT_ROOT.parent / "output" # Assuming output adjacent to G-Rec

# Tools
LP_TOOL = SKILLS_DIR / "live_portrait" / "tool.py"
AE_TOOL = SKILLS_DIR / "audio_enhancer" / "tool.py"

def run_skill(tool_path, args):
    """Run a G-S Protocol skill and return output path."""
    cmd = [sys.executable, str(tool_path)] + args
    print(f"🎬 [Workflow] Executing: {tool_path.name}...")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', check=False)
        data = json.loads(result.stdout)
        
        if data.get("status") == "success":
            return data["output_path"]
        else:
            print(f"❌ [Error] Skill Failed: {data.get('message')}")
            if result.stderr: print(f"🔍 Stderr: {result.stderr}")
            return None
    except Exception as e:
        print(f"❌ [System Error] Failed to run {tool_path.name}: {e}")
        return None

def merge_assets(video_path, audio_path, output_path):
    """
    Loops the video to match audio length and merges them.
    Command: ffmpeg -stream_loop -1 -i vid -i aud -shortest -map 0:v -map 1:a ...
    """
    print(f"🔨 [Workflow] Merging into final video...")
    
    cmd = [
        "ffmpeg", "-v", "error", "-y",
        "-stream_loop", "-1",       # Loop video indefinitely
        "-i", str(video_path),      # Input 0: Video
        "-i", str(audio_path),      # Input 1: Audio
        "-shortest",                # Stop when shortest input (audio) ends
        "-map", "0:v:0",            # Use video from input 0
        "-map", "1:a:0",            # Use audio from input 1
        "-c:v", "libx264",          # Re-encode video for compatibility
        "-c:a", "aac",              # Re-encode audio to AAC
        str(output_path)
    ]
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        print("❌ [Merge Error] FFmpeg failed to merge.")
        return False

def main():
    parser = argparse.ArgumentParser(description="G-Rec Blog Video Pipeline")
    parser.add_argument("--source", required=True, help="Image for LivePortrait")
    parser.add_argument("--voice", required=True, help="Voiceover audio/video file")
    parser.add_argument("--output", default="final_blog_video.mp4", help="Output filename")
    
    args = parser.parse_args()

    # Create Output Dir
    OUTPUT_DIR.mkdir(exist_ok=True)
    final_output = OUTPUT_DIR / args.output

    print("🚀 === G-Rec Production Line Started === 🚀")

    # 1. Generate Visuals (Idle Background)
    print("\n--- Phase 1: Visual Generation ---")
    bg_video = run_skill(LP_TOOL, ["--mode", "idle", "--source", args.source])
    if not bg_video: sys.exit(1)
    print(f"✅ Background Generated: {bg_video}")

    # 2. Process Audio (Enhancement)
    print("\n--- Phase 2: Audio Mastering ---")
    clean_voice = run_skill(AE_TOOL, ["--preset", "broadcast", "--input", args.voice])
    if not clean_voice: sys.exit(1)
    print(f"✅ Audio Mastered: {clean_voice}")

    # 3. Final Assembly
    print("\n--- Phase 3: Final Assembly ---")
    if merge_assets(bg_video, clean_voice, final_output):
        print(f"\n🎉 SUCCESS! Video saved to:\n👉 {final_output}")
    else:
        print("\n💥 FAILURE in final assembly.")

if __name__ == "__main__":
    main()