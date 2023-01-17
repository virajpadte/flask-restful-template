from flask import Flask
from flask_restful import Api
from api.resources.rewards import Rewards
import config

api = Api(prefix=config.API_PREFIX)

api.add_resource(Rewards, '/rewards', '/rewards/<string:user_id>')