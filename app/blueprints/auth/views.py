from flask import abort, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user

from app.services.user import add_user, validate_credentials
from app.util import render, url_has_allowed_host_and_scheme

from .forms import LoginForm, RegisterForm


def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = validate_credentials(form.data["email"], form.data["password"])
        if user:
            login_user(user)
            flash("Logged in successfully")

            next_url = request.args.get("next")
            if not url_has_allowed_host_and_scheme(next_url, request.host):
                return abort(400)
            return redirect(next_url or url_for("core.home"))
        else:
            flash("Email or Password is inccorrect.")

    return render("auth/login.html", {"title": "Login", "form": form})


def register():
    form = RegisterForm()

    if form.validate_on_submit():
        add_user(form.data["email"], form.data["password"])
        flash("Account created, you may now log in.")
        return redirect(url_for("auth.login"))

    return render(
        "auth/register.html",
        {
            "title": "Register",
            "form": form,
        },
    )


@login_required
def logout():
    logout_user()
    return redirect(url_for("core.home"))
