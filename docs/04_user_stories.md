# 🧾 Module 4: Implementing User Stories With AI

This session simulates working on real product features by letting AI help you implement **user stories** end-to-end, including routing, logic, and templates.

---

## 🎯 Goal

Use GitHub Copilot and prompt files to implement selected user stories in the Flask to-do app.

You’ll work in pairs or solo, and document your process along the way.

---

## 🧩 Step 1: Choose a User Story

Pick from the list below or create your own.

---

### 📌 Story 1: Add Due Dates to Tasks

**As a** user  
**I want** to assign a due date when creating a task  
**So that** I can manage my time better  

✅ Acceptance Criteria:
- `Task` model includes a `due_date` field
- `/add` route and form accepts a date
- Due date is shown on the homepage

---

### 📌 Story 2: Prioritize Tasks

**As a** user  
**I want** to assign a priority to tasks  
**So that** I know which tasks are most important  

✅ Acceptance Criteria:
- Priority (1–5) saved in DB
- Shown in list view (e.g. ⭐⭐⭐)

---

### 📌 Story 3: Add Task Filtering

**As a** user  
**I want** to filter tasks by priority or date  
**So that** I can focus on the right ones  

✅ Acceptance Criteria:
- Filter by due date or priority via URL param
- Homepage shows filtered results

---

### 📌 Story 4: Add Authentication (Optional)

**As a** user  
**I want** to log in  
**So that** only I can manage my tasks  

✅ Acceptance Criteria:
- Simple login (hardcoded or Flask-Login)
- Tasks tied to user session

---

## 🛠️ Step 2: Use Prompts

Use `copilot-examples/prompts/create_task.prompt.md` or create your own with:

```yaml
---
mode: agent
model: gpt-4o
tools: ['codebase']
description: 'Add due dates and priorities to the Flask to-do app'
---
```

---

## 🔍 Step 3: Review and Refactor

- Test manually in browser
- Ask Copilot to suggest improvements
- Refactor based on its feedback

---

⏭️ Continue to [docs/05_beast_mode.md](./05_beast_mode.md)
