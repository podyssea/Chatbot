from flask import Blueprint

bp = Blueprint('main', __name__)

# noinspection PyPep8
from app.main import routes
