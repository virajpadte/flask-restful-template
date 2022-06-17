from flask_restful import Resource
from api.common.logger import log
import json

class Foo(Resource):
    def get(self,id):
        log.debug("request parsed for attribute {}".format(id))
        return json.dumps({"body": "Thanks for passing {}".format(id)})
    def post(self):
        pass