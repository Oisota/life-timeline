import logging
from datetime import datetime

from flask import redirect, url_for
from flask_login import current_user, login_required

from app.exts.sqla import db
from app.models import Event
from app.services.event import generate_timeline, get_all_events
from app.util import render

from .forms import EventForm

log = logging.getLogger(__name__)


@login_required
def home():
    events = get_all_events(current_user)
    years = generate_timeline(events)
    form = EventForm()

    if form.validate_on_submit():
        event_dt = datetime(
            year=form.date.data.year,
            month=form.date.data.month,
            day=form.date.data.day,
        )
        evt = Event(
            timestamp=event_dt.timestamp(),
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id,  # TODO mess with model to figure out how to only need user or user_id arg
            user=current_user,
        )
        db.session.add(evt)
        db.session.commit()

        return redirect(url_for("core.home"))
    return render(
        "core/index.html",
        {
            "title": "Home",
            "years": years,
            "form": form,
        },
    )
