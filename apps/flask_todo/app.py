"""Flask Todo application (workshop version) - packaged.

Uses application factory pattern and blueprint for improved testability.
"""
from __future__ import annotations

import os

from flask import (
    Flask,
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from dotenv import load_dotenv

from .config import get_config

load_dotenv()

# Extensions -----------------------------------------------------------------

db = SQLAlchemy()
csrf = CSRFProtect()

# Blueprint ------------------------------------------------------------------

main_bp = Blueprint("main", __name__)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False, server_default="0")


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
        return redirect(url_for("main.home"))
    if len(title) > 100:
        flash("Title too long (max 100 characters).", "error")
        return redirect(url_for("main.home"))

    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    flash("Todo added.", "success")
    return redirect(url_for("main.home"))


@main_bp.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id: int):
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404)
    todo.complete = not todo.complete
    db.session.commit()
    flash("Todo updated.", "info")
    return redirect(url_for("main.home"))


@main_bp.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id: int):
    todo = Todo.query.get(todo_id)
    if not todo:
        abort(404)
    db.session.delete(todo)
    db.session.commit()
    flash("Todo deleted.", "warning")
    return redirect(url_for("main.home"))


# Factory --------------------------------------------------------------------

def create_app() -> Flask:
    app = Flask(__name__)
    app_config = get_config()
    app.config.from_object(app_config)

    if app.config.get("SECRET_KEY") == "dev-insecure-placeholder":  # pragma: no cover
        app.logger.warning(
            "Using insecure placeholder SECRET_KEY. Set SECRET_KEY in .env for production."
        )

    db.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found(_e):  # pragma: no cover
        return render_template("404.html"), 404

    @app.cli.command("init-db")
    def init_db_command():  # pragma: no cover
        with app.app_context():
            db.create_all()
        print("Database initialized (tables ensured).")

    return app


if __name__ == "__main__":  # pragma: no cover
    debug_env = os.getenv("FLASK_DEBUG") == "1"
    application = create_app()
    with application.app_context():
        db.create_all()
    application.run(debug=debug_env)
