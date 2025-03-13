from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField

class LoginForm(FlaskForm):
    email = EmailField()
    password = PasswordField()