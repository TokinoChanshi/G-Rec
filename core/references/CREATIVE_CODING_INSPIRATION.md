# 🎨 Creative Coding & Motion Graphics Inspiration

> **Knowledge Base**: Curated patterns from Remotion, Processing, and Vibe Coding communities.
> **Purpose**: Style reference for G-Rec video engine.

## 1. 🏆 Remotion "Hall of Fame" (Official & Community)
*High-performance React-based motion graphics.*

### 🌟 "Wrapped" Style (Data Storytelling)
*   **Reference**: Spotify Wrapped / GitHub Unwrapped.
*   **Key Tech**: Kinetic Typography (Moving text), Quick transitions (0.2s), Bold Color Palettes.
*   **G-Rec Implementation**: Use `spring()` for elastic text pop-ups.

### 🧊 3D Product Showcases (Apple Style)
*   **Reference**: iPhone landing pages, Vercel Ship keynotes.
*   **Key Tech**: `@remotion/three`, Floating 3D GLTF models, Soft shadows, Depth of Field (Bokeh).
*   **G-Rec Implementation**: `ThreeBasicScene.tsx` with slow camera rotation.

### 💻 Code Walkthroughs (The "God-Tier" Tutorial)
*   **Reference**: Code Hike, Delba's Vercel Demos.
*   **Key Tech**: "Focus" spotlight on code lines, syntax highlighting animations, smooth scrolling.
*   **G-Rec Implementation**: Animate `scrollTop` of a code container code block.

---

## 2. 🌊 Processing / p5.js "Vibe" Patterns
*Generative art for atmospheric backgrounds.*

### 🌌 Flow Fields (流场)
*   **Description**: Thousands of particles tracing invisible paths created by Perlin Noise.
*   **Vibe**: Organic, Liquid, Wind-like.
*   **Use Case**: Background for "Deep Focus" or "Philosophy" videos.

### 🔲 Geometric Minimalism (包豪斯风格)
*   **Description**: Simple shapes (Circles, Lines) moving in perfect mathematical harmony (Sine waves).
*   **Vibe**: Clean, Intellectual, Precise.
*   **Use Case**: Tech explanation backgrounds.

### 🔊 Audio Reactivity (声光同步)
*   **Description**: Visuals that scale/color-shift based on Audio FFT (Frequency).
*   **Vibe**: High Energy, Immersive.
*   **Use Case**: Podcast clips, Music visualizers.

---

## 3. 🧠 Integration Strategy
**How G-Rec combines them:**
1.  **Layer 1 (Background)**: `Processing-Vibe` (Atmosphere).
2.  **Layer 2 (Content)**: Remotion `DOM` elements (Images, Text, Code).
3.  **Layer 3 (Overlay)**: `Three.js` Particles or Glitch effects.
