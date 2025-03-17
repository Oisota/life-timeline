from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, ValidationError

class LoginForm(FlaskForm):
    email = EmailField()
    password = PasswordField()

class RegisterForm(FlaskForm):
    email = EmailField()
    password = PasswordField()
    confirm_password = PasswordField()

    def validate_confirm_password(self, field):
        if field.data != self.password.data:
            raise ValidationError('Passwords do not match, please re-enter')