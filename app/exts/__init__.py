
from .login import login_manager
from .sqla import db
from .csrf import csrf
from .admin import admin

def register_extensions(app):
    login_manager.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    # TODO look for rss feed extension