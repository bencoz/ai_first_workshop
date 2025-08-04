# ⚡ Module 5: Vibe Coding With Beast Mode

This module introduces “Beast Mode” — an advanced prompt configuration that enables **autonomous AI coding** with minimal hand-holding. You’ll see how far Copilot can go when it has clear context, tools, and a goal.

---

## 🦁 What Is Beast Mode?

Beast Mode is:
- A mindset: “Let AI take the first swing”
- A prompt style: Clear, action-oriented instructions
- A configuration: `.prompt.md` + tool access

---

## 🧪 Activity 1: Use an Aggressive Prompt

Create a file: `copilot/prompts/beast_mode_add_feature.prompt.md`

```yaml
---
mode: agent
model: gpt-4o
tools: ['codebase']
description: 'Add the ability to assign tags to tasks and filter by tags on the homepage.'
---
```

Open Copilot Chat and say:

💬 *“Run the beast mode prompt and show me what changes are needed.”*

---

## 🧪 Activity 2: Let Copilot Write the Module

Prompt:

💬 *“Write the entire form, route, and database changes needed for this feature.”*

Then:
- Test the results
- Review them with a partner
- Ask Copilot to clean up or optimize the code

---

## 💬 Discussion: When To Use Beast Mode

| Use Case | Beast Mode Viable? |
|----------|--------------------|
| Adding a feature with known structure | ✅ Yes |
| Refactoring boilerplate | ✅ Yes |
| Creative UI design | ⚠️ Maybe |
| Critical bug fixes | 🚫 Not recommended |

---

## 🧠 Reflection Questions

- Did Beast Mode surprise you?
- When would you trust AI to take the lead?
- When do you want tight control instead?

---

⏭️ Wrap up in [docs/06_wrap_up.md](./06_wrap_up.md)
