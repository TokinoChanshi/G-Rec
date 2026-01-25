# AI Dataset Tagger (API Mode)

## Initial Assessment
Uses **Gemini API** via local script for high-throughput dataset labeling. 
Bypasses chat context limits, enabling processing of hundreds of images in one run.

## Core Principles
1.  **State-Less**: Each image is an independent API call. No context overflow.
2.  **SOTA Standard**: Natural language for Flux, tags for Pony.
3.  **Config Driven**: Uses `.env` for API Keys and Model selection.

## Playbooks

### Mode 1: Short Tags (`--mode short`)
- Danbooru-style keywords. Max 30 tags.

### Mode 2: Natural Caption (`--mode natural`)
- Fluent descriptions. Max 80 words.

### Mode 3: Trigger Training (`--mode trigger`)
- Starts with User-defined trigger word. Ideal for LoRA.

### Mode 4: Video Training (`--mode video`)
- Concise temporal motion description.

## Implementation Framework

### Step 1: Configuration
Ensure `GEMINI_API_KEY` is in your `.env`.

### Step 2: Execution
Run the tool directly. It will scan and process in batches.
```bash
python tool.py --mode trigger --trigger "N7" --input "./images" --batch 50
```

## Output Format
- JSON summary of processed files.
- Creates `.txt` files adjacent to each image/video.