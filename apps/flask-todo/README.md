# Flask Todo App

A simple Flask to-do application using SQLAlchemy ORM and SQLite database, styled with Semantic UI.

## Features

- Add, complete, and delete tasks
- Persistent storage with SQLite database
- Clean, responsive UI with Semantic UI

## Quick Start

### From Repository Root

If you're following the workshop, the app setup is included in the main [SETUP_GUIDE.md](../../SETUP_GUIDE.md).

Quick steps:
```bash
# From repository root
cd apps/flask-todo

# Initialize database
python init_db.py

# Run the app
flask run  # or: python app.py
```

Open `http://127.0.0.1:5000`

### Standalone Setup

If setting up this app independently:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install Flask Flask-SQLAlchemy

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Initialize and run
python init_db.py
flask run
```

## Project Structure

```
.
├── app.py              # Flask application, models, routes
├── init_db.py          # Database initialization script
├── db.sqlite           # SQLite database (created on first run)
├── templates/
│   └── base.html       # HTML template with Semantic UI
├── static/             # (Optional) CSS/JavaScript assets
└── instance/           # (Optional) Database storage location
```

## Architecture

### Database Model

**Todo Model:**
- `id` (Integer, Primary Key) — Unique identifier
- `title` (String, 100 chars) — Task description
- `complete` (Boolean) — Completion status

### Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Display all tasks |
| `/add` | POST | Create a new task |
| `/update/<id>` | GET | Toggle task completion |
| `/delete/<id>` | GET | Delete a task |

## Configuration

Default SQLite configuration in `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

To use a custom database location, update the URI before initializing.

## Development

### Enable Debug Mode

```bash
export FLASK_ENV=development  # Auto-reloads on code changes
```

### Reset Database

```bash
rm db.sqlite
python init_db.py
```

### Sample Data

To populate sample data, edit `init_db.py` and add tasks before running it:

```python
# In init_db.py, after db.create_all()
db.session.add(Todo(title="Buy groceries", complete=False))
db.session.add(Todo(title="Write documentation", complete=False))
db.session.commit()
```

## Styling

This app uses **Semantic UI** for styling. Update `templates/base.html` to customize the appearance.

Semantic UI CDN is included in the template. See [Semantic UI Documentation](https://semantic-ui.com/) for available components.

## Dependencies

- **Flask** — Web framework
- **Flask-SQLAlchemy** — ORM for database operations
- **Semantic UI** — CSS framework (via CDN)

See main repository `requirements.txt` for exact versions.

## Troubleshooting

**Database locked error?**
```bash
rm db.sqlite
python init_db.py
```

**Port 5000 already in use?**
```bash
flask run --port 5001
```

**ModuleNotFoundError?**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r ../../requirements.txt
```

## Learning Resources

- [Flask Official Guide](https://flask.palletsprojects.com)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org)
- [Semantic UI Framework](https://semantic-ui.com)

## Workshop Context

This app is used in the AI-First Workshop (Modules 3–5) to practice:
- Reading and understanding existing code with Copilot
- Adding features using AI-assisted development
- Writing tests and documentation
- Using prompt engineering for implementation planning

See the main `README.md` and workshop modules for more details.
