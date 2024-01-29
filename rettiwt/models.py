from rettiwt import db
from rettiwt.settings import PFP_DEFAULT
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(69), unique=True, nullable=False)
    password = db.Column(db.String(69), nullable=False)
    profile_picture_file = db.Column(db.String(20), nullable=False, default=PFP_DEFAULT)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}'), '{self.email}', '{self.profile_picture_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)