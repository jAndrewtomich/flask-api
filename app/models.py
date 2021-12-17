from app import db

class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    summary = db.Column(db.String())
    keywords = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self, title, summary, keywords, link):
        self.title = title
        self.summary = summary
        self.keywords = keywords
        self.link = link

    def __repr__(self):
        return f'<id {self.id}'