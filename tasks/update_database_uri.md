# Task: Update Database URI in `app.py`

## Issue
The SQLALCHEMY_DATABASE_URI in `apps/flask-todo/app.py` is set to `'sqlite:///db.sqlite'`, which creates the database file in the project root rather than the `instance/` folder. Workshop instructions expect the use of `instance/db.sqlite`.

## Action
- Change `app.config['SQLALCHEMY_DATABASE_URI']` to `sqlite:///instance/db.sqlite`.
- Ensure the `instance/` folder is configured as Flask instance path if needed.
