import os
from rettiwt import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, abort, request
from flask_login import current_user, login_user, logout_user, login_required
from rettiwt.forms import *
from rettiwt.models import User, Post
from rettiwt.utils import *

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('home.html', posts=posts)

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

@app.route('/logout')
def logout():
    logout_user()
    flash("Successfully logged out", 'success')
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = FormChangeCredentials()
    if form.validate_on_submit():
        if current_user.profile_picture_file != PFP_DEFAULT: # delete old pfp from system
            old_picture_path = os.path.join(app.root_path, 'static/pfps', current_user.profile_picture_file)
            if os.path.exists(old_picture_path): os.remove(old_picture_path)
            picture_file = save_picture(form.pfp.data)
            current_user.profile_picture_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        # TODO: password confirm
        db.session.commit()
        flash("Account details updated", 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_picture_file = url_for('static', filename=f'pfps/{current_user.profile_picture_file}')
    return render_template('profile.html', title='Profile', image_file=profile_picture_file, form=form)

@app.route('/newpost', methods=['GET', 'POST'])
@login_required
def newpost():
    form = FormPost()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post created", 'success')
        return redirect(url_for('home'))
    return render_template('newpost.html', title='New Post', form=form, legend='New Post')

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delpost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user: abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post successfully deleted", 'success')
    return redirect(url_for('home'))

@app.route('/post/<int:post_id>')
def postpage(post_id: int):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route('/posts/<string:username>')
def userposts(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date.desc()).all()
    return render_template('userposts.html', posts=posts, user=user)