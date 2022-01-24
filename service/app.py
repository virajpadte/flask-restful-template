import config
from api import api_standard
from api import api_mtls
from flask import Flask
from api.common.logger import log


def create_app():
    log.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api_standard.init_app(app)
    api_mtls.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)