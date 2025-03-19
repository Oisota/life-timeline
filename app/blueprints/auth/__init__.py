from flask import Blueprint

from .cli import register_cli
from .urls import register_urls

bp = Blueprint("auth", __name__)

register_cli(bp)
register_urls(bp)
