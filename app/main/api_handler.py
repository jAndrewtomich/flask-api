from flask_restful import Resource, reqparse
from sqlalchemy import create_engine
from app.models import Article


class ApiHandler(Resource):
    def __init__(self):
        self.conn = create_engine('sqlite:///news.db').connect()

    def __str__(self):
        return "ApiHandler -=- basedir: {}".format(str(self.basedir))

    def __repr__(self):
        return self.__str__()

    def get(self):
        with self.conn as connection:
            q = [{'title': r.title, 'summary': r.summary, 'keywords': r.keywords, 'link': r.link} for r in Article.query.all()]
            data = [{'title': p['title'], 'summary': p['summary'], 'keywords': p['keywords'], 'link': p['link']} for p in q]
        return {
            "resultStatus": "SUCCESS",
            "data": data
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        #parser.add_argument("type", type=str)
        parser.add_argument("data", type=str)
        parser.add_argument("idx", type=int)

        args = parser.parse_args()

        print(args)

        #request_type = args["type"]
        request_json = args["data", "idx"]

        #ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            text = ret_msg
        else:
            text = "Not available"

        result = {"resultStatus": "Success", "text": text}

        return result