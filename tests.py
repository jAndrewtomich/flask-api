from datetime import datetime, timedelta
import unittest
from app import create_app, db, api
from app.models import Article
from config import Config
from flask_restful import Resource

BASE_URL = 'http://localhost:5001'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestApi(Resource):
    def get(self):
        article = db.session.query(Article).first()
        return {
            'title': article.title,
            'summary': article.summary,
            'keywords': article.keywords,
            'link': article.link
        }


class ArticleModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        api.add_resource(TestApi, '/test')


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_article(self):
        db.session.add(Article('A Testing Title', 'Here is a quick summary of the text...', 'Keywords...', 'https://news.ycombinator.com'))
        db.session.commit()
    