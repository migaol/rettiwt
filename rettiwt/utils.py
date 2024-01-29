from rettiwt import login_manager
from rettiwt.models import User, Post

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))