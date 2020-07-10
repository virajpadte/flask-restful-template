from flask import Flask
from flask_restful import Api
from api.resources.foo import Foo
from api.resources.bar import Bar
import config

api = Api(prefix=config.API_PREFIX)

api.add_resource(Foo, '/Foo', '/Foo/<string:id>')
api.add_resource(Bar, '/Bar', '/Bar/<string:id>')