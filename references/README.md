# 📚 Knowledge Base (References)

**"Inject Knowledge directly into the Context Window."**

## Mechanism
Unlike traditional RAG (Retrieval-Augmented Generation) systems that slice documents into chunks, **G-Rec** leverages Gemini 3.0 Pro's massive context window.

Simply place external documentation here, and G-Rec will "read" and "understand" the entire library instantly.

## Usage
1.  **Download Documentation**: Get the `.md` or `.pdf` documentation of a library you want to use (e.g., `LangChain_Docs.pdf`, `PyTorch_Manual.md`).
2.  **Drop it here**: Place the file in this folder `G-Rec/references/`.
3.  **Activate**: Tell G-Rec: "Read the reference docs and explain how to implement X."

## Example Structure
```text
references/
├── openai_api_docs.md    # G-Rec now knows how to use OpenAI API
├── react_v19_changes.pdf # G-Rec now knows React 19 features
└── internal_wiki.txt     # G-Rec now knows your company's rules
```
