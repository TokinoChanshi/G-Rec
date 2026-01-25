import argparse
import sys
import os
import json
from pathlib import Path

# G-Rec Native Mode: No external deps needed!
# We just verify files and tell the Agent what to do.

def scan_images(folder_path, extensions=[".jpg", ".png", ".webp"]):
    folder = Path(folder_path)
    if not folder.exists():
        return {"status": "error", "message": f"Folder not found: {folder_path}"}
    
    images = [str(p) for p in folder.glob("*") if p.suffix.lower() in extensions]
    
    if not images:
        return {"status": "warning", "message": "No images found."}
        
    # Return list for Agent to process
    return {
        "status": "success",
        "count": len(images),
        "images": images,
        "instruction": "Agent: Please iterate through these images using 'read_file' and generate tags/captions for each."
    }

def main():
    parser = argparse.ArgumentParser(description="G-Rec Dataset Tagger (CLI Native)")
    parser.add_argument("--folder", required=True, help="Path to image dataset")
    args = parser.parse_args()
    
    res = scan_images(args.folder)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()