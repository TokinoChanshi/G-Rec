# Skill: Remotion (Professional Motion Graphics)

## Description
Generate high-end 3D animations and UI demo videos using **React-based Remotion framework**.
Unlike generative AI, this is **parametric video**, allowing perfect control over text, timing, and 3D effects.

## Core Capabilities
1.  **3D Text Effects**: Using Three.js integration in Remotion.
2.  **UI Walkthroughs**: Animating code snippets or browser mockups.
3.  **Dynamic Templates**: Passing JSON data to React components to generate different versions.

## How to Run (G-S Protocol)
1.  **Step 1**: G-Rec (Architect) writes the React code into `skills/remotion/src/Composition.tsx`.
2.  **Step 2**: G-Rec (Producer) runs the render command:
```bash
python skills/remotion/tool.py --action render --output "demo.mp4"
```

## Protocol Definitions
- **Code Location**: `skills/remotion/src/`
- **Render Engine**: `npx remotion render`
