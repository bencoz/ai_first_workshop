# Task: Create Automated Tests for Flask Todo App

## Issue
The Flask to-do app has no automated tests. Workshop modules reference writing tests to validate new features and demonstrate continuous integration.

## Action
- Add a `tests/` directory under `apps/flask-todo/`.
- Create sample tests using `pytest`, e.g., `tests/test_app.py`:
  - Test that the home page loads
  - Test adding a todo item via the test client
  - Test toggling completion state
  - Test deleting a todo item
- Update `requirements.txt` to include `pytest` and `pytest-flask`.
- Add a `conftest.py` to configure the Flask app for testing.
