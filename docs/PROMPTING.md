# 💬 Prompting Guide

To get the most out of G-Rec (Gemini 3.0 Pro), use the following interaction patterns.

## 1. The "Role Switch" Trigger
Explicitly tell G-Rec which "Hat" to wear.

- **To fix bugs**: "Act as **Architect**. Analyze `make_blog_video.py` for race conditions."
- **To make content**: "Act as **Producer**. Generate a video from `assets/script.txt`."

## 2. The "Knowledge Injection" Pattern
Don't copy-paste code. Point to files.

- **Bad**: (Pasting 500 lines of code) "Fix this."
- **Good**: "Read `core/DECISION_TREE.md` and tell me if my new feature violates any rules."
- **Good**: "I put the `LangChain_Docs.pdf` in references. Read it and implement a Chain."

## 3. The "Chain of Thought" (CoT)
For complex tasks, ask for a plan first.

- "Plan the steps to refactor the audio module, then stop. Do not execute yet."
- G-Rec will list the steps.
- Then you say: "Proceed with Step 1."

## 4. Environment Context
G-Rec knows it is on **Windows**.
- It will automatically handle `\\` vs `/` path issues.
- It prefers `python` over `python3` (usually).
- It assumes access to PowerShell.

