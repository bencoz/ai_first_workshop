# ⚡ Module 5: Beast Mode — Autonomy & Prompt Engineering

Push beyond pair‑programming into autonomous AI coding. In this 30‑minute module you’ll set up a “Beast Mode” chat-mode, practice precise instruction writing, and run an act‑first agent. The latest version (3.1) of the chat‑mode is included.

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
Beast Mode is a highly opinionated prompt engineering setup that transforms a code agent into a fully autonomous problem solver.
It includes:
- A structured workflow for solving coding problems.
- Aggressive use of tools (e.g., terminal, browser, file editing).
- Built-in planning and todo list tracking.
- Extensive internet research capabilities.
- A persistent, iterative mindset: the agent keeps working until the problem is fully solved.


When to use it:
- ✅ Structured features with clear constraints, boilerplate refactors, docs/tests generation
- ✅ Projects where the agent should take initiative and solve problems end-to-end.
- ⚠️ Creative/UI exploration (pair closely and review often)
- ⚠️ Tasks that require deep investigation, multi-step planning, and tool integration.
- 🚫 Critical fixes or risky migrations (prefer plan‑first + tests)

---

## 🧩 Installation Steps

In VS Code, go to the Agent dropdown in the chat sidebar.
Choose Configure Modes → Create new custom chat mode file.
Save it in the User Data Folder.
Name it Beast Mode and paste the contents of beastmode.chatmode.md.
It will now appear as a selectable mode in your agent dropdown.

---

## 📦 Starter Artifacts

- `copilot/prompts/beastmode3_1.chatmode.md` 

---
## 🧠 Activity1 : Prompt Engineering Techniques in Beast Mode

 Beast Mode leverages **advanced prompt engineering strategies** to transform a code agent into a highly autonomous, tool-using problem solver. These techniques are embedded throughout the configuration and are critical to its effectiveness.

### ✨ Key Techniques

#### 1. 🦾 Role Priming with Identity & Behavior
- **Purpose:** Sets a clear agent persona and expectations.
- **Effect:** Primes the model to act as a senior engineer—confident, proactive, and autonomous.
- **Reference:**
  - _"You are a senior software engineer and expert problem solver..."_

---

#### 2. 📝 Recursive Planning via Markdown Todo Lists
- **Purpose:** Externalizes reasoning and enables iterative refinement.
- **Effect:**
  - Encourages structured thinking
  - Enables self-monitoring
  - Promotes stepwise progress
- **Reference:**
  - _"Break the task into a markdown todo list..."_
  - *(See: Planning and Execution section)*

---

#### 3. 🛠️ Tool-First Thinking
- **Purpose:** Drives the agent to use tools aggressively and explain intent before acting.
- **Effect:**
  - Action-oriented problem solving
  - Thinks and acts like a developer
- **Reference:**
  - _"Before using a tool, explain what you are doing and why..."_
  - *(See: Tool Usage section)*

---

#### 4. 🚀 Autonomy & Persistence
- **Purpose:** Encourages the agent to keep working until the task is fully complete.
- **Effect:**
  - Goal-driven, persistent mindset
  - Self-directed problem solving
- **Reference:**
  - _"Never stop until the task is complete..."_
  - *(See: Completion Criteria section)*

---

#### 5. 🙅‍♂️ Minimizing User Dependency
- **Purpose:** Reduces interruptions and simulates independence.
- **Effect:**
  - Maintains flow
  - Lowers user cognitive load
- **Reference:**
  - _"Do not ask the user for help unless you are completely blocked..."_
  - *(See: User Interaction section)*

---

#### 6. 🧠 Contextual Memory & Self-Reflection
- **Purpose:** Promotes self-awareness and adaptive planning.
- **Effect:**
  - Remembers progress
  - Adjusts plans as needed
- **Reference:**
  - _"Update your todo list as you go..."_
  - *(See: Planning and Execution & Completion Criteria)*

---


## 🧪 Activity2: Full Beast Mode (Act‑First)

Use Beast Mode 3.1 in VS Code to implement a user story in the sample app.

The agent should:
1. Create a todo list.
2. Search for best practices for that user story content .
3. Modify the codebase
5. Test the implementation.
6. Document the change.

🧪 Agent Review Checklist
While the agent works, observe and document:

- ✅ Did it create a clear todo list?
- 🔍 Did it perform recursive web searches?
- 🛠 Did it use tools like editFiles, runCommands, or fetch?
- 🧪 Did it test the code thoroughly?
- 📄 Did it update documentation or README?
- 🧠 Did it store any memory or context?


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

## 🧠 Reflection

- What changed when the agent autonomy increased?
- Which instructions mattered most for quality?
- Where would you always keep a plan‑first gate?

---

⏭️ Continue to [docs/06_wrap_up.md](./06_wrap_up.md)
