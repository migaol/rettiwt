from rettiwt import app, db, bcrypt
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(69), unique=True, nullable=False)
    password = db.Column(db.String(69), nullable=False)
    profile_picture_file = db.Column(db.String(69), nullable=False, default='default_pfp.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def hash_password(password: str) -> str:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return hashed_password

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)