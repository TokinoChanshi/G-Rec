# 🎬 G-Rec Release Demo Script
**Target Audience**: Developers & Content Creators
**Tone**: Cyberpunk / Industrial / "Just Works"
**Duration**: 45-60 seconds

## 📦 Prep Work (素材准备)
1. **The Face (视觉)**:
   - Copy `inputtest_dataset/_Cyber-Idol_Metallic_extra_detailed_Eye-catching_art._Hyper_r_bed9a419-9a33-4a43-87b8-f49d032c584c_0.png` to `workspace/avatar.png`.
2. **The Voice (听觉)**:
   - Record yourself (or use TTS) reading the **Script** below.
   - Save as `workspace/intro.mp3`.

### 🎙️ Voiceover Script (Chinese):
> "这是 G-Rec。一个运行在你本地的全自动视频生产线。
> 从一张照片，到一段语音，它能自动生成口型同步的数字人视频。
> 甚至，它还能利用 LLM 自动翻译，并克隆我的声音，生成英文版、日文版...
> 这一切，都在你的显卡上完成。不依赖云端，没有 API 费用。
> G-Rec, Automate your creativity."

---

## 🎥 Recording Sequence (录制流程)

### Scene 1: The Setup (0:00 - 0:10)
*   **Action**: Open your terminal (PowerShell/CMD) in `博客视频\G-Rec`.
*   **Visual**: Show the file explorer. A messy folder vs. the clean `G-Rec` structure.
*   **Voiceover**: (Lines 1-2) "这是 G-Rec..."

### Scene 2: The Command (0:10 - 0:20)
*   **Action**: Type this command slowly and clearly:
    ```powershell
    python workflows/make_blog_video.py --source workspace/avatar.png --voice workspace/intro.mp3 --dub English
    ```
*   **Voiceover**: (Lines 3-4) "从一张照片..."

### Scene 3: The Process (0:20 - 0:40)
*   **Action**: Hit ENTER.
*   **Visual**:
    - Watch the console logs scroll (Matrix effect).
    - Highlight specific logs: `[Visual Generation]`, `[Audio Mastering]`, `[AI Dubbing]`.
*   **Voiceover**: (Lines 5-6) "这一切，都在你的显卡上完成..."

### Scene 4: The Result (0:40 - 0:50)
*   **Action**: Open `output/final_blog_video.mp4`.
*   **Visual**: Play the video full screen.
*   **Audio**: Let the *generated* video audio play (showing off the lip-sync and dubbing).
*   **Voiceover**: (Line 7) "G-Rec, Automate your creativity."

---

## 🚀 Post-Recording
Upload to Bilibili/YouTube with tags: `#AI` `#LocalLLM` `#Automation` `#G-Rec`
