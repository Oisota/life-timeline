"""Admin dashboard"""

from flask import redirect, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app.models import (
    Event,
    User,
)

from .sqla import db

admin = Admin(name="Derek Blog", template_mode="bootstrap4")


class AdminView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login", next=request.url))


admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Event, db.session))
