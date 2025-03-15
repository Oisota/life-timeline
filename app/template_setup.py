"""Custom jinja template filters and context processors"""

from datetime import datetime
import calendar

def template_setup(app):
    app.add_template_filter(date_format)
    app.add_template_filter(month_name)

def date_format(s, fmt_string='%B %d, %Y'):
    """Format timestamp to readable date"""
    ts = int(s)
    dt = datetime.fromtimestamp(ts)
    return dt.strftime(fmt_string)

def month_name(month_num: int) -> str:
    return calendar.month_name[month_num]