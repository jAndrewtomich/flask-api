from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from config import DevelopmentConfig

db = SQLAlchemy()
api = Api()
cors = CORS()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_url_path="", static_folder="frontend/build")
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    cors.init_app(app)
    api.init_app(app)

    from app.main import bp as main_bp 
    app.register_blueprint(main_bp)

    from app.main import news_h, api_h

    return app

from app import models 
