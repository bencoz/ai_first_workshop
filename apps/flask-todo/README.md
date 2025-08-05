# Simple Flask Todo App using SQLAlchemy and SQLite database.

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup
- Create and activate a virtual environment in project root:
  ```console
  python3 -m venv venv
  source venv/bin/activate
  ```

- Install all dependencies:
  ```console
  pip install -r requirements.txt
  ```

- Copy environment template and configure:
  ```console
  cp .env.example .env
  ```

- Initialize the database:
  ```console
  cd apps/flask-todo
  python init_db.py
  ```

- Run the app:
  ```console
  flask run
  ```

This app automatically loads configuration from `.env` via `python-dotenv`. Ensure `.env` exists in the project root.
