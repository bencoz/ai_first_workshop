# Task: Add `.env.example` File

## Issue
A `.env` file exists with environment variable settings, but there's no `.env.example` template for new developers.

## Action
- Create a `.env.example` at the project root.
- Include sample variables:
  ```
  FLASK_APP=app.py
  FLASK_ENV=development
  ```
- Update documentation to instruct users to copy `.env.example` to `.env`.
