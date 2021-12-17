from flask import Blueprint

bp = Blueprint("main", __name__)

from app.main import routes, api_handler, news_handler

api_h = api_handler.ApiHandler()
news_h = news_handler.NewsHandler()