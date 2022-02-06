from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os, logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()
cors = CORS()
api = Api()

def create_app():
    app = Flask(__name__, static_url_path="", static_folder="frontend/build")
    env_config = os.environ.get("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    db.init_app(app)

    cors.init_app(app)
    api.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/flask_api.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Flask API Startup')

    return app