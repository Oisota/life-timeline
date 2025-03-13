from flask import Blueprint

from .urls import register_urls
from .cli import register_cli

bp = Blueprint('auth', __name__)

register_cli(bp)
register_urls(bp)