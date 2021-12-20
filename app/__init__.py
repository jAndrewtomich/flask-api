from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()
cors = CORS()
api = Api()

def create_app():
    app = Flask(__name__, static_url_path="", static_folder="frontend/build")
    env_config = os.environ.get("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    cors.init_app(app)
    api.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
