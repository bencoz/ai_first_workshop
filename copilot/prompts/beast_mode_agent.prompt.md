---
mode: agent
model: gpt-4o
tools: ['codebase']
description: 'Add task tags (create, display, and filter by tag) with small, reviewable diffs.'
---

Context
- Repo: Flask To‑Do app from earlier modules.
- Preference: small diffs, runnable between steps, and clear file paths.

Goal
- Implement task tags end‑to‑end: store tags, allow entry on create, display in list, and support filtering.

Acceptance Criteria
- Each task may include 0–N tags (string labels).
- The create form accepts tags (comma‑separated is fine).
- Tags appear next to each task in the main list.
- Filtering via `/?tag=<name>` shows only tasks that include `<name>`.
- App remains runnable between steps; changes are minimal and readable.

Autonomy (Dial)
- Balanced (default): Propose a plan, await approval, then apply small diffs step‑by‑step.
- Beast: Act‑first to implement the minimal viable change set. Still keep diffs small.
- Careful: Ask clarifying questions and verify file paths before planning.

Plan‑First Instructions (Balanced)
- Draft a short plan with: affected files (exact paths), minimal diffs per file, and a manual test checklist.
- Confirm the plan first. Then show diffs for step 1 only. Keep steps small and runnable.

Operating Rules
- Keep edits minimal; prefer extending existing files over adding new ones.
- Cite exact file paths and show focused diffs.
- Ask before any destructive or schema‑altering change.
- If ambiguity arises (e.g., unknown data model), ask one clarifying question.

Constraints
- Follow the repo’s current routes/templates/data patterns.
- Avoid heavy dependencies. Use simple parsing for tags.
- Maintain current code style and structure.

Manual Test Checklist (target)
- Create a task with tags: “groceries” and “weekly” → appears with both tags listed.
- Visit `/?tag=weekly` → only tasks tagged “weekly” are shown.
- Create a task with no tags → UI remains correct.
- No server errors on create/list/filter flows.

