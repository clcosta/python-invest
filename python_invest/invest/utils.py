__all__ = ['convert_dates_to_str', 'dict_to_url_params']
import re
from datetime import date, datetime
from urllib import parse

from .validators import validate_date_in_out


def convert_dates_to_str(
    from_date: str | date, to_date: str | date
) -> tuple[str, str]:
    """
    Convert date objects to string and validate string date format.
    Return tuple of string dates in format d/m/Y.
    """
    pattern = r'([0-9]{2}\/[0-9]{2}\/[0-9]{4})'
    try:
        from_date = from_date.strftime('%m/%d/%Y')
    except AttributeError:
        if not re.fullmatch(pattern, from_date):
            raise ValueError(
                f'The date format is invalid, please use d/m/Y format in from_date argument.'
            )
    try:
        to_date = to_date.strftime('%m/%d/%Y')
    except AttributeError:
        if not re.fullmatch(pattern, to_date):
            raise ValueError(
                f'The date format is invalid, please use d/m/Y format in to_date argument.'
            )
    validate_date_in_out(
        datetime.strptime(from_date, '%d/%m/%Y'),
        datetime.strptime(to_date, '%d/%m/%Y'),
    )
    return from_date, to_date


def dict_to_url_params(data: dict) -> str:
    """
    Convert dictionary to url parameters.
    """
    return parse.urlencode(data)
