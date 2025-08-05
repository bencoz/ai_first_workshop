# 🧭 Module 3: AI Onboarding With an Open Source App

In this session, you'll practice using AI to explore and document a **new codebase**. The goal is to simulate how AI can help you onboard quickly and become productive with unfamiliar code.

---

## 👀 What You'll Work With

We’ll use [patrickloeber/flask-todo](https://github.com/patrickloeber/flask-todo), a simple Flask app that lets users add and complete tasks.

You'll clone it into the `apps/flask-todo/` folder of your workshop repo.

---

## 🧪 Exercise 1: Explore With Copilot Chat

1. Open any file (e.g. `app.py`)  
2. Start asking Copilot questions like:
   - “What is the purpose of this app?”
   - “Where are tasks stored?”
   - “Explain what the `index()` route does.”

3. Let Copilot summarize the model and routes.

---

## ✍️ Exercise 2: Generate Internal Docs

Choose one file and ask Copilot:
> “Write internal documentation as if onboarding a new dev to this file.”

Paste the output into a new `README.md` inside the app folder (e.g. `app/README.md`)

---

## 🎯 Bonus Challenge: Map the App

Ask Copilot:
> “Draw a map of the major routes and templates.”

Try to output:
```plaintext
Route: /           → Template: index.html
Route: /add        → Template: add.html
Route: /complete   → No template, redirects
```

---

## 🔁 Optional Extension

Prompt:
> “Add inline comments and docstrings to all functions in app.py”

Review what Copilot generates, and clean up or revise it.

---

📚 These skills help you **use AI as your onboarding guide** — a huge productivity booster when joining new teams or maintaining legacy apps.

Continue to [docs/04_user_stories.md](./04_user_stories.md) ▶️
