from flask import Flask
from config import config_options


def create_app(config_name):
    """
    Initializing the app

    Function that takes configuration setting key as an argument
    Args:
        config_name: name of the configuration used
    """
    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting up the request configurations
    from .request import configure_request
    configure_request(app)

    return app
