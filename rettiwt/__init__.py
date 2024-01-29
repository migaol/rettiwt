from typing import Type
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app startup
app = Flask(__name__)
app.config['SECRET_KEY'] = '8ee18b8148b9bfa8e8fe17a1fe332c6dcd'

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from rettiwt import routes