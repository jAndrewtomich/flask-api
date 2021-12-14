from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import Config
from app.main.api_handler import ApiHandler

api = Api()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="", static_folder="frontend/build")
    app.config.from_object(config_class)

    cors.init_app(app)
    api.init_app(app)

    from app.main import bp as main_bp 
    app.register_blueprint(main_bp)

    return app

api.add_resource(ApiHandler, "/flask/endpoint")