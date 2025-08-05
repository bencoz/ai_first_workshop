# Task: Fix root README.md

## Issue
The root `README.md` references incorrect directories:
- Refers to `app/` folder, but the Flask app is under `apps/flask-todo/`.
- Refers to `copilot/` for prompts and instructions, but files are under `copilot-examples/` or not present.

## Action
- Update paths in `README.md` to match the actual structure:
  - `apps/flask-todo/` for the Flask application.
  - `.github/copilot-instructions.md` and `.github/prompts/` for Copilot configuration.
- Ensure the setup instructions point to the correct directories.
