from flask import Flask
from flask_restful import Api
from api.resources.foo import Foo
from api.resources.bar import Bar
from api.resources.health import Health
import config

api_standard = Api(prefix=config.API_PREFIX)
api_mtls = Api(prefix=config.SECURE_API_PREFIX)

api_standard.add_resource(Foo, '/foo', '/foo/<string:token>')
api_standard.add_resource(Health, '/health')
api_mtls.add_resource(Bar, '/bar', '/bar/<string:token>')