"""Event Service"""

from datetime import datetime
from itertools import groupby
from typing import List

from app.exts.sqla import db
from app.models import Event, User


def get_all_events(user: User) -> List[Event]:
    stmt = (
        db.select(Event)
        .where(Event.user_id == user.id)
        .order_by(Event.timestamp.desc())
    )
    events = db.session.execute(stmt).scalars()
    return list(events)


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
    groupers = [
        lambda e: datetime.fromtimestamp(e.timestamp).year,
        lambda e: datetime.fromtimestamp(e.timestamp).month,
        lambda e: datetime.fromtimestamp(e.timestamp).day,
    ]
    return _group(events, groupers)


def _group(items: list, groupers: list):
    """
    Recursively group items from events list into a nested list structure

    items: list - list of items to be grouped
    groupers: list - list of functions to be passed as key funcs to groupby,
        The length of the list determines how deep the tree will nest

    Returns
    """
    results = []
    for x, xg in groupby(items, groupers[0]):
        if len(groupers) == 1:
            results.append({"title": x, "items": list(xg)})
        else:
            results.append({"title": x, "items": _group(xg, groupers[1:])})

    return results
