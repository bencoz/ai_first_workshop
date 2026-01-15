# 🚀 Complete Setup Guide

This guide covers the full setup process for the AI-First Workshop, including environment configuration, VSCode optimization, and GitHub Agentic Workflows integration.

## Prerequisites

Before starting, ensure you have:

- **Python 3.10+** — Check with `python3 --version`
- **Git** — Check with `git --version`
- **VSCode** (optional but recommended) — [Download](https://code.visualstudio.com)
- **GitHub CLI** (`gh` command) — [Install](https://cli.github.com) (needed for Agentic Workflows)
- **SQLite** — Usually pre-installed on macOS/Linux; [install](https://www.sqlite.org/download.html) if needed

---

## 1. Clone and Environment Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/bencoz/ai_first_workshop.git
cd ai_first_workshop
```

### Step 2: Create and Activate Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Copy the example file and update as needed:

```bash
cp .env.example .env
```

Edit `.env` to set your configuration (if needed for development):

```env
# Database URL (default is fine for local development)
DATABASE_URL=sqlite:///instance/db.sqlite

# Flask settings
FLASK_APP=apps/flask-todo/app.py
FLASK_ENV=development
```

---

## 2. Initialize and Run the Flask App

### Initialize the Database

```bash
cd apps/flask-todo
python init_db.py
```

This creates the SQLite database (`db.sqlite`) with the Todo schema.

### Run the Application

**Option A: Using Flask CLI (Recommended)**
```bash
export FLASK_APP=app.py  # or: $env:FLASK_APP="app.py" on Windows PowerShell
flask run
```

**Option B: Run Directly**
```bash
python app.py
```

### Verify It's Working

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

You should see the Todo app homepage. Add a task to confirm the database is working.

---

## 3. VSCode Setup (Recommended)

### 3.1 Install VSCode Extensions

1. **GitHub Copilot Chat** — Enables Copilot chat and Agent Mode
   - Open VSCode → Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X`)
   - Search "GitHub Copilot Chat"
   - Install and sign in with your GitHub account

2. **GitHub Copilot** (if not already installed) — Base Copilot functionality
   - Search "GitHub Copilot"
   - Install and authenticate

### 3.2 Configure VSCode Settings

The repository includes a pre-configured `.vscode/settings.json` that optimizes for AI-First Development:

```json
{
    "github.copilot.enable": {
        "markdown": true
    }
}
```

**What this does:**
- Enables GitHub Copilot for Markdown files (useful for writing documentation and prompts)

**To apply additional settings:**

1. Open VSCode Settings (`Cmd+,` on macOS, `Ctrl+,` on Windows/Linux)
2. Search for `github.copilot` to see available options
3. For more granular control, edit `.vscode/settings.json` directly

**Recommended Additional Settings** (optional):

Add these to `.vscode/settings.json` for an AI-First workflow:

```json
{
    "github.copilot.enable": {
        "markdown": true
    },
    "chat.agent.enabled": true,
    "chat.agent.maxRequests": 100,
    "github.copilot.chat.agent.runTasks": true,
    "chat.mcp.discovery.enabled": true
}
```

For the latest VSCode + Copilot settings, see:  
[VS Code — Copilot Settings Reference](https://code.visualstudio.com/docs/copilot/reference/copilot-settings)

### 3.3 Configure GitHub Copilot Custom Instructions

1. Open **Copilot Chat** in VSCode (Cmd+Shift+I or Ctrl+Shift+I)
2. Click the **⚙️ gear icon** → **Instructions**
3. Select **New Instructions File** → **User Data Folder**
4. Add a brief personal instruction set:

```
You are collaborating with me as a staff-level engineer.
Keep answers brief and actionable. Propose a plan first, then offer small diffs.
Prefer clarity over cleverness. Suggest tests when risk is high.
Call out assumptions and safer alternatives.
```

5. Create a **Workspace** Custom Instructions file by opening `.github/copilot-instructions.md`
   - This file contains project-specific rules for Copilot
   - Copilot automatically reads it for workspace context

---

## 4. GitHub Agentic Workflows (Optional but Recommended)

### 4.1 Install GitHub CLI and Agentic Workflows Extension

If you haven't already installed the GitHub CLI, follow the [official guide](https://cli.github.com).

Then install the Agentic Workflows extension:

```bash
gh extension install github/gh-agentic-workflows
```

### 4.2 VSCode MCP Server Setup

The repository includes an MCP (Model Context Protocol) server configuration in `.vscode/mcp.json`:

```json
{
  "servers": {
    "github-agentic-workflows": {
      "command": "gh",
      "args": ["aw", "mcp-server"],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

**What this does:**
- Enables the GitHub Agentic Workflows MCP server in VSCode
- Allows Copilot to execute agentic workflows directly from the editor
- Provides context about repository workflows and agents

**To enable MCP in VSCode:**

1. Open VSCode **Settings** (Cmd+, or Ctrl+,)
2. Search for `mcp`
3. Find and enable **MCP (Model Context Protocol)** support
4. Restart VSCode

### 4.3 Understand the Workflows

The repository includes several automation workflows in `.github/workflows/`:

- **update-docs.yml** — Synchronizes documentation with code changes automatically
  - Triggered on every push to `main`
  - Creates draft PRs with documentation updates
  - See `.github/workflows/update-docs.md` for details

- **copilot-setup-steps.yml** — Helps set up Copilot for this workspace

**To compile and test workflows:**

```bash
# From repository root
gh aw compile

# Run a specific workflow
gh aw run update-docs --ref main
```

### 4.4 Agents

The repository includes pre-built AI agents in `.github/agents/`:

- **create-agentic-workflow.agent.md** — Creates new workflow automation
- **debug-agentic-workflow.agent.md** — Debugs existing workflows
- **upgrade-agentic-workflows.md** — Upgrades workflow dependencies

Use these by invoking them via the GitHub CLI or Copilot Chat (when MCP is enabled).

---

## 5. Common Commands & Workflows

### Development

```bash
# Activate virtual environment
source .venv/bin/activate  # or: .\.venv\Scripts\Activate.ps1 on Windows

# Run Flask app
cd apps/flask-todo && flask run

# Run tests (if added)
pytest

# Format code
black .

# Lint
flake8 .
```

### Git & GitHub

```bash
# Check status
git status

# Compile workflows
gh aw compile

# View workflow run
gh run list

# Check documentation workflow
gh run view <run-id>
```

### Database

```bash
# Reset database
rm apps/flask-todo/db.sqlite
cd apps/flask-todo && python init_db.py
```

---

## 6. Troubleshooting

### Virtual Environment Not Activating

**Problem:** `source: command not found` or similar

**Solution:**
- On **Windows**, use: `.\.venv\Scripts\Activate.ps1` (PowerShell) or `venv\Scripts\activate.bat` (Command Prompt)
- On **macOS/Linux**, use: `source .venv/bin/activate`
- Ensure you're in the repository root before activating

### Flask App Won't Start

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate
# Reinstall dependencies
pip install -r requirements.txt
```

### Database Errors

**Problem:** `OperationalError: unable to open database file`

**Solution:**
```bash
cd apps/flask-todo
python init_db.py  # Reinitialize
```

### Copilot Not Working in VSCode

**Problem:** No Copilot suggestions or chat unavailable

**Solution:**
1. Ensure you're signed in to GitHub in VSCode (`Cmd/Ctrl+Shift+P` → "GitHub Sign In")
2. Check that GitHub Copilot and GitHub Copilot Chat extensions are installed and enabled
3. Restart VSCode

### MCP Server Not Detected

**Problem:** MCP server errors in VSCode

**Solution:**
1. Ensure `gh` and agentic workflows extension are installed: `gh extension install github/gh-agentic-workflows`
2. Verify `.vscode/mcp.json` exists in the repository
3. Restart VSCode and check settings for MCP enablement

---

## 7. Next Steps

1. **Read the Workshop Agenda** — Start with `docs/00_agenda.md`
2. **Work Through Modules** — Follow `docs/01_ai_first_principles.md` through `docs/06_wrap_up.md`
3. **Explore Prompts** — Check `copilot-examples/` for task-specific Copilot prompts
4. **Customize Instructions** — Personalize `.github/copilot-instructions.md` for your team

---

## 📚 Additional Resources

- [GitHub Copilot Documentation](https://github.com/features/copilot)
- [VSCode + Copilot Guide](https://code.visualstudio.com/docs/copilot/overview)
- [Flask Documentation](https://flask.palletsprojects.com)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
- [Awesome Copilot](https://github.com/github/awesome-copilot) — Community prompts and instructions

---

For questions or issues, open a GitHub issue or discussion in this repository.
