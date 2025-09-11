# 🗓️ AI‑First Workshop Agenda

Welcome to the AI‑First Software Development Workshop. This agenda outlines the modules, their learning goals, and expected outcomes for each session. Core runtime: ~4 hours (excluding breaks). Can expand to a full day with deeper practice and share‑outs.

---

## 🔹 Module 1: AI‑First Principles — Guided Discussion
- **Time**: 30 minutes
- **Goal**: Align on current state and introduce the AI‑first mindset; identify near‑term transition steps and quality gates.
- **Activities**:
  - Warm‑up framing (3 min) and Primer: AIFSD in 60 seconds
  - Discussion Topic 1 (8 min): Current state & habits — engaging questions
  - Discussion Topic 2 (10 min): Transition & quality gates — engaging questions
  - Wrap‑up (5 min): Commitments for the next week
- **Resource**: `docs/01_ai_first_principles.md`

---

## 🔹 Module 2: Customizing GitHub Copilot (VS Code)
- **Time**: 45 minutes
- **Goal**: Practice context engineering for Copilot — shape behavior with Custom Instructions, Knowledge, and plan‑first Agent Mode; configure VS Code for AIFSD.
- **Topics & Examples**:
  - Why customize: English as the “hottest language” and context engineering
  - Artifacts overview: `copilot-instruction`, `*.instructions`, `*.prompt`, and chat modes
  - AIFSD VS Code settings: agent enablement, max requests, MCP discovery, autoFix, tool auto‑approve
  - Personal quickstart: 6–10 line Global profile
  - Workspace rules and Knowledge attachments
  - Plan → Context → Edits: pack context first, then apply minimal diffs in Agent Mode
  - MCP overview: where it fits alongside Knowledge and Agent Mode
- **Resource**: `docs/02_customizing_copilot.md`

---

## 🔹 Module 3: AI Onboarding With an Open Source App
- **Time**: 30 minutes
- **Goal**: Use Copilot to explore and document an unfamiliar codebase
- **Activities**:
  - Explore the [Flask Todo App](https://github.com/patrickloeber/flask-todo)
  - Use Copilot chat to answer: "What does this route do?"
  - Generate Markdown documentation for one module
- **Resource**: `docs/03_onboarding_exercise.md` (prebundled app at `apps/flask-todo/`)

---

## 🔹 Module 4: Implementing User Stories With AI
- **Time**: 60 minutes
- **Goal**: Collaboratively implement real user stories with Copilot
- **Activities**:
  - Choose from pre-defined stories (see `docs/04_user_stories.md`)
  - Prompt Copilot to scaffold changes
  - Review generated code & write tests
- **Resource**: `docs/04_user_stories.md`

---

## 🔹 Module 5: Vibe Coding With Beast Mode
- **Time**: 30 minutes
- **Goal**: Experience autonomous AI workflows
- **Activities**:
  - Use an aggressive `.prompt.md` for agent-style flow (see `copilot/prompts/`)
  - Let Copilot generate entire modules
  - Pair-review with human feedback
- **Resource**: `docs/05_beast_mode.md`, prompts in `copilot/prompts/`

---

## 🔹 Module 6: Wrap-Up & Reflection
- **Time**: 30 minutes
- **Goal**: Internalize lessons and share takeaways
- **Activities**:
  - Quick self‑assessment and pair share‑outs (wins/frictions)
  - Start/Stop/Continue: 3–5 team commitments with owners
  - Feedback pulse + pick success metrics; next‑steps & close
- **Resource**: `docs/06_wrap_up.md`

---

🎯 *Recommended for groups of 4–6 people, working in pairs.*
