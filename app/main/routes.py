from app.main import bp, api_handler, news_handler
from app import api, db
from app import models

@bp.before_app_first_request
def get_news():
    hlList = news_handler.extract_headlines(['https://news.ycombinator.com', 'https://news.ycombinator.com/news?p=2', 'https://news.ycombinator.com/news?p=3', 'https://news.ycombinator.com/news?p=4', 'https://news.ycombinator.com/news?p=5'])
    api.add_resource(api_handler.ApiHandler, '/')
    news_handler.generate_summaries(hlList)


@bp.route('/', defaults={"path": ""})
def server(path):
    articles = db.session.query(models.Article).all()
    return {"result": "Success" if articles is not None else "Failure",
    "data": [{'title': a.title, 'summary': a.summary, 'keywords': a.keywords, 'link': a.link} for a in articles]}