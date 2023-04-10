import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def df_to_table(
    dataframe: pd.DataFrame,
) -> Table:
    """Convert a pandas.DataFrame obj into a rich.Table obj.
    Args:
        dataframe (DataFrame): A Pandas DataFrame to be converted to a rich Table.
    Returns:
        Table: The rich Table instance passed, populated with the DataFrame values."""

    table = Table()

    for column in dataframe.columns:
        table.add_column(str(column))

    for _, value_list in dataframe.iterrows():
        row = []
        row += [str(x) for x in value_list]
        table.add_row(*row)

    return table
