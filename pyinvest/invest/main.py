from datetime import date
from pyinvest.const import API_URL
from .validators import validate_args
from .utils import dict_to_url_params, convert_dates_to_str
from .crypto import Crypto


class Invest:
    def __init__(self, email: str):
        self.email = email

    @property
    def crypto(self):
        return Crypto(self)

    @validate_args
    def _get_base_historical_url(
        self,
        product: str,
        from_date: str | date,
        to_date: str | date,
        time_frame: str = 'Daily',
    ) -> str:
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
