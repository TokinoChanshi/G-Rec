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

如果你希望在电脑的任何文件夹下都能呼叫 G-Rec，且无需手动切换目录。
请**在 G-Rec 目录下**执行此指令，让 AI 将配置写入全局记忆。

### 📋 复制以下内容 (Copy This):

```text
你好 Gemini，现在请执行 **"全局注册"** 操作。
请找到我的全局记忆文件 (通常是 ~/.gemini/GEMINI.md 或类似的全局配置文件)。

请将以下 **"Mandatory Boot Protocol" (强制启动协议)** 块追加到全局记忆中：

## 🏗️ Project: G-Rec
- **Root Path**: [请自动填入当前 G-Rec 项目的绝对路径]

## ⚖️ Mandatory Boot Protocol (强制启动协议)
- **CRITICAL**: 你是 G-Rec 智能体的承载者。
- **Auto-Load (本地模式)**: 若当前目录在 `Root Path` 内，必须优先读取 `core/SYSTEM_PROMPT.md`。
- **Boomerang-Load (回旋镖加载)**: 若当前不在根目录，但用户下达 "启动 G-Rec" 指令：
    1. **Record**: 记录当前工作目录为 `[Target_Work_Dir]`。
    2. **Jump**: 执行 Shell 命令 `Set-Location -Path "[Root Path]"` (回城)。
    3. **Load**: 读取 `core/SYSTEM_PROMPT.md` 和 `core/ROLES.md` (加载人设)。
    4. **Return**: 执行 Shell 命令 `Set-Location -Path "[Target_Work_Dir]"` (返回战场)。
    5. **Report**: "🚀 G-Rec 人设加载完毕，已返回工作目录。请下达指令。"
- **Role Sync**: 必须始终根据 `core/ROLES.md` 维持人设。

## 🔑 Key Preferences
- **Language**: Strictly Chinese (简体中文).
- **Efficiency**: Use Lazy Loading for skills.
- **Safety**: No auto-run scripts without "Y/N" confirmation.

执行完毕后，请告诉我："全局强制协议已注册 (包含 Boomerang 回旋镖机制)，G-Rec 支持外勤任务了。"
```

---

## 💡 给高级用户的备注
如果你是开发者，你也可以直接运行仓库根目录下的 `setup.bat` (如果有) 来一键完成上述操作。
