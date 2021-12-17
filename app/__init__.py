from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import Config
import os
from app.main.api_handler import ApiHandler

api = Api()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="", static_folder="frontend/build")
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

    cors.init_app(app)
    api.init_app(app)

    from app.main import bp as main_bp 
    app.register_blueprint(main_bp)

    return app

api.add_resource(ApiHandler, "/flask/endpoint")