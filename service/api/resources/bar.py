from flask_restful import Resource
from flask import request

secure_token_dict = {
    "secure_token" : "this_is_a_secret_value"
}
class Bar(Resource):
    def get(self,token):
        if secure_token_dict.get(token):
            return secure_token_dict
        else:
            return {
                "Error" : "Secure Token invalid"
            }