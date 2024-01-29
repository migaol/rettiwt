import os, secrets
from PIL import Image
from rettiwt import app, login_manager, bcrypt
from rettiwt.models import User
from rettiwt.settings import PFP_DEFAULT, PFP_DIMENSIONS

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def save_picture(form_picture: str) -> str:
    random_hash = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    pfp_fname = random_hash + f_ext
    pfp_path = os.path.join(app.root_path, 'static/pfps', pfp_fname)
    
    i = Image.open(form_picture)
    i.thumbnail(PFP_DIMENSIONS)
    i.save(pfp_path)
    return pfp_fname

def hash_password(password: str) -> str:
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return hashed_password