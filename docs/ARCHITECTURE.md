# 🏗️ G-Rec Architecture & Design Philosophy

## 1. The Core Philosophy: "Directory-as-Context"
G-Rec operates on a simple premise: **The File System is the Source of Truth.**
Instead of relying on hidden vector databases or opaque memory streams, G-Rec uses the visible folder structure to manage its context.

- **`core/`**: The Brain (Long-term rules).
- **`skills/`**: The Limbs (Executable capabilities).
- **`references/`**: The Knowledge (Injectable context).

## 2. Token Efficiency: The "Lazy Loading" Strategy
One of G-Rec's primary advantages is **Token Optimization**.

### The Problem
Traditional agents inject ALL available tool definitions into the System Prompt.
- If you have 50 tools, you waste ~2k tokens per turn just defining them.
- This creates "Noise" and distracts the model.

### The G-Rec Solution
G-Rec uses a **Two-Tier Context System**:

1.  **Tier 1 (Always Loaded)**: `SKILL_INDEX.md`
    - Contains only a one-line summary of each skill.
    - Cost: Very Low (< 100 tokens).
2.  **Tier 2 (On-Demand)**: `skills/[name]/SKILL.md`
    - Contains the heavy, detailed prompt engineering for a specific tool.
    - Loaded ONLY when the specific skill is activated.

**Result**: You can have 1000+ skills in your repository without bloating your active context window.

## 3. The G-S Protocol (Gemini-Skill Protocol)
To ensure stability, every skill must adhere to this structure:

```text
skills/my_new_tool/
├── SKILL.md       # The "Prompt" (Natural Language for the AI)
└── tool.py        # The "Code" (Python/Bat for the Machine)
```

- **Separation of Concerns**: The AI reads English (`SKILL.md`), the System executes Code (`tool.py`).
- **Safety**: The AI never generates code to run directly; it only invokes pre-verified `tool.py` scripts.
