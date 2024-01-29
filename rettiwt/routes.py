from rettiwt import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from rettiwt.forms import *
from rettiwt.models import User, Post
from rettiwt.utils import *

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('home'))

    form = FormRegister()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=User.hash_password(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('home'))

    form = FormLogin()
    if form.validate_on_submit():
        if '@' in form.login_identifier.data: # email
            user = User.query.filter_by(email=form.login_identifier.data).first()
        else: # username
            user = User.query.filter_by(username=form.login_identifier.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data): # valid
            login_user(user)
            flash("Successfully logged in", 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login failed: check your credentials", 'danger')
    return render_template('login.html', title='Login', form=form)