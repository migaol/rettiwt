from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from rettiwt.forms_validators import ValidChars, UniqueUsername, UniqueEmail

class FormRegister(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=16), ValidChars()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class FormLogin(FlaskForm):
    login_identifier = StringField('Email or Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class FormChangeCredentials(FlaskForm):
    username = StringField('Username',
                                validators=[DataRequired(), Length(min=3, max=16), ValidChars(), UniqueUsername()])
    email = StringField('Email', validators=[DataRequired(), Email(), UniqueEmail()])
    pfp = FileField('Change Profile Picture', validators=[FileAllowed(['jpg', 'png', 'svg'])])
    submit = SubmitField('Save Changes')

class FormPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class FormEditPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save Changes')