from typing import Type
from flask import Flask
from rettiwt.config import Config, ConfigDebug

def create_app(config: Type = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = config.DEBUG

    return app