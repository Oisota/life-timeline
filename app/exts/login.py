import flask_login

from app.services.user import get_user

login_manager = flask_login.LoginManager()

login_manager.login_view = "auth.login"


@login_manager.user_loader
def user_loader(user_id):
    """Load user from DB"""
    return get_user(user_id)
