"""Main app package"""
from dotenv import load_dotenv

load_dotenv()

from flask import Flask

from app.blueprints import register_blueprints
from app.cli import register_cli
from app.errors import register_error_handlers
from app.exts import register_extensions
from app.template_setup import template_setup


def create_app():
    """App Factory"""
    app = Flask(__name__)
    app.config.from_prefixed_env()

    register_extensions(app)
    register_cli(app)
    register_blueprints(app)
    register_error_handlers(app)
    template_setup(app)

    return app
