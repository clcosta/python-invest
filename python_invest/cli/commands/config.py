import configparser
import re
from pathlib import Path

from rich.console import Console
from rich.prompt import Confirm

from python_invest.const import BASE_PATH

base_config_path = Path(BASE_PATH) / 'pinv.ini'


def load_config(
    config: configparser.ConfigParser = configparser.ConfigParser(),
    config_path: Path = base_config_path,
) -> dict:
    try:
        res = config.read(config_path)
        if not res:
            raise FileNotFoundError(config_path.resolve())
        return config['api.config']
    except FileNotFoundError as er:
        console = Console()
        console.print(
            f'[bold]Config file [red]{config_path.resolve()}[/red] not found![/bold]'
        )
        raise er


def config_handler(email: str, config_file: str | Path) -> bool:
    config = configparser.ConfigParser()
    console = Console()
    prompt = Confirm(console=console)
    config_path = Path(config_file) if config_file else base_config_path

    def input_and_store_email(email):
        email_pattern = re.compile(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        )
        while True:
            if not email:
                email = console.input('[bold]✉️ Email[/bold]: ')
            if not re.fullmatch(email_pattern, email):
                console.print('[bold][red1]Email is not valid![/][/]')
            break
        config['api.config'] = {
            'EMAIL': email,
        }
        with config_path.open('w') as configfile:
            config.write(configfile)
        console.print(
            f'[bold]Config file [green]{config_path.resolve()}[/green] created![/bold]'
        )

    if not config_path.exists():
        console.print('[bold]Config file [red]pinv.ini[/red] not found![bold]')
        answer = prompt.ask('[bold]You want create one?[/]')
        if answer:
            input_and_store_email(email)
            return True
        else:
            return False
    else:
        conf = load_config(config, config_path)
        if config_path != base_config_path:
            config.write(base_config_path.open('w'))
        email = conf['EMAIL']
        answer = prompt.ask(
            f'[bold]This is the correct email [green]{email}[/green] ?[/bold]'
        )
        if answer:
            return True
        else:
            input_and_store_email(email)
            return True
