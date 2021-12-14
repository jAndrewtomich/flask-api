from flask import Flask, request, current_app, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from main.api_handler import ApiHandler
from config import Config

api = Api()


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="", static_folder="frontend/build")
    app.config.from_object(config_class)

    api.init_app(app)

    from app.main import bp as main_bp 
    app.register_blueprint(main_bp)