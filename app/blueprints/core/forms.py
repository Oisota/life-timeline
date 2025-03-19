from flask_wtf import FlaskForm
from wtforms import DateField, StringField, TextAreaField, validators


class EventForm(FlaskForm):
    date = DateField("Date", [validators.InputRequired()])
    title = StringField("Title", [validators.InputRequired()])
    description = TextAreaField(
        "Description", [validators.InputRequired()], render_kw={"rows": 3}
    )
