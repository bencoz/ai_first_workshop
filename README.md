# AI‑First Software Development Workshop

Hands‑on workshop to practice AI‑first workflows with GitHub Copilot, prompt files, and a small Flask app. Start with the agenda, then work through the modules.

## 🌟 Workshop Goals

- Introduce the AI‑First Software Development (AIFSD) mindset
- Learn to integrate GitHub Copilot and prompt engineering into daily development
- Practice real-world workflows using an open-source Flask to-do app
- Shift from human-led to AI-assisted and eventually AI-augmented coding

## 🧰 Tech Stack

- Python 3.10+
- Flask (based on [patrickloeber/flask-todo](https://github.com/patrickloeber/flask-todo))
- GitHub Copilot (Chat + Agent Mode)
- GitHub Agentic Workflows (automated documentation sync)
- Markdown & Prompt Files

## 🗂️ Project Structure

```.
├── .github/
│   ├── copilot-instructions.md      # Project-specific Copilot rules
│   ├── workflows/
│   │   └── update-docs.yml          # Automated documentation sync
│   ├── agents/                       # Agentic workflow definitions
│   └── aw/                           # Agentic workflows configuration
├── .vscode/
│   ├── settings.json                # VSCode + Copilot optimization
│   └── mcp.json                     # MCP server configuration
├── apps/
│   └── flask-todo/                  # Prebundled Flask to‑do app (used in Modules 3–5)
├── copilot-examples/                # Example prompts and chat modes
├── docs/                            # Workshop lessons and walkthroughs
├── requirements.txt                 # Flask app dependencies
└── README.md                        # You're here!
```

## ⚙️ Quick Start

### Prerequisites

- Python 3.10+
- Git
- VSCode (recommended)
- GitHub CLI (for Agentic Workflows)

SQLite is usually pre-installed on macOS/Linux. If needed, see [official instructions](https://www.sqlite.org/download.html).

### 1. Clone and Setup

```bash
git clone https://github.com/bencoz/ai_first_workshop.git
cd ai_first_workshop

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Configure environment (copy template)
cp .env.example .env
```

### 2. Run the App

```bash
cd apps/flask-todo
python init_db.py        # Initialize database
flask run                # Start the app
# or: python app.py
```

Open `http://127.0.0.1:5000` and add a task to confirm it works.

### 3. Setup VSCode (Recommended)

1. **Install Extensions:**
   - GitHub Copilot Chat
   - GitHub Copilot

2. **Sign in** to GitHub in VSCode

3. **Open the Repository** in VSCode

The repository includes optimized settings in `.vscode/settings.json`.

### 4. (Optional) Setup GitHub Agentic Workflows

```bash
gh extension install github/gh-agentic-workflows
gh aw compile
```

For complete setup instructions, see **[SETUP_GUIDE.md](./SETUP_GUIDE.md)**.

## 🧠 Workshop Modules

Start with the agenda, then follow each module:

- **Module 0 — Agenda** (overview): `docs/00_agenda.md`
- **Module 1 — AI‑First Principles** (30m): `docs/01_ai_first_principles.md`
- **Module 2 — Customizing GitHub Copilot** (45m): `docs/02_customizing_copilot.md`
- **Module 3 — AI Onboarding With an Open Source App** (30m): `docs/03_onboarding_exercise.md`
- **Module 4 — Implementing User Stories With AI** (60m): `docs/04_user_stories.md`
- **Module 5 — Beast Mode — Autonomy & Prompt Engineering** (30m): `docs/05_beast_mode.md`
- **Module 6 — Wrap‑Up & Reflection** (30m): `docs/06_wrap_up.md`

Example prompts for Modules 4–5 are in `copilot-examples/`.

## 🤖 Automation & Documentation

This repository includes **GitHub Agentic Workflows** that automate documentation updates:

### Workflow: `update-docs`

- **Trigger:** Every push to `main`
- **Purpose:** Keeps documentation synchronized with code changes
- **Output:** Draft pull requests with documentation updates

**Configuration:** `.github/workflows/update-docs.yml`

**Details:** See `.github/workflows/update-docs.md` for full workflow description and philosophy.

## 🔧 Key Files & Conventions

### Copilot Configuration

- `.github/copilot-instructions.md` — Project-level Copilot rules and conventions
- `.vscode/settings.json` — VSCode settings for AI-First development
- `.vscode/mcp.json` — MCP server configuration for Agentic Workflows
- `copilot-examples/` — Example prompts, chat modes, and instructions

### Development

- `apps/flask-todo/` — Main Flask application
- `requirements.txt` — Python dependencies
- `.env.example` — Environment variables template

### Documentation

- `docs/` — Workshop modules and lessons
- `SETUP_GUIDE.md` — Complete setup instructions

## 🚀 Common Commands

```bash
# Activate virtual environment
source .venv/bin/activate  # or: .\.venv\Scripts\Activate.ps1 on Windows

# Run Flask app
cd apps/flask-todo && flask run

# Compile Agentic Workflows
gh aw compile

# View workflow runs
gh run list
```

## 📚 Resources

- [GitHub Copilot Documentation](https://github.com/features/copilot)
- [VSCode + Copilot Guide](https://code.visualstudio.com/docs/copilot/overview)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Awesome Copilot](https://github.com/github/awesome-copilot) — Community prompts and instructions

## 🛠️ Troubleshooting

For setup issues, database errors, or Copilot problems, see **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** or open a GitHub issue.

---

**Ready to start?** Begin with [SETUP_GUIDE.md](./SETUP_GUIDE.md), then move to `docs/00_agenda.md`.
