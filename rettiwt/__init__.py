from typing import Type
from flask import Flask

# app startup
app = Flask(__name__)
app.config['SECRET_KEY'] = '8ee18b8148b9bfa8e8fe17a1fe332c6dcd'

# database
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# security
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# login system
from flask_login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'light'

from rettiwt import routes