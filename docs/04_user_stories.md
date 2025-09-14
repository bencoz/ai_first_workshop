# 🧾 Module 4: Implementing User Stories With AI

Implement real product features end‑to‑end in the Flask To‑Do app using AI for planning, code changes, and verification. You’ll turn a user story into a small, reviewable PR with clear acceptance criteria.

---

## 🎯 Goals (60 minutes)

- Select a user story and write crisp acceptance criteria
- Create a plan and minimal change set with AI
- Implement routes, logic, and templates (small diffs) using Agent Mode
- Verify behavior manually and with lightweight tests/checklists
- Capture a short “story notes” doc for reuse

---

## ⏱️ Timeboxed Agenda

- 5m — Pick a story + agree on acceptance criteria
- 8m — Draft a plan: affected files, minimal diffs, test plan
- 27m — Implement with Copilot Agent Mode (iterate in small steps)
- 12m — Verify in browser and tidy (docs/tests)
- 8m — Prepare PR notes and share back

---

## 🔧 What You’ll Work With

- The same open‑source Flask app from Module 3 (in `app/`).
- Your editor with Copilot Chat enabled; Agent Mode preferred for applying diffs.
- Optional: `pytest` if you choose to add a smoke test.

If you didn’t complete Module 3, follow its Setup section to run the app locally, then return here.

---

## 🧩 Step 1: Choose a User Story

Pick one of the stories below (or write your own):

### 📌 Story 1: Add Due Dates to Tasks

As a user, I want to assign a due date when creating a task so that I can manage my time better.

Acceptance Criteria:
- Task items store a `due_date` (ISO date or display‑friendly)
- The create form accepts a date input
- Due date appears in the main list view

---

### 📌 Story 2: Prioritize Tasks

As a user, I want to assign a priority to tasks so that I know which tasks are most important.

Acceptance Criteria:
- Priority (1–5) is stored with each task
- Priority appears in the list (e.g., 1–5 or stars)
- Sorting or clear visual emphasis exists (even basic)

---

### 📌 Story 3: Filter Tasks by Date or Priority

As a user, I want to filter tasks so I can focus on the right ones.

Acceptance Criteria:
- URL/query params (e.g., `?priority=3` or `?due=today`) filter the list
- The homepage shows only matching tasks when a filter is present
- “Clear filter” path returns to the full list

---

### 📌 Story 4 (Optional): Add Authentication

As a user, I want to log in so that only I can manage my tasks.

Acceptance Criteria:
- Simple login (hardcoded user or Flask‑Login)
- Tasks are scoped to the current session/user

---

## 🗺️ Step 2: Draft a Plan (with AI)

Open Copilot Chat and use the 'new task.prompt.md' to start working with Copilot on the user story; then adjust specifics from your code.

Tip: Ask the model to cite file paths exactly as they exist.

---

## 🔬 Step 3: Verify and Tidy

- Run the app and manually test against each acceptance criterion
- If you added a quick test, run it (or write a tiny smoke test now)
- Update any docs touched (e.g., `app/docs/routes.md` and form fields)
- Keep changes small; prefer a simple visual for priority (e.g., stars or (P3))

Acceptance check:
- All criteria satisfied and visible in the UI (where applicable)
- No errors in server logs for common flows
- Code follows the existing style and routes structure

---

## 🧱 Deliverable Templates

Create a short story notes file in your feature branch:

`app/docs/story-notes.md`

```md
# Story Notes — <title>

## Acceptance Criteria
- <criterion>
- <criterion>

## Minimal Change Set
- <path>: <short diff summary>
- <path>: <short diff summary>

## Manual Test Checklist
- <step>
- <step>

## Follow‑ups
- <nice‑to‑have>
```

Optional PR description snippet:

```md
Title: <feature>: <short summary>

Why: Implements <story> with minimal changes.

What:
- <bullet list of concrete changes>

Verification:
- <steps/screenshots>
```

---

## 🌱 Stretch Goals (Optional)

- Add sorting controls to the list page (by priority or due date)
- Show relative due dates (e.g., “Due in 2 days”)
- Add a simple test for the filter logic using Flask’s test client
- Persist user login and scope tasks to user (if doing Story 4)

---

## 🧑‍🏫 Facilitator Notes

- Encourage pairs to keep diffs small and runnable between steps
- Time checks at 15m, 30m, 50m; share plans at 8m to unblock
- If offline, skip installing new packages; favor simple data additions
- Share‑out: each pair shows acceptance criteria, plan, and 1 screenshot

---

⏭️ Continue to [docs/05_beast_mode.md](./05_beast_mode.md)
