import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    server = Flask(__name__)
    server.config.from_object(config_class)

    with server.app_context():
        db.init_app(server)
        migrate.init_app(server, db)

    from app.main import bp as main_bp
    server.register_blueprint(main_bp)

    if not server.debug and not server.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/server.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s '
                                                    '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        server.logger.addHandler(file_handler)

        server.logger.setLevel(logging.INFO)
        server.logger.info('Webhook Server startup')

    return server


# noinspection PyPep8
from app import models
