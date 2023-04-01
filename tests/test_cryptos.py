import re

import httpx
import pytest

from python_invest import Invest

intervals = ['Daily', 'Monthly', 'Weekly']
intervals_kwargs = [
    {
        'symbol': 'BTC',
        'from_date': '01/01/2023',
        'to_date': '01/02/2023',
        'as_dict': False,
        'time_frame': 'Daily',
    },
    {
        'symbol': 'BTC',
        'from_date': '01/01/2023',
        'to_date': '02/01/2023',
        'as_dict': False,
        'time_frame': 'Monthly',
    },
    {
        'symbol': 'BTC',
        'from_date': '01/01/2023',
        'to_date': '01/31/2023',
        'as_dict': False,
        'time_frame': 'Weekly',
    },
]
params = list(zip(intervals, intervals_kwargs))


@pytest.mark.parametrize('interval,interval_kwargs', params, scope='class')
class TestHistoricalDataWithPreCachedData:
    def test_crypto_historical_data_using_symbol_expected_asdf(
        self, inv, interval_data, interval_kwargs
    ):
        data = inv.crypto.get_historical_data(**interval_kwargs).sort_values(
            'Date'
        )
        assert data.equals(interval_data.expected_asdf)

    def test_crypto_historical_data_using_symbol_expected_asdict(
        self, inv, interval_data, interval_kwargs
    ):
        kwargs = interval_kwargs.copy()
        kwargs['as_dict'] = True
        data = inv.crypto.get_historical_data(**kwargs)
        assert data == interval_data.expected_asdict

    def test_crypto_historical_data_using_name_expected_asdf(
        self, inv, interval_data, interval_kwargs
    ):
        kwargs = interval_kwargs.copy()
        kwargs.update({'symbol': None, 'name': 'bitcoin'})
        data = inv.crypto.get_historical_data(**kwargs).sort_values('Date')
        assert data.equals(interval_data.expected_asdf)

    def test_crypto_historical_data_using_name_expected_asdict(
        self, inv, interval_data, interval_kwargs
    ):
        kwargs = interval_kwargs.copy()
        kwargs.update({'symbol': None, 'name': 'bitcoin', 'as_dict': True})
        data = inv.crypto.get_historical_data(**kwargs)
        assert data == interval_data.expected_asdict


class TestBasicsListCryptoAndOtherArguments:

    start_crypto_list = [
        {'tag': '0chain', 'name': '0Chain', 'symbol': 'ZCN'},
        {'symbol': 'ZRX', 'tag': '0x', 'name': '0x'},
        {'tag': '0xbtc', 'symbol': '0xBTC', 'name': '0xBitcoin'},
        {'tag': '1inch', 'symbol': '1INCH', 'name': '1inch'},
        {'tag': '2give', 'name': '2GIVE', 'symbol': '2GIVE'},
        {'symbol': 'AAVE', 'tag': 'aave', 'name': 'Aave'},
    ]

    def test_start_six_items_of_crypto_list_in_firebase_equals_to_start_of_crypto_list(
        self, inv
    ):
        assert inv.crypto.get_list()[:6] == self.start_crypto_list

    def test_empty_symbol_and_name(self, inv):
        error_msg = 'Necessary crypto indentifier. Please provide a crypto Symbol or name.'
        with pytest.raises(ValueError, match=error_msg):
            inv.crypto.get_historical_data(symbol=None, name=None)

    # @pytest.mark.parametrize('inv', [Invest('your@email.com')])
    # def test_bad_email(self, inv):
    #     error_msg_pattern = r"^[Failure in get crypto list. Server error.]+"
    #     with pytest.raises(httpx.HTTPError, match=re.compile(error_msg_pattern)):
    #         inv.crypto.get_historical_data(symbol='BTC')

    # @pytest.mark.parametrize(
    #     'inv', [Invest('pyinvest@gmail.com')]
    # )   # This is a fictional but valid email
    # def test_sent_mail_to_valid_email(self, inv):
    #     error_msg = 'The Scrapper API sent to your email address the verification link. Please verify your email before run the code again.'
    #     with pytest.raises(PermissionError, match=error_msg):
    #         inv.crypto.get_historical_data(symbol='BTC')
