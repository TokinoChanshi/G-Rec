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
VSM_TOOL = SKILLS_DIR / "video_sync_master" / "tool.py"

def run_skill(tool_path, args):
    """Run a G-S Protocol skill and return output path."""
    cmd = [sys.executable, str(tool_path)] + args
    print(f"🎬 [Workflow] Executing: {tool_path.name}...")
    
    try:
        # Use simple Popen or run. capture_output=True might hang if buffer fills on large output?
        # Using run with text=True is standard.
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', check=False)
        
        # Try to parse last line as JSON if possible, or search for JSON block
        try:
            # Some tools might print logs then JSON. Simple heuristic:
            output_str = result.stdout.strip()
            if not output_str:
                print(f"❌ [Error] No output from {tool_path.name}")
                if result.stderr: print(f"🔍 Stderr: {result.stderr}")
                return None

            # Attempt to find JSON structure if mixed with logs
            if output_str.endswith("}"):
                # Find last opening brace
                idx = output_str.rfind("{")
                if idx != -1:
                    json_str = output_str[idx:]
                    data = json.loads(json_str)
                else:
                    data = json.loads(output_str)
            else:
                data = json.loads(output_str)
                
            if data.get("status") == "success" or data.get("success") is True:
                # VSM returns "output" or "output_path" or "audio_path"
                return data.get("output_path") or data.get("output") or data.get("audio_path")
            else:
                print(f"❌ [Error] Skill Failed: {data.get('message') or data.get('error')}")
                if result.stderr: print(f"🔍 Stderr: {result.stderr}")
                return None
        except json.JSONDecodeError:
            print(f"❌ [Error] Invalid JSON from {tool_path.name}")
            print(f"🔍 Output start: {output_str[:200]}...")
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
    parser.add_argument("--dub", help="Target language to dub the final video into (e.g. 'English')")
    
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
        print(f"\n🎉 Video Assembled: {final_output}")
    else:
        print("\n💥 FAILURE in final assembly.")
        sys.exit(1)

    # 4. Optional Dubbing
    if args.dub:
        print(f"\n--- Phase 4: AI Dubbing ({args.dub}) ---")
        dub_output = run_skill(VSM_TOOL, ["dub", "--video", str(final_output), "--lang", args.dub])
        if dub_output:
            print(f"✅ Dubbing Complete: {dub_output}")
        else:
            print("❌ Dubbing Failed.")

if __name__ == "__main__":
    main()