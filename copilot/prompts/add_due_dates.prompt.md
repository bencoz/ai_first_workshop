---
mode: agent
model: gpt-4o
tools: ['codebase']
description: 'Add due dates to tasks with minimal, reviewable diffs.'
---

Goal
- Implement due dates for tasks in the Flask To‑Do app.

Acceptance Criteria
- Task items store a `due_date` value.
- The create form accepts a date input.
- The main list displays the due date.

Plan‑First Instructions
- Propose a plan before code: acceptance criteria restated, affected files (paths), minimal change set, and a manual test checklist. Include an optional tiny pytest.
- Wait for approval. Then show diffs for step 1 only. Keep each step runnable.

Constraints
- Follow the repo’s existing routes, templates, and data model.
- Avoid heavy dependencies; prefer the simplest viable change.
- If a database/model exists, extend it minimally. If not, adapt the current storage pattern.

Manual Test Checklist (target)
- Create a task with a due date; see it listed with the date.
- Create a task without a due date; UI still works.
- No server errors for create/list flows.

