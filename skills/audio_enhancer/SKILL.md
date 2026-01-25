# Audio Enhancer Pro

## Initial Assessment
Raw audio from microphones often contains noise (fans, hum) and lacks "radio presence". 
This skill applies a hybrid processing chain: **Deep Learning Denoising** (DeepFilterNet) followed by **Classic Broadcast DSP** (EQ, Compression, Loudness).

## Core Principles
1.  **Hybrid Approach**: AI is good at removing noise but bad at tone. DSP is good at tone but bad at noise. We use both.
2.  **Loudness Standards**: All output is normalized to **-16 LUFS** (Standard for Podcasts/Web Video).
3.  **Non-Destructive**: The original video track is replaced, but the video stream is copied (no re-encoding of video).

## Playbooks

### Pattern 1: Broadcast Voice (Standard)
*Best for: Vlogs, Tutorials, Talking Head.*
- **Pipeline**:
  1.  `DeepFilterNet` (Remove background noise).
  2.  `Highpass 90Hz` (Remove rumble).
  3.  `De-Mud 250Hz` (Clean up boxiness).
  4.  `Presence 3kHz` (Add clarity).
  5.  `Compressor` (Even out dynamics).
  6.  `Loudnorm` (Target -16 LUFS).

### Pattern 2: Aggressive Denoise (Clean Silence)
*Best for: Recordings with high background hiss or fan noise.*
- **Pipeline**:
  1.  `DeepFilterNet` (AI Denoise).
  2.  `Noise Gate (-50dB)`: Hard cut on silence.
  3.  `Lowpass 10kHz`: Remove high-frequency hiss.
  4.  `Gentle Compression`: Avoid amplifying floor noise.

## Implementation Framework

### 1. Dependencies
- **DeepFilterNet**: `pip install deepfilternet`
- **FFmpeg**: Must be in system PATH.

### 2. Execution Strategy
Use the standardized `tool.py` entry point.

```bash
python tool.py --input "path/to/video.mp4" --preset [broadcast|aggressive]
```

### 3. Quality Checks
- [ ] **Noise Floor**: Is the silence actually silent? (Use `aggressive` if not).
- [ ] **Color Integrity**: Check if brightness/contrast matches source (Remux must use `-map_metadata 0`).
- [ ] **Distortion**: Did the `Loudnorm` cause clipping?
- [ ] **Sync**: Is the audio still synced with the lips?

## Output Format
- **Success**: Returns JSON `{"status": "success", "output_path": "..."}`.
- **File**: Creates `*_cleaned.mp4` in the same directory as input (or specified output).
