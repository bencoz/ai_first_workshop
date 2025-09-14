---
mode: agent
model: GPT-4.1
tools: ['codebase']
description: 'Add task priority (1–5) and display in the list.'
---

Goal
- Let users assign a numeric priority to tasks and show it in the list.

Acceptance Criteria
- Priority (1–5) is stored with each task.
- Priority is visible in the main list (e.g., ⭐ or (P3)).
- Sorting or a clear visual emphasis exists (basic is fine).

Plan‑First Instructions
- Draft a minimal plan: files/paths, tiny diffs, and a quick manual test list.
- Confirm the plan first, then apply step 1 only. Keep steps small and runnable.

Constraints
- Fit changes into existing files and patterns.
- Avoid heavy UI work; a simple indicator is sufficient.
- If a schema exists, extend it minimally; otherwise adapt the current storage.

Manual Test Checklist (target)
- Create tasks with priority 1 and 5; both appear with correct indicators.
- List view remains functional and readable with/without priority.
- No server errors on add/list flows.

