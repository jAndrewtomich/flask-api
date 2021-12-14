from flask_restful import Resource, reqparse
from pathlib import Path
import os


class ApiHandler(Resource):
    def __init__(self):
        self.basedir = Path("/home/at/Coding/py/text_summarizer/output")
        self.filelist = os.listdir(self.basedir)

    def __str__(self):
        return "ApiHandler -=- basedir: {}".format(str(self.basedir))

    def __repr__(self):
        return self.__str__()

    def get(self, idx=1):
        tmpth = str(Path(self.basedir / self.filelist[idx]))
        print(tmpth)
        with open(tmpth, 'r') as reader:
            out = reader.read()
            print(out)
        return {
            "resultStatus": "SUCCESS",
            "data": out
        }

    def post(self, idx=0):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument("type", type=str)
        parser.add_argument("data", type=str)

        args = parser.parse_args()

        print(args)

        request_type = args["type"]
        request_json = args["data"]

        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            text = ret_msg
        else:
            text = "Not available"

        result = {"status": "Success", "text": text}

        return result