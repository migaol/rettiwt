from flask_login import current_user
from rettiwt.models import User
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError

class ValidChars:
    def __init__(self, message: str = None):
        self.message = message

    def __call__(self, form: FlaskForm, field: StringField):
        invalid_chars = set(field.data) - set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
        if invalid_chars:
            message = self.message or f"Field can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_)."
            raise ValidationError(message)
        
class UniqueUsername:
    def __init__(self, message: str = None):
        self.message = message

    def __call__(self, form: FlaskForm, field: StringField):
        if current_user.is_authenticated and field.data == current_user.username: return
        user = User.query.filter_by(username=field.data).first()
        if user:
            message = self.message or f"Username is taken"
            raise ValidationError(message)

class UniqueEmail:
    def __init__(self, message: str = None):
        self.message = message
    
    def __call__(self, form: FlaskForm, field: StringField):
        if current_user.is_authenticated and field.data == current_user.email: return
        user = User.query.filter_by(email=field.data).first()
        if user:
            message = self.message or f"Email is already in use"
            raise ValidationError(message)