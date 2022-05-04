from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


def create_app(config_name):
    # initialize flask app instance
    app = Flask(__name__)
    
    # bootstrap init
    Bootstrap(app)

    # app configs
    app.config.from_object(config_options[config_name])

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting request config
    from .request import configure_request
    configure_request(app)

    return app
