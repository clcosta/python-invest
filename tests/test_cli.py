import pandas as pd
from typer.testing import CliRunner

from python_invest.cli import cli
from python_invest.cli.commands.pandas_to_rich import df_to_table

expected_data = pd.read_csv('./tests/data/cryptoMonthly.csv')

expected_table = df_to_table(expected_data)

runner = CliRunner()


def test_no_command_in_cli_must_return_2_stout():
    result = runner.invoke(cli, [])
    # 2 is missing command in typer
    assert result.exit_code == 2
