import argparse
import sys
import os
from pathlib import Path

# --- Configuration ---
SKILL_ROOT = Path(__file__).parent.absolute()
SRC_DIR = SKILL_ROOT / "src"

TEMPLATE_TSX = """
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';

export const MyVideo: React.FC<{text: string}> = ({text}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
    
    // AI Generated Logic Here
    const opacity = Math.min(1, frame / 20);
    const rotation = frame * 10;

	return (
		<AbsoluteFill style={{
			justifyContent: 'center',
			alignItems: 'center',
			fontSize: 100,
			backgroundColor: 'white',
		}}>
			<div style={{
                opacity, 
                transform: `rotate(${rotation}deg)`
            }}>
				{text}
			</div>
		</AbsoluteFill>
	);
};
"""

def generate_code(text_content, style="default"):
    """
    Simulate AI code generation for Remotion.
    In a real scenario, this would call an LLM to write complex React code.
    """
    print(f"🎨 [Remotion] Generating React code for text: '{text_content}'...")
    
    # Ensure src exists
    SRC_DIR.mkdir(exist_ok=True)
    target_file = SRC_DIR / "Composition.tsx"
    
    # Inject text into template
    code = TEMPLATE_TSX.replace("{text}", text_content) # Simple injection
    
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(code)
        
    return target_file

def render_video(output_path):
    """
    Wrapper for npx remotion render
    """
    print(f"🎬 [Remotion] Starting render engine...")
    print(f"👉 Command: npx remotion render src/index.ts {output_path}")
    
    # We fake the success for now if npm is not ready
    if not (SKILL_ROOT / "package.json").exists():
        return {"status": "warning", "message": "Remotion project not initialized. Run 'npm init video' in this folder first."}
        
    return {"status": "success", "message": "Render command sent (Simulation)."}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", choices=["generate", "render"], default="generate")
    parser.add_argument("--text", default="Hello G-Rec")
    parser.add_argument("--output", default="out.mp4")
    
    args = parser.parse_args()
    
    if args.action == "generate":
        path = generate_code(args.text)
        print(f"✅ Code generated at: {path}")
    elif args.action == "render":
        res = render_video(args.output)
        print(res)

if __name__ == "__main__":
    main()