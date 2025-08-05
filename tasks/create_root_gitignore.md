# Task: Create Root .gitignore

## Issue
There is no `.gitignore` at the root of the repository. Without this, files like virtual environments, build artifacts, and IDE settings may be accidentally committed.

## Action
- Add a `.gitignore` file at the root with standard Python exclusions:
  - `venv/`, `.venv/`, `__pycache__/`, `*.py[cod]`, `.env`, etc.
- Reference components from the existing `apps/flask-todo/.gitignore` and adjust for root-level project files.
