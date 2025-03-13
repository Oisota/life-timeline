"""Custom jinja template filters and context processors"""

from datetime import datetime

def template_setup(app):
    app.add_template_filter(date_format)

def date_format(s, fmt_string='%B %d, %Y'):
    """Format timestamp to readable date"""
    ts = int(s)
    dt = datetime.fromtimestamp(ts)
    return dt.strftime(fmt_string)