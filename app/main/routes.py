from app.main import bp, api_handler, news_handler
from app import api, db
from app import models

@bp.before_app_first_request
def first_get_news():
    api.add_resource(api_handler.ApiHandler, '/')
#    hlList = news_handler.extract_headlines(['https://news.ycombinator.com', 'https://news.ycombinator.com/news?p=2', 'https://news.ycombinator.com/news?p=3', 'https://news.ycombinator.com/news?p=4', 'https://news.ycombinator.com/news?p=5'])
#    news_handler.generate_summaries(hlList)
#    api.add_resource(api_handler.ApiHandler, '/')

@bp.before_app_request
def get_news():
    hlList = news_handler.extract_headlines(['https://news.ycombinator.com'])
    test_link = db.session.query(models.Article).first()
    if test_link is not None: test_link = test_link.link
    if test_link != hlList[0][0]:
        news_handler.generate_summaries(hlList)
    
@bp.route('/', defaults={"path": ""})
def server(path):
    articles = db.session.query(models.Article).all()
    return {"result": "Success" if articles is not None else "Failure",
    "data": [{'title': a.title, 'summary': a.summary, 'keywords': a.keywords, 'link': a.link} for a in articles]}
