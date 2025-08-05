
import os
import logging
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env
logging.basicConfig(level=logging.INFO)
db = SQLAlchemy()

# Data model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Blueprint for routes
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@bp.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.home'))

@bp.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('main.home'))

@bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.home'))

def create_app():
    """Application factory for Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    # Configure database URI from environment or default to instance folder
    db_uri = os.getenv('DB_PATH', 'sqlite:///db.sqlite')
    # Add 'sqlite:///' to db_uri if not present
    if not db_uri.startswith('sqlite:///'):
        db_uri = f"sqlite:///{db_uri}"

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Log the resolved absolute path for SQLite
    if db_uri.startswith('sqlite:///'):
        rel_path = db_uri.replace('sqlite:///', '')
        abs_path = os.path.abspath(rel_path)
        logging.info(f"[Flask] SQLite DB absolute path: {abs_path}")
    logging.info(f"[Flask] Using SQLAlchemy DB URI: {db_uri}")
    # Initialize extensions
    db.init_app(app)
    # Register blueprints
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    # Ensure db.sqlite exists in the project root
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite')
    if not os.path.exists(db_path):
        open(db_path, 'a').close()
        logging.info(f"[Flask] Created database file at: {db_path}")
    else:
        logging.info(f"[Flask] Database file exists at: {db_path}")
    try:
        with app.app_context():
            db.create_all()
            logging.info("[Flask] Database tables created.")
        app.run(debug=True)
    except Exception as e:
        logging.error(f"[Flask] Exception during startup: {e}")
