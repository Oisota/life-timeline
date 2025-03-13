import logging
from datetime import datetime

from flask import redirect, url_for
from flask_login import login_required, current_user

from app.util import render
from app.models import Event
from app.exts.sqla import db
from .forms import EventForm
#from app.services.event import generate_timeline

log = logging.getLogger(__name__)

@login_required
def home():
    stmt = db.select(Event) \
        .where(Event.user_id == current_user.id) \
        .order_by(Event.timestamp.desc())
    events = db.session.execute(stmt).scalars()
    events = list(events)
    #tree = generate_timeline(events)
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
            user_id=current_user.id, # TODO mess with model to figure out how to only need user or user_id arg
            user=current_user,
        )
        db.session.add(evt)
        db.session.commit()

        return redirect(url_for('core.home'))
    return render('core/index.html', {
        'title': 'Home',
        'events': events,
        #'tree': tree,
        'form': form,
    })