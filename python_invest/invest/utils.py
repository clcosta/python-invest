__all__ = ['convert_dates_to_str', 'dict_to_url_params']
import re
from datetime import date
from urllib import parse


def convert_dates_to_str(from_date: date, to_date: date) -> tuple[str, str]:
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
    return from_date, to_date


def dict_to_url_params(data: dict) -> str:
    return parse.urlencode(data)
