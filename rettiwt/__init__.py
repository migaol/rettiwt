from typing import Type
from flask import Flask
from rettiwt.config import Config, ConfigDebug

CONFIG = ConfigDebug

app = Flask(__name__)
app.config.from_object(Config)
app.debug = CONFIG.DEBUG

from rettiwt import routes