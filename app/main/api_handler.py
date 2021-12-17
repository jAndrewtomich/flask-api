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

    def get(self):
        out = []
        for f in self.filelist:
            tmpth = str(Path(self.basedir / f))
            with open(tmpth, 'r') as reader:
                out.append(reader.read())
        return {
            "resultStatus": "SUCCESS",
            "text": out
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