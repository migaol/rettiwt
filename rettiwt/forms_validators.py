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