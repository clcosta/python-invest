__all__ = ['Crypto']

from datetime import date

import httpx as req
import pandas as pd
from httpx._exceptions import HTTPError

from python_invest.const import FB_BASE_URL, FB_CRYPTO_DOC_ID

from .firebase import parser
from .utils import dict_to_url_params

pd.options.mode.chained_assignment = None


class Crypto:
    """
    The Crypto class will be used by the Invest class, the methods of the class will be accessed to obtain crypto area data.

    Warning:
        This class is not intended to be used directly.

    Args:
        invest_instance (Invest): An instance of the Invest class.
    """

    def __init__(self, invest_instance):
        self.__invest_intance = invest_instance

    def get_historical_data(
        self,
        symbol: str = None,
        from_date: str | date = '2023-01-01',
        to_date: str | date = '2023-02-01',
        name: str = None,
        time_frame: str = 'Daily',
        as_dict: bool = False,
    ) -> dict | pd.DataFrame:
        """
        Get historical data from crypto, the return could be raw in dict or filtered DataFrame.

        Note:
            The `symbol` or `name` is required, if not provided, the method will return an error.

        Args:
            symbol (str, optional): The symbol of the crypto. Defaults to None.
            from_date (str | date, optional): The start date of the historical data. Defaults to '2023-01-01'.
            to_date (str | date, optional): The end date of the historical data. Defaults to '2023-02-01'.
            name (str, optional): The name of the crypto. Defaults to None.
            time_frame (str, optional): The time frame of the historical data. Defaults to 'Daily'.
            as_dict (bool, optional): Whether to return the data as dict. Defaults to False.

        Returns:
            (dict | pd.DataFrame): The historical data.
        """
        if not any((symbol, name)):
            raise ValueError(
                'Necessary crypto indentifier. Please provide a crypto Symbol or name.'
            )
        url = self.__invest_intance._get_base_historical_url(
            product='cryptos',
            from_date=from_date,
            to_date=to_date,
            time_frame=time_frame,
        )

        data = {
            'symbol': symbol if symbol else '',
            'name': name if name else '',
        }
        new_args = dict_to_url_params(data)
        url += f'&{new_args}'
        res = req.get(url)
        if res.text.lower() in (
            'email verification sent.',
            'email address not verified.',
        ):
            raise PermissionError(
                'The Scrapper API sent to your email address the verification link. Please verify your email before run the code again.'
            )
        match res.status_code:
            case 400 | 404 | 401:
                raise HTTPError(
                    f'Failure in get crypto data. Bad request. {res.status_code}: {res.text}'
                )
            case 500:
                raise HTTPError(
                    f'Failure in get crypto data. Server error. {res.status_code}: {res.text}'
                )
            case _:
                if res.status_code != 200:
                    raise HTTPError(
                        f'Unknown error. {res.status_code}: {res.text}'
                    )
        res_json = res.json()['data']
        if as_dict:
            return res_json
        raw_df = pd.DataFrame(res_json)
        df = raw_df[
            [
                'last_close',
                'last_open',
                'last_max',
                'last_min',
                'volumeRaw',
                'change_precent',
            ]
        ]
        df.rename(
            {
                'last_close': 'Price',
                'last_open': 'Open',
                'last_max': 'High',
                'last_min': 'Low',
                'volumeRaw': 'Vol',
                'change_precent': 'Change',
            },
            inplace=True,
            axis=1,
        )
        df['Date'] = pd.to_datetime(
            pd.to_datetime(raw_df.rowDateTimestamp)
        ).dt.strftime('%Y-%m-%d')
        return df

    def get_list(self) -> list:
        """
        Get the list of cryptos.

        Returns:
            (list[dict]): The return will be a list of `name`, `symbol` and `tag` of the cryptos.
        """
        url = FB_BASE_URL + FB_CRYPTO_DOC_ID
        response = req.get(url)
        if response.status_code != 200:
            raise ValueError(
                f'Failure in get crypto list. {response.status_code}: {response.text}'
            )
        data = response.json()['fields']['data']['arrayValue'][
            'values'
        ]  # pre defined in firebase
        return parser(data)
