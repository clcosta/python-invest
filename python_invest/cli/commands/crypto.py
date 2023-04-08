from datetime import datetime
from pathlib import Path

import pandas as pd
import typer
from rich.console import Console
from rich.text import Text

from python_invest import Invest
from python_invest.cli.commands.config import load_config

from .pandas_to_rich import df_to_table
from .utils import show_args as _show_args

crypto_commands = typer.Typer()


def __args_to_crypto_api(*args):
    dt_in, dt_out, symbol, name, time_frame = args
    range_dates = {'from_date': dt_in, 'to_date': dt_out}
    return {
        'symbol': symbol if symbol else None,
        **range_dates,
        'name': name if name else None,
        'time_frame': time_frame if time_frame else 'Monthly',
    }


def _load_email(email):
    try:
        conf = load_config()
    except FileNotFoundError as er:
        if not email:
            raise ValueError('[bold]Email is not set![/]')
    email = email if email else conf['EMAIL']
    return email


@crypto_commands.command('list', help='List all available crypto.')
def list_crypto(
    email: str = typer.Option(
        None, help='The email of the API user.', envvar='BASE_EMAIL'
    ),
    to_csv: Path = typer.Option(
        None,
        help='If provided, the output will be saved in a csv file.',
        is_flag=True,
        show_default=False,
    ),
):
    console = Console()
    email = _load_email(email)
    inv = Invest(email)
    data = inv.crypto.get_list()
    df = pd.DataFrame.from_records(data)
    if to_csv:
        to_csv = to_csv if to_csv != Path('.') else Path('./output.csv')
        console.print(
            f'Your file will be saved on:{" ":<5}[bold][i]{to_csv.resolve()}[/i][bold]'
        )
        df.to_csv(to_csv, index=False)
        return
    success_text = Text(
        '\nTABLE OF LIST OF ALL CRYPTOS AVAILABLE\n', style='#dcbdfb'
    )
    table = df_to_table(df)
    console.print(success_text, table, justify='center')


@crypto_commands.command(
    'historical',
    help='Use the Invest Class Crypto API to get historical data.',
)
def historical_data(
    symbol: str = typer.Argument(
        ...,
        help='The symbol of the crypto.',
    ),
    name: str = typer.Argument(
        None,
        help='The name of the crypto.',
    ),
    time_frame: str = typer.Argument(
        'Monthly',
        help='The time frame of the historical data.',
        autocompletion=lambda: ['Daily', 'Weekly', 'Monthly'],
    ),
    date_in: str = typer.Argument(
        datetime(year=2020, month=1, day=1).strftime('%d/%m/%Y'),
        help='The date of the start historical data.',
    ),
    date_out: str = typer.Argument(
        datetime.now().strftime('%d/%m/%Y'),
        help='The date of the end historical data.',
    ),
    email: str = typer.Option(
        None,
        help='The email of the API user.',
        envvar='BASE_EMAIL',
    ),
    to_csv: Path = typer.Option(
        None,
        help='If provided, the output will be saved in a csv file.',
        is_flag=True,
        confirmation_prompt=False,
    ),
    show_args: bool = typer.Option(
        False,
        help='If provided, the arguments will be displayed all options are used.',
        is_flag=True,
        show_default=False,
    ),
) -> None:
    console = Console()
    email = _load_email(email)
    inv = Invest(email)
    arguments = __args_to_crypto_api(
        date_in, date_out, symbol, name, time_frame
    )
    df = inv.crypto.get_historical_data(**arguments, as_dict=False)
    if to_csv:
        to_csv = to_csv if to_csv != Path('.') else Path('./output.csv')
        console.print(
            f'Your file will be saved on:{" ":<5}[bold][i]{to_csv.resolve()}[/i][bold]'
        )
        df.to_csv(to_csv, index=False)
        if show_args:
            _show_args(arguments)
        return
    table = df_to_table(df)
    success_text = Text('\nTABLE OF HISTORICAL DATA\n', style='#dcbdfb')
    console.print(success_text, table, justify='center')
    if show_args:
        _show_args(arguments)
