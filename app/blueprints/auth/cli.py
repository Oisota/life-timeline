"""Auth CLI commands"""

import click

from app.services.user import add_user


def register_cli(bp):
    bp.cli.command("add-user")(add_user_cmd)


@click.argument("email")
@click.argument("password")
def add_user_cmd(email, password):
    """CLI command for adding user to the DB"""
    add_user(email, password)
