# ⚡ Module 5: Beast Mode — Autonomy & Prompt Engineering

Push beyond pair‑programming into autonomous AI coding. In this 30‑minute module you’ll set up a “Beast Mode” prompt, practice precise instruction writing, and run an act‑first agent. A short chat‑mode example is included.

Reference inspiration: Burke Holland’s Beast Mode gist — https://gist.github.com/burkeholland/88af0249c4b6aff3820bf37898c8bacf

---

## 🎯 Goals (30 minutes)

- Write high‑leverage instructions that steer an agent
- Run a full “act‑first” Beast Mode agent
- Practice safe change patterns: small diffs and checklists

---

## ⏱️ Timeboxed Agenda

- 5m — Setup and orientation
- 5m — Prompt primer (very concise)
- 15m — Activity: Full Beast Mode (act‑first)
- 5m — Debrief

---

## 🦁 What Is Beast Mode?

Beast Mode combines:
- A mindset: “Let AI take the first swing; I’ll own the merge.”
- A prompt style: crisp goal, constraints, acceptance criteria, and operating rules.
- A configuration: reusable `*.prompt.md` for Agent Mode and a chat‑mode variant.

When to use it:
- ✅ Structured features with clear constraints, boilerplate refactors, docs/tests generation
- ⚠️ Creative/UI exploration (pair closely and review often)
- 🚫 Critical fixes or risky migrations (prefer plan‑first + tests)

---

## ✍️ Prompt Primer (concise)

Mini‑spec checklist:
- Goal, Acceptance Criteria, Constraints
- Operating Rules: small diffs, keep runnable, ask before destructive changes
- Manual Test Checklist

Example upgrade: “Add task tags: store 0–N tags, accept comma‑separated input, display in list, filter via `?tag=…`, minimal diffs, include a manual test checklist.”

---

## 📦 Starter Artifacts

- `copilot/prompts/beast_mode_agent.prompt.md` — use in act‑first mode (see Autonomy section inside).
- `copilot/prompts/beast_mode_chat.prompt.md` — optional chat‑mode variant for quick review loops.

---

## 🧪 Activity: Full Beast Mode (Act‑First)

Run the agent prompt in act‑first mode (set in the prompt’s Autonomy section) to implement task tags end‑to‑end.

Suggested flow:
- “Run beast_mode_agent in act‑first mode for tags.”
- Let it propose and apply minimal diffs end‑to‑end.
- Validate against the Manual Test Checklist.

Observe:
- Speed vs. accuracy trade‑offs
- Diff size and risk profile
- Whether acceptance criteria are fully met

If results drift: tighten constraints and acceptance criteria.

---

## ⚙️ Quick Experiments (optional, time‑permitting)

- Add a stricter “Operating Rules” block → smaller, incremental diffs
- Expand the “Manual Test Checklist” → better self‑verification
- Toggle “ask before destructive changes” to feel autonomy shifts

---

## 💬 Chat Mode (optional)

Use `copilot/prompts/beast_mode_chat.prompt.md` for a quick, conversational run:

“Load the chat prompt. Draft a plan to add tags, then propose minimal diffs step‑by‑step, asking before destructive changes.”

---

## 🧱 Acceptance Checks (for any run)

- Criteria met and visible in UI where applicable
- No server errors in common flows (create/list/filter)
- Diffs are minimal and match repo’s structure and style

---

## 🧠 Reflection

- What changed when autonomy increased?
- Which constraints mattered most for quality?
- Where would you always keep a plan‑first gate?

---

⏭️ Continue to [docs/06_wrap_up.md](./06_wrap_up.md)
