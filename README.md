# AI‑First Software Development Workshop

Welcome to the AI‑First Software Development Workshop — a hands-on, real-world guided experience for junior developers who want to master AI-first workflows and practices.

## 🌟 Workshop Goals

- Introduce the AI‑First Software Development (AIFSD) mindset
- Learn to integrate GitHub Copilot and prompt engineering into daily development
- Practice real-world workflows using an open-source Flask to-do app
- Shift from human-led to AI-assisted and eventually AI-augmented coding

## 🧰 Tech Stack

- Python 3.10+
- Flask (based on [patrickloeber/flask-todo](https://github.com/patrickloeber/flask-todo))
- GitHub Copilot
- Markdown & Prompt Files

## 🗂️ Project Structure

```.
├── apps/flask-todo/        # Flask to-do app
├── copilot-examples/       # Example Copilot instructions and prompts
├── docs/                   # Workshop lessons and walkthroughs
├── requirements.txt        # Flask app dependencies
└── README.md               # You're here!
```

## ⚙️ Setup Instructions

### Prerequisites
SQLite is usually pre-installed on macOS. If you need to install it, see the official instructions: https://www.sqlite.org/download.html

1. **Clone the Repo**
   ```bash
   git clone https://github.com/bencoz/ai_first_workshop.git
   cd ai_first_workshop
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Init the DB**
   ```bash
   cd apps/flask-todo && python init_db.py
   ```

6. **Run the App**
   ```bash
   flask run
   ```

Then go to `http://localhost:5000` in your browser.

## 🧠 Workshop Modules

Each module lives in the `docs/` folder and includes a combination of:
- Lessons
- Group exercises
- Prompts
- Live demos

## 🚀 Start with `docs/00_agenda.md`

Workshop Structure and Roadmap
This workshop is structured into six sessions, each focusing on a specific aspect of AI-first software development:

- [docs/01_ai_first_principles.md](docs/01_ai_first_principles.md) — AI-First Principles & Developer Mindset (30 min)
- [docs/02_customizing_copilot.md](docs/02_customizing_copilot.md) — Customizing GitHub Copilot (45 min)
- [docs/03_onboarding_exercise.md](docs/03_onboarding_exercise.md) — AI Onboarding with an Open Source App (45 min)
- [docs/04_user_stories.md](docs/04_user_stories.md) — Implementing User Stories with AI (60 min)
- [docs/05_beast_mode.md](docs/05_beast_mode.md) — Vibe Coding with Beast Mode (30 min)
- [docs/06_wrap_up.md](docs/06_wrap_up.md) — Wrap-Up & Reflection (30 min)

Feel free to navigate to each session’s document for detailed guidance. We recommend going through the sessions in order, as they build on each other.