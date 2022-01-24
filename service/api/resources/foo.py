from flask_restful import Resource

standard_token_dict = {
    "standard_token" : "this_is_a_standard_value"
}

class Foo(Resource):
    def get(self,token):
        if standard_token_dict.get(token):
            return standard_token_dict
        else:
            return {
                "Error" : "Standard Token invalid"
            }