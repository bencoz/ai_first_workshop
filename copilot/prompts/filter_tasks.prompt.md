---
mode: agent
model: GPT-4.1
tools: ['codebase']
description: 'Add filtering by due date or priority via query params.'
---

Goal
- Filter the task list using URL query params (e.g., `?priority=3`, `?due=today`).

Acceptance Criteria
- Query params filter the tasks shown on the homepage.
- A visible way to clear filters returns to the full list.
- Works alongside existing list behavior.

Plan‑First Instructions
- Provide a plan: affected routes/templates, small diffs, and a manual test checklist. Confirm before applying code.
- Apply changes step‑by‑step, keeping the app runnable between steps.

Constraints
- Follow current route + template structure; minimal changes preferred.
- Avoid adding heavy date libraries; keep parsing simple.

Manual Test Checklist (target)
- Visit `/?priority=3` and see only priority 3 tasks.
- Visit `/?due=today` and see tasks due today (or an empty list).
- Use “Clear filter” to return to full list.

