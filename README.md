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
- Markdown & Prompt Files

## 🗂️ Project Structure

```.
├── apps/
│   └── flask-todo/         # Prebundled Flask to‑do app (used in Modules 3–5)
├── copilot/                # Copilot instructions and prompts
├── docs/                   # Workshop lessons and walkthroughs
├── requirements.txt        # Flask app dependencies
└── README.md               # You're here!
```

## ⚙️ Setup Instructions

### Prerequisites
SQLite is usually pre-installed on macOS. If you need to install it, see the official instructions: https://www.sqlite.org/download.html

1. **Clone the repo**
   ```bash
   git clone https://github.com/bencoz/ai_first_workshop.git
   cd ai_first_workshop
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app** (choose one)
   - Flask CLI
     ```bash
     cd apps/flask-todo
     export FLASK_APP=app.py  # Windows PowerShell: $env:FLASK_APP="app.py"
     flask run
     ```
   - Python (auto‑creates DB on first run)
     ```bash
     cd apps/flask-todo
     python app.py
     ```

Open `http://127.0.0.1:5000` and add a task to confirm it works.

## 🧠 Workshop Modules

Start with the agenda, then follow each module:

- Module 1 — AI‑First Principles (30m): `docs/01_ai_first_principles.md`
- Module 2 — Customizing GitHub Copilot (45m): `docs/02_customizing_copilot.md`
- Module 3 — AI Onboarding With an Open Source App (30m): `docs/03_onboarding_exercise.md`
- Module 4 — Implementing User Stories With AI (60m): `docs/04_user_stories.md`
- Module 5 — Beast Mode — Autonomy & Prompt Engineering (30m): `docs/05_beast_mode.md`
- Module 6 — Wrap‑Up & Reflection (30m): `docs/06_wrap_up.md`

Prompts for Modules 4–5 live in `copilot/prompts/`.

See the full agenda at `docs/00_agenda.md`.
