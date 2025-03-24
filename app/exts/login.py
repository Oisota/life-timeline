import flask_login

from app.exts.sqla import db
from app.models import User

login_manager = flask_login.LoginManager()

login_manager.login_view = "auth.login"


@login_manager.user_loader
def user_loader(user_id):
    """Load user from DB"""
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()
