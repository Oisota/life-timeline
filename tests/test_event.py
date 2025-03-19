"""Test event service"""

from datetime import datetime

import pytest

from app.models import Event
from app.services.event import generate_timeline


def evt_fac(dt):  # event factory
    return Event(
        timestamp=dt.timestamp(), title="Foo", description="Foo", user=None, user_id=1
    )


@pytest.mark.parametrize(
    "events, expected",
    [
        ([], []),
        (
            [
                evt_fac(datetime(2025, 1, 2)),
            ],
            [
                {
                    "title": 2025,
                    "items": [
                        {
                            "title": 1,
                            "items": [
                                {
                                    "title": 2,
                                    "items": [
                                        evt_fac(datetime(2025, 1, 2)),
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
        ),
        (
            [
                evt_fac(datetime(2025, 1, 1)),
                evt_fac(datetime(2025, 1, 2)),
                evt_fac(datetime(2025, 1, 2)),
                evt_fac(datetime(2025, 1, 2)),
                evt_fac(datetime(2025, 2, 1)),
                evt_fac(datetime(2025, 2, 1)),
                evt_fac(datetime(2024, 3, 1)),
                evt_fac(datetime(2024, 1, 1)),
            ],
            [
                {
                    "title": 2025,
                    "items": [
                        {
                            "title": 1,
                            "items": [
                                {
                                    "title": 1,
                                    "items": [
                                        evt_fac(datetime(2025, 1, 1)),
                                    ],
                                },
                                {
                                    "title": 2,
                                    "items": [
                                        evt_fac(datetime(2025, 1, 2)),
                                        evt_fac(datetime(2025, 1, 2)),
                                        evt_fac(datetime(2025, 1, 2)),
                                    ],
                                },
                            ],
                        },
                        {
                            "title": 2,
                            "items": [
                                {
                                    "title": 1,
                                    "items": [
                                        evt_fac(datetime(2025, 2, 1)),
                                        evt_fac(datetime(2025, 2, 1)),
                                    ],
                                }
                            ],
                        },
                    ],
                },
                {
                    "title": 2024,
                    "items": [
                        {
                            "title": 3,
                            "items": [
                                {
                                    "title": 1,
                                    "items": [
                                        evt_fac(datetime(2024, 3, 1)),
                                    ],
                                }
                            ],
                        },
                        {
                            "title": 1,
                            "items": [
                                {
                                    "title": 1,
                                    "items": [
                                        evt_fac(datetime(2024, 1, 1)),
                                    ],
                                }
                            ],
                        },
                    ],
                },
            ],
        ),
    ],
)
def test_generate_timeline(events, expected):
    timeline = generate_timeline(events)
    assert timeline == expected
