# 🧭 Module 3: AI Onboarding With an Open Source App

Use AI to explore an unfamiliar codebase and produce lightweight onboarding docs in 30 minutes. You’ll practice asking effective questions, verifying answers against code, and turning findings into reusable documentation.

---

## 🎯 Goals (30 minutes)

- Understand app structure, routes, and data flow
- Create concise onboarding docs new devs can use immediately
- Practice an ask–verify loop to reduce AI hallucinations

---

## ⏱️ Timeboxed Agenda

- 5m — Setup and run the app
- 7m — Explore the code with AI
- 12m — Write onboarding docs (3 small artifacts)
- 6m — Verify, tidy, and share back (optional)

---

## 🔧 What You’ll Work With

We’ll use the open-source app [patrickloeber/flask-todo](https://github.com/patrickloeber/flask-todo), a small Flask project for adding and completing tasks. Clone it into `app/` in this repo.

If you’re offline, use a pre-bundled copy in `app/` and skip cloning.

---

## 🚀 Setup (5m)

From the root of this workshop repo:

```bash
# Clone (skip if app/ already exists)
git clone https://github.com/patrickloeber/flask-todo app

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1

# Install dependencies
if [ -f app/requirements.txt ]; then 
  pip install -r app/requirements.txt
else 
  pip install flask
fi

# Run the app (try one of these depending on repo layout)
cd app
export FLASK_APP=app.py && flask run   # Windows PS: $env:FLASK_APP="app.py"; flask run
# or: python app.py
```

Open http://127.0.0.1:5000 and add/complete a task to confirm it works.

---

## 🧪 Exercise 1: Explore With AI (7m)

Open the app folder in your editor and start a chat with your AI assistant (e.g., Copilot Chat). Use these prompts and verify answers in code:

Prompts:

1) “Give a high-level overview: entrypoint, main modules, data model, routes, and templates. Cite file paths and line numbers.”

2) “List all Flask routes with their handler functions and associated templates. Include file:line citations.”

3) “Explain the request flow when a user creates a task: which route, function, validation, data store, and redirect path?”

4) “Point out any implicit requirements: env vars, secrets, DB files, or Flask configuration.”

As you receive answers, open the cited files and lines to confirm accuracy. If something seems off, ask the AI to correct itself with updated citations.

---

## ✍️ Exercise 2: Create Onboarding Docs (12m)

Produce three small, high-signal docs inside the app. Keep each to 1–2 screens.

- `app/docs/quickstart.md` — Setup/run instructions and common pitfalls
- `app/docs/architecture.md` — Components, data model, and request flow
- `app/docs/routes.md` — Route → function → template map with brief behavior

Ask your AI assistant to draft each file, then you edit for accuracy and brevity.

Recommended prompts:

- “Draft a Quickstart for running this repo locally based only on files present here. Include prerequisites and copy-paste commands.”
- “Create an architecture overview describing modules, data model, and request flow with file references.”
- “Generate a routes table with route, function, template, and 1-line notes. Verify by reading decorators in code.”

---

## 🧱 Deliverable Templates

Use these as starting points and tune to the code you see.

`app/docs/quickstart.md`

```md
# Quickstart

## Prerequisites
- Python 3.10+
- Virtualenv (recommended)

## Setup
python -m venv .venv
source .venv/bin/activate        # Windows: .\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt   # or: pip install flask

## Run
export FLASK_APP=app.py && flask run  # Windows: $env:FLASK_APP="app.py"; flask run
# or: python app.py

## Troubleshooting
- If Flask cannot find the app, check FLASK_APP and working directory.
- If a SQLite file is used, ensure the process can write to the folder.
```

`app/docs/architecture.md`

```md
# Architecture

## Components
- Entry point: <file>
- Routes/handlers: <file(s)>
- Templates: <folder>
- Data storage: <file/tech>

## Data Model
- Task: { id, title, completed }

## Request Flow
```mermaid
flowchart TD
A[Browser] -->|GET /| B[index()] --> C[render index.html]
A -->|POST /add| D[add()] --> E[store new task] --> F[redirect /]
A -->|POST /complete| G[complete(id)] --> H[update task] --> F
```

## Key Dependencies
- Flask
- (Optional) SQLite / SQLAlchemy / Jinja2 templates
```

`app/docs/routes.md`

```md
# Routes

| Route | Function | Template | Notes |
|---|---|---|---|
| / | index | index.html | Lists tasks |
| /add | add | add.html | Creates task, then redirects |
| /complete | complete | – | Marks complete, then redirects |

> Source: verify with @app.route decorators in code.
```

---

## 🧪 Verify & Tidy (6m)

- Open each claim’s source file and line; fix any mismatches
- Confirm Quickstart runs on a clean machine (in principle)
- Keep commands copyable and paths accurate
- Trim fluff; prefer links to files over prose

Acceptance criteria:

- Docs build from actual code, not guesses
- Routes table matches real decorators
- Quickstart is runnable without missing steps

---

## 🌱 Stretch Goals (Optional)

- Add concise docstrings to key functions in the entry file
- Write an ADR: `app/docs/adr/0001-data-store.md` explaining where tasks live
- Propose a “good first issue” in a short checklist (bugs or DX polish)

---

## 🧑‍🏫 Facilitator Notes

- No network? Provide a pre-bundled `app/` and skip cloning
- Time checks at 10m and 20m to keep pace
- Share-out: have pairs show their routes table and 1 diagram; discuss how AI helped and where it hallucinated

---

📚 Using AI as your onboarding guide is a huge productivity booster when joining new teams or maintaining legacy apps.

Continue to [docs/04_user_stories.md](./04_user_stories.md) ▶️
