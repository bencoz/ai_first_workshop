# Task: Improve `.env` Usage in `app.py`

## Issue
`app.py` loads environment variables but the code does not reference any from `.env`. It should load the Flask settings like `FLASK_APP` and `FLASK_ENV` or custom variables like `DATABASE_URI`.

## Action
- Modify `app.py` to read `DATABASE_URI` from environment (e.g., `os.getenv('DATABASE_URI')`) with fallback.
- Update `.env.example` and `.env` to include `DATABASE_URI=sqlite:///instance/db.sqlite`.
- Remove hardcoded URI or prefer environment variable for production flexibility.
