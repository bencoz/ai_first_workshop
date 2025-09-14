# Copilot Instructions for AI Agents

## 1. Project Overview
- This repository is an AI-First Software Development Workshop for junior developers.
- Main app: Flask-based to-do list (Python 3.10+), using SQLAlchemy ORM and SQLite.
- Focus: AI-first workflows, prompt engineering, and Copilot customization.
- Includes workshop modules, prompt files, and Copilot instruction examples.

## 2. Project Structure
- `apps/flask-todo/`: Main Flask app (entry: `app.py`, DB init: `init_db.py`, template: `templates/base.html`)
- `requirements.txt`: Python dependencies
- `docs/`: Workshop modules and guides
- `copilot-examples/`: Example Copilot instructions and prompts
- `.github/`: Place for Copilot instructions and prompt files
- `instance/`: SQLite DB storage

## 3. Dependency Management
- Install dependencies: `pip install -r requirements.txt`
- Create virtual environment: `python3 -m venv venv && source venv/bin/activate`
- Initialize DB: `cd apps/flask-todo && python init_db.py`
- Run app: `cd apps/flask-todo && flask run`

## 4. Repository-Specific Rules and Conventions
- Use Python 3.10+ features and type hints where possible
- Follow Flask best practices for routing, templates, and DB models
- Use snake_case for variables, functions, and filenames
- Organize code by feature/module (e.g., routes, models, templates)
- Store templates in `templates/` and static files in `static/` (if added)
- Use SQLAlchemy ORM for DB access; avoid raw SQL except for DB init
- Place documentation in `README.md` and `docs/` modules
- Add internal documentation and comments for onboarding
- Use semantic-ui for UI styling in templates
- Place Copilot instructions in `.github/copilot-instructions.md`
- Place prompt files in `.github/prompts/` or `copilot-examples/prompts/`
- Use `.env` for environment variables if needed

## 5. General Software-Engineering Best Practices (AI-Oriented)
- Break features into small, discrete tasks and PRs
- Always create a high-level design or plan before coding
- Write meaningful documentation and inline comments for new code
- Include automated tests and sample data for new features
- Follow clear, descriptive commit-message conventions
- Keep PRs small, focused, and well-described
- Encourage code reviews and continuous integration
- Use error-handling and logging best practices
- Refactor recurring helpers into shared utilities
- Maintain consistent naming and import patterns
- Document new modules and update `README.md` as needed
- Use prompt files to guide AI agents for feature work
- Validate all changes with manual and automated tests

