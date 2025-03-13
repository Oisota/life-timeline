from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms import validators

class EventForm(FlaskForm):
    date = DateField('Date', [validators.InputRequired()])
    title = StringField('Title', [validators.InputRequired()])
    description = TextAreaField('Description', [validators.InputRequired()])
