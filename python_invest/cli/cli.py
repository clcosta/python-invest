import configparser
from pathlib import Path

import typer

from python_invest.cli.commands import config_handler, crypto_commands
from python_invest.const import BASE_PATH

cli = typer.Typer(name='python-invest')

cli.add_typer(crypto_commands, name='crypto', help='Crypto functions')


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


@cli.command('version', help='Version of Package')
def version():
    """
    Version of the Package.
    """
    try:
        configs = configparser.ConfigParser()
        configs.read(Path(BASE_PATH).parent / 'pyproject.toml')
        v = configs['tool.poetry']['version']
        print(f"""Version: {v.replace('"', '')}""")
    except Exception as er:
        raise ValueError(
            'Failure to get the CLI Version, please reinstall the package!'
        ) from er
