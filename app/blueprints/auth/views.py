from flask import redirect, url_for, flash, request, abort, redirect
from flask_login import login_user, logout_user, login_required

from app.util import render, url_has_allowed_host_and_scheme
from app.services.user import validate_credentials
from .forms import LoginForm

def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = validate_credentials(form.data['email'], form.data['password'])
        if user:
            login_user(user)
            flash('Logged in successfully')

            next_url = request.args.get('next')
            if not url_has_allowed_host_and_scheme(next_url, request.host):
                return abort(400)
            return redirect(next_url or url_for('core.home'))
        else:
            flash('Email or Password is inccorrect.')

    return render('auth/login.html', {
        'title': 'Login',
        'form': form
    })

@login_required
def logout():
    logout_user()
    return redirect(url_for('core.home'))