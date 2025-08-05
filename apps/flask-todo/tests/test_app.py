import os
import sys
import pytest

"""
Test suite for Flask Todo App using in-memory SQLite database.
"""
# Ensure app module path to import create_app factory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app, db


@pytest.fixture
def client():
    # Use in-memory SQLite for tests via environment variable
    os.environ['DB_PATH'] = 'sqlite:///:memory:'
    app = create_app()
    app.config['TESTING'] = True
    # Initialize database schema
    with app.app_context():
        db.create_all()
    # Provide test client
    with app.test_client() as client:
        yield client



def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_add_todo(client):
    response = client.post('/add', data={'title': 'Test Todo'}, follow_redirects=True)
    assert b'Test Todo' in response.data


def test_toggle_todo(client):
    client.post('/add', data={'title': 'Toggle Todo'}, follow_redirects=True)
    response = client.get('/update/1', follow_redirects=True)
    assert b'Completed' in response.data


def test_delete_todo(client):
    client.post('/add', data={'title': 'Delete Todo'}, follow_redirects=True)
    response = client.get('/delete/1', follow_redirects=True)
    assert b'Delete Todo' not in response.data
