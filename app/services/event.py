"""Event Service"""

from typing import List
from datetime import datetime
from collections import defaultdict

from app.exts.sqla import db
from app.models import Event, User

def get_all_events(user: User) -> List[Event]:
    stmt = db.select(Event) \
        .where(Event.user_id == user.id) \
        .order_by(Event.timestamp.desc())
    events = db.session.execute(stmt).scalars()
    return list(events)

def generate_timeline(events: List[Event]) -> dict:
    """Generate tree timeline from event list

    This assumes events is already ordered in reverse chronological order
    
    Given a list of events, we return a tree like this:
    [
        {
            'title': '2025',
            'items': [
                {
                    'title': 'January',
                    'items': [
                        {'title': '14', 'items': [events]}
                    ]
                }
            ]
        }
    ]
    Keys are year/month/day nested with the final layer being events on the day
    """
    tree = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [])))
    tree = []
    for event in events:
        dt = datetime.fromtimestamp(event.timestamp)
        year = str(dt.year)
        month = str(dt.month)
        day = str(dt.day)

        current_year = year
        while current_year == year:


        tree[year][month][day].append(event)

    return tree