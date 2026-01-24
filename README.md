# G-Rec (Gemini Reconstruction)

<div align="center">

![Gemini 3.0 Pro](https://img.shields.io/badge/Model-Gemini%203.0%20Pro-4285F4?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge)
![Role](https://img.shields.io/badge/Role-Multi--Persona-purple?style=for-the-badge)

**A Multi-Persona AI Framework for Codebase Evolution & Content Production.**  
**基于 "多重人格" 架构的本地化全栈工程伙伴。**

[English](#english) | [中文](#chinese)

</div>

---

<a name="english"></a>
## 🌍 English Introduction

**G-Rec** is a localized CLI agent architecture powered by **Gemini 3.0 Pro**.

> **💡 Inspiration & Credits**:
> This project is heavily inspired by **[claude-Reconstruction](https://github.com/Arxchibobo/claude-Reconstruction)** created by **[Arxchibobo](https://github.com/Arxchibobo)**.
> We stand on the shoulders of giants to evolve the "Directory-as-Context" philosophy for **Windows Native Environments** and **Automated Video Production**.

G-Rec implements a **Hybrid Engine** capable of both deep Codebase Understanding and Automated Content Production.

> **⚠️ Open Source Disclaimer**:
> This repository contains the **G-Rec Core Framework** only.
> Proprietary skills (e.g., LivePortrait) are excluded. You must implement your own skills following the [Contributing Guide](docs/CONTRIBUTING.md).

### 🌟 Key Features

*   **⚡ Token Efficiency (Lazy Loading)**: Unlike traditional agents, G-Rec does not bloat context with unused tools. It loads skill definitions on-demand. (See [Architecture](docs/ARCHITECTURE.md))
*   **🧠 Dual Core Engine**:
    *   **Architect Mode**: Deep understanding and refactoring of complex projects via `references/` injection.
    *   **Producer Mode**: Automating creative workflows (Video/Audio) via the **G-S Protocol**.
*   **📚 Knowledge Injection**: Simply drop PDF/MD files into `references/`, and G-Rec creates an instant knowledge base without RAG setup.
*   **🪟 Windows Native**: Optimized for local Windows environments (PowerShell, encoding, paths).

### 📚 Documentation
*   [**Architecture & Design**](docs/ARCHITECTURE.md): How it works and why it saves tokens.
*   [**Dynamic Roles**](docs/ROLES_GUIDE.md): Meet the Architect, the Producer, and the SRE.
*   [**Contributing Skills**](docs/CONTRIBUTING.md): How to build your own tools.
*   [**Prompting Guide**](docs/PROMPTING.md): Best practices for interaction.

---

<a name="chinese"></a>
## 🇨🇳 中文介绍

**G-Rec** 是一个基于 **Gemini 3.0 Pro** 的本地化智能体架构。

> **💡 致敬与灵感**:
> 本项目深受 **[Arxchibobo](https://github.com/Arxchibobo)** 大佬的 **[claude-Reconstruction](https://github.com/Arxchibobo/claude-Reconstruction)** 项目启发。
> 我们对其提出的 "Directory-as-Context" (目录即上下文) 理念进行了**Windows 本地化适配**与**视频生产场景**的深度拓展。在此向原作者表示诚挚感谢！

通过 **多重人格 (Multi-Persona)** 机制，G-Rec 打造了一个既能重构代码，又能自动化生产内容的双核 AI 引擎。

> **⚠️ 开源免责声明**:
> 本仓库仅包含 **G-Rec 核心框架**。
> 具体技能模块请参考文档自行扩展。

### 🌟 核心亮点

*   **⚡ 极致节省 Token**: 采用“懒加载”机制，只有在使用特定技能时才加载上下文，支持无限扩展技能库而不降低模型智商。(详见 [架构文档](docs/ARCHITECTURE.md))
*   **🧠 双核驱动**:
    *   **架构师模式**: 直接读取 `references/` 文档库，秒级理解陌生代码。
    *   **制作人模式**: 通过 G-S 协议调用本地 Python 工具，实现媒体生产自动化。
*   **📚 知识注入**: 只要把 PDF/MD 扔进 `references/` 目录，无需配置向量数据库，AI 立刻学会新知识。
*   **🪟 Windows 深度适配**: 专为本地开发者打造，解决中文路径和环境依赖痛点。

### 📚 文档中心
*   [**架构原理**](docs/ARCHITECTURE.md): 了解它是如何帮你省钱的。
*   [**角色指南**](docs/ROLES_GUIDE.md): 认识架构师、制作人和 SRE。
*   [**技能贡献**](docs/CONTRIBUTING.md): 手把手教你写插件。
*   [**提示词指南**](docs/PROMPTING.md): 让 AI 听懂你的话。

### 🚀 Quick Start

> **🐣 New to CLI? / 小白用户？**
> Don't know how to run commands? Just copy the prompt from [**INSTALL_GUIDE_FOR_AI.md**](INSTALL_GUIDE_FOR_AI.md) and paste it to your AI Assistant.
> 不懂代码？直接复制 [**给 AI 的安装指令**](INSTALL_GUIDE_FOR_AI.md) 发给你的 Gemini 即可。

1.  **Initialize**: `setup.bat`
2.  **Add Skills**: Drop python tools into `skills/`.
3.  **Run**: `python workflows/make_blog_video.py`

## 📜 License
MIT License.
