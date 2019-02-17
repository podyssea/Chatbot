import pytest
from app import create_app
from flask_sqlalchemy import SQLAlchemy

# https://github.com/pallets/flask/blob/1.0.2/examples/tutorial/tests/conftest.py
# https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
# https://realpython.com/python-web-applications-with-flask-part-iii/#unit-vs-integration-tests


@pytest.fixture(scope='module')
def app():
    db = SQLAlchemy()
    app = create_app()
    with app.app_context():
        db.init_app(app)
    yield app


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()
