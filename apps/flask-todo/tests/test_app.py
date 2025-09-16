import pytest

from apps.flask_todo.app import create_app, db, Todo


@pytest.fixture()
def app():
    app = create_app()
    # Override config for tests
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


def test_home_empty_list(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Todo List" in resp.data  # baseline content from template


def test_add_validation_rejects_blank(client):
    resp = client.post("/add", data={"title": "   "}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Title is required" in resp.data


def test_add_and_list(client):
    resp = client.post("/add", data={"title": "Test Item"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Test Item" in resp.data


def test_update_toggle(client, app):
    # Create seed item
    with app.app_context():
        item = Todo(title="Seed", complete=False)
        db.session.add(item)
        db.session.commit()
        tid = item.id
    # Toggle
    resp = client.post(f"/update/{tid}", follow_redirects=True)
    assert resp.status_code == 200
    # Confirm toggled
    with app.app_context():
        updated = db.session.get(Todo, tid)
        assert updated.complete is True


def test_delete(client, app):
    with app.app_context():
        item = Todo(title="To Delete", complete=False)
        db.session.add(item)
        db.session.commit()
        tid = item.id
    resp = client.post(f"/delete/{tid}", follow_redirects=True)
    assert resp.status_code == 200
    with app.app_context():
        gone = db.session.get(Todo, tid)
        assert gone is None


def test_404(client):
    resp = client.get("/does-not-exist")
    assert resp.status_code == 404
    assert b"Not Found" in resp.data


def test_model_defaults(app):
    with app.app_context():
        item = Todo(title="Default Test")
        db.session.add(item)
        db.session.commit()
        assert item.complete is False
        assert len(item.title) <= 100
