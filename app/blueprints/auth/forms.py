from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, ValidationError


class LoginForm(FlaskForm):
    email = EmailField("Email")
    password = PasswordField("Password")


class RegisterForm(LoginForm):
    confirm_password = PasswordField("Confirm Password")

    def validate_confirm_password(self, field):
        if field.data != self.password.data:
            raise ValidationError("Passwords do not match, please re-enter")
