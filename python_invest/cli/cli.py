from pathlib import Path

import typer

from python_invest.cli.commands import config_handler, crypto_commands

cli = typer.Typer(name='python-invest')

cli.add_typer(crypto_commands, name='crypto')


@cli.command('config', help='Configure the CLI application.')
def config(
    email: str = typer.Option(None, help='The email of the API user.'),
    config_file: Path = typer.Option(
        None, help='The path to the config file.'
    ),
):
    """
    Configure the CLI application.

    Args:
        - email: The email of the API user.
        - config_file: The path to the config file.

    Returns:
        - config_status: The status of the config application.
    """
    return config_handler(email, config_file)
