# 🎛️ Module 2: Customizing GitHub Copilot

In this module, you'll learn how to **tune and shape Copilot's behavior** using `.copilot-instructions.md` and `.prompt.md` files to maximize its usefulness on your project.

---

## 🧩 Why Customize Copilot?

Out-of-the-box Copilot is helpful — but with a little guidance, it becomes a **true collaborator**. Customizing:
- Makes suggestions more relevant
- Enforces your coding conventions
- Adds domain knowledge or team norms

---

## 📄 `.copilot-instructions.md`

> A markdown-based instruction file that applies to all files (or scoped ones) in your repo.

### ✍️ Example:
```markdown
---
applyTo: "**/*.py"
---
# Copilot Instructions

Use Python 3.10+ features.
Always include type hints.
Prefer Flask best practices.
Use snake_case for variables and functions.
```

📁 Place it in: `.github/copilot-instructions.md`

---

## 🧪 Activity: Add Instructions

1. Create the `.github/` folder in the root of your project
2. Add your own `.copilot-instructions.md` using the template above
3. Ask Copilot Chat:  
   💬 *“How will you behave based on this instruction file?”*

---

## ⚙️ `.prompt.md` — Optional But Powerful

This file defines:
- **The model** (e.g. GPT-4o)
- **Tool access** (e.g. codebase search)
- **Long-running goals** (“Refactor all views to class-based views”)

📁 Place it in: `.github/prompts/*.prompt.md`

---

## 🧪 Prompt Activity: Create a Goal

Write a `.prompt.md` for this scenario:
> "Add due dates and priorities to tasks in the Flask app."

Use this structure:
```yaml
---
mode: agent
model: gpt-4o
tools: ['codebase']
description: 'Add due dates and priority fields to the task model'
---
```

---

## 💬 Tips for Prompt Design

- Be specific about **intent** (“create a new route” vs “add a feature”)
- Scope your goals (single feature at a time)
- Use Chat to reflect and iterate

---

⏭️ Continue to [docs/03_onboarding_exercise.md](./03_onboarding_exercise.md)
