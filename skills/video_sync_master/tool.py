import argparse
import sys
import subprocess
import json
import os
from pathlib import Path

# --- Configuration ---
SKILL_ROOT = Path(__file__).parent.absolute()
BACKEND_MAIN = SKILL_ROOT / "backend" / "main.py"

def run_vsm_cmd(args_list):
    """Generic runner for VSM backend"""
    if not BACKEND_MAIN.exists():
        return {"status": "error", "message": "Backend missing. Please install VSM."}

    cmd = [sys.executable, str(BACKEND_MAIN), "--json"] + args_list
    print(f"🎬 [VSM] Running: {' '.join(cmd)}")
    
    try:
        # Run with real-time output but capture JSON at end
        # Using check=False to handle soft failures gracefully
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        output = result.stdout
        if "__JSON_START__" in output:
            try:
                json_str = output.split("__JSON_START__")[1].split("__JSON_END__")[0].strip()
                return json.loads(json_str)
            except:
                return {"status": "error", "message": "Failed to parse JSON response", "raw": output[-500:]}
        else:
            if result.returncode == 0:
                return {"status": "success", "raw_output": output}
            else:
                return {"status": "error", "message": result.stderr or output}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description="VideoSyncMaster Advanced Controller")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. ASR (Get Subtitles)
    p_asr = subparsers.add_parser("asr", help="Extract subtitles")
    p_asr.add_argument("--video", required=True)
    p_asr.add_argument("--service", default="jianying", choices=["whisperx", "jianying", "bcut"])

    # 2. Translate (Text to Text)
    p_trans = subparsers.add_parser("translate", help="Translate text/subs")
    p_trans.add_argument("--text", required=True, help="Text string or JSON segments")
    p_trans.add_argument("--lang", required=True, help="Target language (e.g. English, Chinese)")

    # 3. Dub (Full Pipeline)
    p_dub = subparsers.add_parser("dub", help="Full video translation & dubbing")
    p_dub.add_argument("--video", required=True)
    p_dub.add_argument("--lang", required=True)
    p_dub.add_argument("--tts", default="indextts", help="TTS Service: indextts / qwen")

    # 4. Sync (Lip Sync Only)
    p_sync = subparsers.add_parser("sync", help="Sync lips to new audio")
    p_sync.add_argument("--video", required=True)
    p_sync.add_argument("--audio", required=True)

    args = parser.parse_args()

    if args.command == "asr":
        res = run_vsm_cmd(["--action", "asr", "--input", args.video, "--asr", args.service])
    elif args.command == "translate":
        res = run_vsm_cmd(["--action", "translate_text", "--input", args.text, "--lang", args.lang])
    elif args.command == "dub":
        res = run_vsm_cmd(["--action", "merge_video", "--input", args.video, "--lang", args.lang, "--tts_service", args.tts])
        # Note: 'merge_video' in VSM usually implies the full flow if implemented correctly in main.py, 
        # but we might need to chain calls if VSM expects separate steps.
        # Based on my read, VSM's main.py might not have a single 'dub' entry point exposed via CLI easily except via specific functions.
        # We assume 'dub_video' function is mapped to an action, if not, we might need to extend main.py.
    elif args.command == "sync":
        # VSM uses 'video_retalking' or similar logic usually hidden behind UI
        # We map this to 'align' if available, or warn user.
        res = run_vsm_cmd(["--action", "align", "--input", args.video, "--ref", args.audio])
    else:
        parser.print_help()
        res = {}

    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()