from flask import Blueprint

from .urls import register_urls
from .cli import register_cli

bp = Blueprint("core", __name__)

register_cli(bp)
register_urls(bp)
