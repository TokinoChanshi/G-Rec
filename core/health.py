#!/usr/bin/env python3
"""
G-Rec System Health Monitor (The Doctor)
Performs a comprehensive diagnostic of the agent's environment, dependencies, and core files.
"""
import os
import sys
import shutil
import importlib.util
from pathlib import Path

# Fix: Import handling for standalone execution
try:
    from .config import PROJECT_ROOT, CORE_DIR, Colors
except (ImportError, ValueError):
    # Fallback if running directly
    sys.path.append(str(Path(__file__).parent))
    from config import PROJECT_ROOT, CORE_DIR, Colors

def check_binary(name):
    """Check if a tool is in PATH"""
    path = shutil.which(name)
    status = f"{Colors.OKGREEN}✅ Found{Colors.ENDC}" if path else f"{Colors.FAIL}❌ Missing{Colors.ENDC}"
    details = f"({path})" if path else ""
    print(f"  {name:<15} {status} {details}")
    return bool(path)

def check_python_module(name):
    """Check if a python package is installed"""
    spec = importlib.util.find_spec(name)
    status = f"{Colors.OKGREEN}✅ Found{Colors.ENDC}" if spec else f"{Colors.FAIL}❌ Missing{Colors.ENDC}"
    print(f"  {name:<15} {status}")
    return bool(spec)

def check_env_var(name):
    """Check if environment variable is set"""
    val = os.environ.get(name)
    status = f"{Colors.OKGREEN}✅ Configured{Colors.ENDC}" if val else f"{Colors.WARNING}⚠️ Not Set{Colors.ENDC}"
    masked = f"({val[:4]}...)" if val else ""
    print(f"  {name:<20} {status} {masked}")
    return bool(val)

def check_file(path_obj):
    """Check if file exists"""
    status = f"{Colors.OKGREEN}✅ Found{Colors.ENDC}" if path_obj.exists() else f"{Colors.FAIL}❌ Missing{Colors.ENDC}"
    print(f"  {path_obj.name:<20} {status}")
    return path_obj.exists()

def check_integrity():
    print(f"\n{Colors.HEADER}🏥 G-Rec System Health Report{Colors.ENDC}")
    print("=============================")

    # 1. Core Files
    print(f"\n{Colors.OKCYAN}[1] Core Integrity{Colors.ENDC}")
    core_files = [
        CORE_DIR / "SYSTEM_PROMPT.md",
        CORE_DIR / "SKILL_INDEX.md",
        CORE_DIR / "TASK_QUEUE.md",
        CORE_DIR / "MEMORY.md",
        CORE_DIR / "EVOLUTION_LOG.md",
        CORE_DIR / "manager.py",
        CORE_DIR / "task_manager.py",
        CORE_DIR / "prevention.py",
        CORE_DIR / "health.py",
        CORE_DIR / "config.py"
    ]
    integrity_score = 0
    for f in core_files:
        if check_file(f): integrity_score += 1
    
    # 2. External Tools
    print(f"\n{Colors.OKCYAN}[2] External Tools{Colors.ENDC}")
    tools = ["git", "ffmpeg", "ffprobe", "node", "npm", "code"]
    tool_score = 0
    for t in tools:
        if check_binary(t): tool_score += 1

    # 3. Python Dependencies (Critical)
    print(f"\n{Colors.OKCYAN}[3] Python Environment{Colors.ENDC}")
    libs = ["requests", "numpy", "cv2", "torch", "PIL", "yt_dlp", "dotenv"]
    lib_score = 0
    for l in libs:
        # Map import name to package name checks if needed, usually same
        import_name = "cv2" if l == "opencv-python" else l
        if l == "cv2": import_name = "cv2"
        if l == "PIL": import_name = "PIL"
        if l == "yt_dlp": import_name = "yt_dlp"
        if l == "dotenv": import_name = "dotenv"
        
        if check_python_module(import_name): lib_score += 1

    # 4. API Keys (Soft Check)
    print(f"\n{Colors.OKCYAN}[4] API Configuration (Optional){Colors.ENDC}")
    keys = ["OPENAI_API_KEY", "PEXELS_API_KEY", "PIXABAY_API_KEY"]
    key_score = 0
    for k in keys:
        if check_env_var(k): key_score += 1

    # Summary
    print("\n=============================")
    print(f"📊 Diagnostic Summary")
    print(f"  Core Files:  {integrity_score}/{len(core_files)}")
    print(f"  Tools:       {tool_score}/{len(tools)}")
    print(f"  Python Libs: {lib_score}/{len(libs)}")
    print(f"  API Keys:    {key_score}/{len(keys)}")
    
    if integrity_score < len(core_files):
        print(f"\n{Colors.FAIL}❌ CRITICAL: Core files are missing. Re-run setup or restore from git.{Colors.ENDC}")
    elif tool_score < 2: # Git and Node are bare minimum? FFmpeg highly recommended.
        print(f"\n{Colors.WARNING}⚠️ WARNING: Key tools missing. Some skills may fail.{Colors.ENDC}")
    else:
        print(f"\n{Colors.OKGREEN}✅ System Status: HEALTHY{Colors.ENDC}")

if __name__ == "__main__":
    check_integrity()
