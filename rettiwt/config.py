import os

class Config:
    DEBUG=False

    # create an environ variable: export FLASK_SECRET_KEY=<key>
    # or just set it to anything
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

class ConfigDebug:
    DEBUG=True
    SECRET_KEY = '8ee18b8148b9bfa8e8fe17a1fe332c6dcd'