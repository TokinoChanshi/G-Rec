# 🤖 给 AI 的安装指令 (G-Rec Bootstrap Protocol)

如果你是小白用户，不知道如何安装配置。
请直接**复制下面的这段话**，发送给你的 Gemini CLI (或任何终端 AI 助手)。

## 1. 基础安装 (必做)

### 📋 复制以下内容 (Copy This):

```text
你好 Gemini，我希望你在我的电脑上部署 "G-Rec" 框架。请扮演一名 [高级系统部署工程师]，严格按照以下步骤执行操作：

**任务 1: 环境自检**
请检查当前目录下是否已经安装了 git 和 python。如果缺少，请告诉我如何安装，不要继续。

**任务 2: 拉取框架**
请执行 git clone https://github.com/[YOUR_USERNAME]/G-Rec.git (如果仓库已存在，请进入该目录)。
*请注意：你需要将 [YOUR_USERNAME] 替换为实际的仓库地址，或者询问我地址。*

**任务 3: 初始化环境**
进入 G-Rec 目录后：
1. 检查是否存在 `setup.bat`。如果有，请运行它。
2. 如果没有，请帮我创建一个虚拟环境 (python -m venv venv)，并创建 requirements.txt 安装基础依赖 (python-dotenv, requests)。

**任务 4: 激活智能体**
请读取 `core/SYSTEM_PROMPT.md` 和 `core/ROLES.md`。
理解所有内容后，请向我汇报："G-Rec 系统已就绪。当前处于 [Architect] 模式。请下达指令。"

**任务 5: 知识注入 (可选)**
请扫描 `docs/` 目录下的所有文档，告诉我你学会了什么。

请一步步执行，每完成一步向我确认。
```

---

## 2. 全局集成 (选做 - 推荐)

如果你希望在电脑的任何文件夹下都能呼叫 G-Rec，请**在 G-Rec 目录下**执行此指令。

### 📋 复制以下内容 (Copy This):

```text
你好 Gemini，现在请执行 **"全局注册"** 操作。
请找到我的全局记忆文件 (通常是 ~/.gemini/GEMINI.md 或类似的全局配置文件)。

请将以下信息**追加**到全局记忆中：

## 🏗️ Project Integration: G-Rec
- **Status**: Registered
- **Path**: [请自动填入当前 G-Rec 项目的绝对路径]
- **Protocol**: Directory-as-Context
- **Instruction**: 当我要求 "进入 G-Rec 模式" 时，请切换工作目录到上述 Path，并读取该目录下的 core/SYSTEM_PROMPT.md。

执行完毕后，请告诉我："全局注册已完成，您现在可以在任何地方呼叫 G-Rec 了。"
```

---

## 💡 给高级用户的备注
如果你是开发者，你也可以直接运行仓库根目录下的 `setup.bat` (如果有) 来一键完成上述操作。