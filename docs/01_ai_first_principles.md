# 📘 Module 1: AI‑First Principles — Lecturer Discussion Guide

Teaching aid for a fast, facilitator‑led discussion on adopting an AI‑First Software Development (AIFSD) mindset — shifting from “AI as a helper” to “AI as a co‑creator.” Based on ideas from the AIFSD approach: https://github.com/tembo/aifsd

---

## 🎯 Learning Objectives

- Understand what “AI‑first” means for day‑to‑day development.
- Contrast current workflows with an AI‑first lifecycle (spec → scaffold → iterate → evaluate → ship → observe).
- Practice prompt‑first iteration and “own the merge” review habits.
- Define quality gates using lightweight evals and tests for AI‑touched code.
- Draft a practical adoption plan for your team/class.

---

## 🧑‍🏫 Who, Format, Materials

- Audience: Software engineers, tech leads, students (intermediate+).
- Format: Guided discussion (no demo in this segment).
- Duration: 30 minutes max (agenda below).
- Materials: Whiteboard or shared doc for notes.

---

## 🗓️ Suggested Agenda (30 minutes)

- 0–3 min — Warm‑up and framing
- 3–7 min — Primer: AIFSD in 60 seconds
- 7–15 min — Discussion Topic 1: Current state and habits
- 15–25 min — Discussion Topic 2: Transition and quality gates
- 25–30 min — Wrap‑up: commitments and next steps

---

## 🧠 Primer: AIFSD in 60 Seconds

- AI as collaborator: Co‑create specs, scaffolds, code, and documentation.
- Prompt‑first: Iterate on prompts/instructions before hand‑editing code.
- Own the merge: Humans remain accountable for quality and safety.
- Evals as guardrails: Define pass/fail checks for AI‑generated changes.
- Observe and improve: Add feedback loops; treat prompts as versioned artifacts.

---

## 🧑‍🤝‍🧑 Discussion Topic 1 — Current State & Habits

Engaging prompts to surface how the group works today:

- Where does AI currently show up (if at all)? What’s working vs. frustrating?
- For which tasks do you still start from scratch? Why not involve AI earlier?
- How do you decide when to accept, modify, or discard AI output?
- What are your existing quality gates (tests, reviews, linters)? Where would AI fit?
- Which parts of your SDLC feel slow or risky today? What’s the root cause?
- What risks (security, privacy, licensing, hallucination) actually block adoption?

Facilitator notes:
- Capture “bright spots” where AI already adds value.
- Note repeated friction (spec churn, boilerplate, integration, tests) for later mapping.

---

## 🔄 Discussion Topic 2 — Transition to AI‑First

Use these prompts to design a practical adoption path.

Mindset and roles:
- How does the developer’s role shift (orchestrator, curator, reviewer) in AI‑first teams?
- What does “own the merge” mean for code review and accountability?
- How will pairing change when one “pair” is an AI agent?

Process and artifacts:
- What new artifacts will you track? (prompt briefs, evals, examples, datasets)
- How will you version prompts and link them to code changes?
- Where in CI/CD will you run evals, and what are the pass/fail gates?

Architecture and tooling:
- Which AI patterns apply to your work? (retrieval, tools, agents, codegen)
- What data or context do your models need to be reliably helpful?
- What privacy, safety, or compliance rules constrain your setup?

Commitments (actionable, near‑term):
- What is one safe experiment we can run this week?
- What will we stop doing manually that AI can draft for us?
- What two quality gates can we adopt now (e.g., tests/evals + human review)?
- How will we capture and version prompts linked to PRs?

Adoption ladder (pick 2–3 for the next month):
- Use AI for summarizing code, tickets, and PRs.
- Prompt‑to‑scaffold new modules and tests; request diffs, not blobs.
- Add a lightweight eval for one critical path (e.g., golden tests for a function).
- Require “eval green + human review” for AI‑touched code.
- Start a prompt catalog (owners, examples, versions).
- Add basic observability to learn from failures.

---

## 🧭 Principles Cheat Sheet (AIFSD‑inspired)

- Think AI‑first: Ask “How would I solve this with AI?”
- Own the merge: Human accountability for quality and safety.
- Prompt over manual edits: Change prompts before editing code.
- Scaffold early, iterate often: From spec to minimal working skeleton.
- Evals as guardrails: Define success criteria and enforce them in CI.
- Data and docs as first‑class: Examples and contexts drive model quality.
- Version prompts and artifacts: Treat them like code.
- Observe and learn: Add telemetry and feedback loops.
- Risk‑based gates: Stricter checks for higher‑impact changes.

---

## ⚠️ Pitfalls & Anti‑Patterns

- Treating AI as an autocomplete engine rather than a collaborator.
- Vague prompts with no examples or constraints.
- Skipping evaluation and relying on “looks good to me.”
- Letting prompt sprawl grow without ownership or versioning.
- Putting models in critical paths without observability.

---

## 📚 Further Reading

- AIFSD (concepts and practices): https://github.com/tembo/aifsd
- AI‑First Software Development Manifesto: https://www.tembo.io/blog/ai-first-software-development-manifesto
- Practical evals for LLM features: search for “LLM eval harness” and “golden tests”.

---

Continue to `docs/02_customizing_copilot.md` ▶️
