# Task: Update `apps/flask-todo/README.md`

## Issue
The Flask app README:
- Installs Flask and Flask-SQLAlchemy individually but doesn’t mention `python-dotenv` or the root `requirements.txt`.
- Suggests manual `export` commands but app uses `python-dotenv` via `.env` file.
- Does not reference the project-level `.env` or `.env.example`.

## Action
- Update installation to use `pip install -r requirements.txt`.
- Add `python-dotenv` to requirements if missing.
- Update instructions to load `.env` automatically and mention `.env.example`.
- Simplify environment variable setup (inform users to copy `.env.example` to `.env`).
