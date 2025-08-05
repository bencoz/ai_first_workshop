# Task: Refactor Flask App to Application Factory Pattern

## Issue
Tests for the Flask todo app are failing because the current `app.py` uses a global `Flask` instance and SQLAlchemy engine is bound at module import time to the default database URI. Tests override configuration after initialization, but the engine remains bound to the original database file path, causing sqlite errors.

## Action
- Refactor `apps/flask-todo/app.py` to:
  - Remove the global `app` instance and use a `create_app()` factory that:
    - Creates a `Flask` app
    - Configures the database URI from `app.config` before binding SQLAlchemy
    - Initializes extensions (`db.init_app(app)`)
    - Registers routes via a blueprint
  - Define routes using a blueprint (e.g., `bp = Blueprint('main', __name__)`) instead of `@app.route`
  - Ensure `create_app()` returns a fully configured app without binding engine until init_app
  - Update the CLI entry point for running the app to use `create_app()`

This will allow tests to override `app.config['SQLALCHEMY_DATABASE_URI']` before calling `db.init_app()`, ensuring the in-memory database is used during tests.
