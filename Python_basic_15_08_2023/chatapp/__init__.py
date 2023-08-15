"""
Application basic configuration module.
"""
from flask import Flask

from .events import socketio
from .routes import main

def create_app():
    """
    method perform the basic configuration for the application.

    Parameters:
    ----------
    None

    Return:
    ------
    app    
        return the app object.
    """
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"
    app.register_blueprint(main)
    socketio.init_app(app)
    return app
