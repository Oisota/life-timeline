"""Event Service"""

from typing import List
from datetime import datetime
from collections import defaultdict
from itertools import groupby

from app.exts.sqla import db
from app.models import Event, User

def get_all_events(user: User) -> List[Event]:
    stmt = db.select(Event) \
        .where(Event.user_id == user.id) \
        .order_by(Event.timestamp.desc())
    events = db.session.execute(stmt).scalars()
    return list(events)

def date_info(event):
    dt = datetime.fromtimestamp(event.timestamp)
    return dt.year, dt.month, dt.day

def generate_timeline(events: List[Event]) -> List:
    """Generate tree timeline from event list

    Params
    ------
    events : List[Event]
        The list of events to generate the timeline from. This list is assumed
        to be sorted already. Otherwise the timeline will not generate properly.
    
    Given a list of events, we return a tree like this:
    [
        {
            'title': '2025',
            'items': [
                {
                    'title': 'January',
                    'items': [
                        {
                            'title': '14',
                            'items': [events]
                        }
                    ]
                }
            ]
        }
    ]
    """
    if not events:
        return []

    by_year = lambda e: date_info(e)[0]
    by_month = lambda e: date_info(e)[1]
    by_day = lambda e: date_info(e)[2]

    # I feel like this could be a recursive function somehow, idk
    year_items = []
    year_groups = groupby(events, by_year)
    for year, year_group in year_groups:
        month_items = []
        month_groups = groupby(year_group, by_month)
        for month, month_group in month_groups:
            day_items = []
            day_groups = groupby(month_group, by_day)
            for day, day_group in day_groups:
                day_items.append({
                    'title': day,
                    'items': list(day_group)
                })
            
            month_items.append({
                'title': month,
                'items': day_items,
            })

        year_items.append({
            'title': year,
            'items': month_items,
        })

    return year_items