from app.main import bp, api_handler, news
from app import api, db
from app import models

@bp.before_app_first_request
def get_news():
    hlList = news.extract_headlines('https://news.ycombinator.com')
    api.add_resource(api_handler.ApiHandler, '/')
    news.generate_summaries(hlList)


@bp.route('/', defaults={"path": ""})
def server(path):
    articles = db.session.query(models.Article).all()
    return {"result": "Success" if articles is not None else "Failure",
    "data": [{'title': a.title, 'summary': a.summary, 'keywords': a.keywords, 'link': a.link} for a in articles]}