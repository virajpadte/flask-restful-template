class BaseConfig():
    API_PREFIX = '/api'
    SECURE_API_PREFIX = '/api/secure'
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True

class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True

class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'


