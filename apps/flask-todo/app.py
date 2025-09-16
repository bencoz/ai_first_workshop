"""Flask Todo application (workshop version).

Enhancements added:
 - Environment-driven secret key & debug configuration
 - CSRF protection via Flask-WTF
 - Stricter model constraints (NOT NULL, defaults)
 - Input validation & flash messaging (to be wired in template)
 - POST-only mutation routes (update/delete)
 - 404 handling for missing resources
"""

from __future__ import annotations

import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    abort,
    Blueprint,
)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
try:  # Support both old dashed folder path and new package import during transition
    from .config import get_config  # type: ignore
except ImportError:  # pragma: no cover
    from apps.flask_todo.config import get_config  # type: ignore

load_dotenv()  # Load environment variables

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app() -> Flask:
    """Application factory to create Flask app.

    This pattern improves testability and configuration flexibility.
    """
    app = Flask(__name__)
    app_config = get_config()
    app.config.from_object(app_config)
    if app.config.get("SECRET_KEY") == "dev-insecure-placeholder":  # pragma: no cover
        app.logger.warning(
            "Using insecure placeholder SECRET_KEY. Set SECRET_KEY in .env for production."
        )

    # Init extensions
    db.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)

    # Error handlers ----------------------------------------------------------
    @app.errorhandler(404)
    def not_found(_e):  # pragma: no cover simple handler
        return render_template("404.html"), 404

    # CLI command for quick DB init (educational convenience)
    @app.cli.command("init-db")
    def init_db_command():  # pragma: no cover
        """Initialize database tables."""
        with app.app_context():
            db.create_all()
        click_msg = "Database initialized (tables ensured)."
        print(click_msg)

    return app

class Todo(db.Model):
    """Todo item model."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False, server_default="0")


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@main_bp.route("/add", methods=["POST"])
def add():
    """Create a new todo item with validation."""
    raw_title: str | None = request.form.get("title")
    title = (raw_title or "").strip()

    if not title:
        flash("Title cannot be empty.", "error")
        return redirect(url_for("home"))
    if len(title) > 100:
        flash("Title too long (max 100 characters).", "error")
        return redirect(url_for("home"))

    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    flash("Todo added.", "success")
    return redirect(url_for("home"))


@main_bp.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id: int):
    """Toggle completion state for a todo (POST-only)."""
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404)
    todo.complete = not todo.complete
    db.session.commit()
    flash("Todo updated.", "info")
    return redirect(url_for("home"))


@main_bp.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id: int):
    """Delete a todo (POST-only)."""
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404)
    db.session.delete(todo)
    db.session.commit()
    flash("Todo deleted.", "warning")
    return redirect(url_for("home"))

if __name__ == "__main__":  # For direct execution during workshop
    debug_env = os.getenv("FLASK_DEBUG") == "1"
    application = create_app()
    with application.app_context():
        db.create_all()
    application.run(debug=debug_env)
