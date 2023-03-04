from datetime import date

from python_invest.const import API_URL

from .crypto import Crypto
from .utils import convert_dates_to_str, dict_to_url_params
from .validators import validate_args


class Invest:
    """
    The Invest class is the main class that will be used to interact with all invest module.

    Args:
        email (str): The email of the user to receive validation API Link.
    """

    def __init__(self, email: str):
        self.email = email

    @property
    def crypto(self):
        """
        The crypto property is used to interact with the Crypto class.

        Returns:
            (Crypto): The Crypto class instance.
        """
        return Crypto(self)

    @validate_args
    def _get_base_historical_url(
        self,
        product: str,
        from_date: str | date,
        to_date: str | date,
        time_frame: str = 'Daily',
    ) -> str:
        """
        The _get_base_historical_url method is used to get the base historical url.
        """
        from_date, to_date = convert_dates_to_str(from_date, to_date)
        url_params = dict_to_url_params(
            {
                'product': product,
                'from_date': from_date,
                'to_date': to_date,
                'time_frame': time_frame,
                'type': 'historical_data',
            }
        )
        url = API_URL.format(email=self.email, args=url_params)
        return url
