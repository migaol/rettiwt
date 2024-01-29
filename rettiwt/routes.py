from rettiwt import app
from flask import render_template, redirect, url_for, flash
from rettiwt.forms import *

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        # save details
        flash(f"Successfully created an account: {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        if '@' in form.login_identifier.data: # email
            # verify
            pass
        else: # username
            # verify
            pass
        
        if True: # valid
            flash("Successfully logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login failed: check your credentials", 'danger')
    return render_template('login.html', title='Login', form=form)