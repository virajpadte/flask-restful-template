from flask_restful import Resource
from api.common.logger import log
import json

class Rewards(Resource):
    def get(self,user_id):
        log.debug("request parsed for attribute {}".format(user_id))
        return {
            "food": "15",
            "travel": "3",
            "utility": "25",
            "travel": "2",
        }