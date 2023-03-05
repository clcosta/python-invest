import httpx
import pytest

from python_invest import Invest

from .utils import get_data

inv = Invest('secov14820@vootin.com')   # Temp mail


class TestDailyData:

    expected_asdict, expected_asdf = get_data('Daily')

    def test_crypto_historical_data_symbol_asdf(self):

        data = inv.crypto.get_historical_data(
            symbol='BTC',
            from_date='01/01/2023',
            to_date='01/02/2023',
            as_dict=False,
        ).sort_values('Date')
        assert data.to_dict() == self.expected_asdf.to_dict()

    def test_crypto_historical_data_symbol_asdict(self):

        data = inv.crypto.get_historical_data(
            symbol='BTC',
            from_date='01/01/2023',
            to_date='01/02/2023',
            as_dict=True,
        )
        assert data == self.expected_asdict

    def test_crypto_historical_data_name(self):

        data = (
            inv.crypto.get_historical_data(
                name='bitcoin',
                from_date='01/01/2023',
                to_date='01/02/2023',
                as_dict=False,
            )
            .sort_values('Date')
            .sort_values('Date')
        )
        assert data.to_dict() == self.expected_asdf.to_dict()

    def test_crypto_historical_data_name_asdict(self):

        data = inv.crypto.get_historical_data(
            name='bitcoin',
            from_date='01/01/2023',
            to_date='01/02/2023',
            as_dict=True,
        )
        assert data == self.expected_asdict


class TestMonthlyData:

    expected_asdict, expected_asdf = get_data('Monthly')

    def test_crypto_historical_data_symbol_asdf(self):

        data = inv.crypto.get_historical_data(
            symbol='BTC',
            from_date='01/01/2023',
            to_date='02/01/2023',
            as_dict=False,
            time_frame='Monthly',
        ).sort_values('Date')
        assert data.to_dict() == self.expected_asdf.to_dict()

    def test_crypto_historical_data_symbol_asdict(self):

        data = inv.crypto.get_historical_data(
            symbol='BTC',
            from_date='01/01/2023',
            to_date='02/01/2023',
            as_dict=True,
            time_frame='Monthly',
        )
        assert data == self.expected_asdict

    def test_crypto_historical_data_name(self):

        data = inv.crypto.get_historical_data(
            name='bitcoin',
            from_date='01/01/2023',
            to_date='02/01/2023',
            as_dict=False,
            time_frame='Monthly',
        ).sort_values('Date')
        assert data.to_dict() == self.expected_asdf.to_dict()

    def test_crypto_historical_data_name_asdict(self):

        data = inv.crypto.get_historical_data(
            name='bitcoin',
            from_date='01/01/2023',
            to_date='02/01/2023',
            as_dict=True,
            time_frame='Monthly',
        )
        assert data == self.expected_asdict


class TestWeeklyData:

    expected_asdict, expected_asdf = get_data('Weekly')

    def test_crypto_historical_data_symbol_asdf(self):

        data = inv.crypto.get_historical_data(
            symbol='BTC',
            from_date='01/01/2023',
            to_date='01/31/2023',
            as_dict=False,
            time_frame='Weekly',
        ).sort_values('Date')
        assert data.to_dict() == self.expected_asdf.to_dict()

    def test_crypto_historical_data_symbol_asdict(self):

        data = inv.crypto.get_historical_data(
            symbol='BTC',
            from_date='01/01/2023',
            to_date='01/31/2023',
            as_dict=True,
            time_frame='Weekly',
        )
        assert data == self.expected_asdict

    def test_crypto_historical_data_name(self):

        data = inv.crypto.get_historical_data(
            name='bitcoin',
            from_date='01/01/2023',
            to_date='01/31/2023',
            as_dict=False,
            time_frame='Weekly',
        ).sort_values('Date')
        assert data.to_dict() == self.expected_asdf.to_dict()

    def test_crypto_historical_data_name_asdict(self):

        data = inv.crypto.get_historical_data(
            name='bitcoin',
            from_date='01/01/2023',
            to_date='01/31/2023',
            as_dict=True,
            time_frame='Weekly',
        )
        assert data == self.expected_asdict


class TestBasics:

    start_crypto_list = [
        {'tag': '0chain', 'name': '0Chain', 'symbol': 'ZCN'},
        {'symbol': 'ZRX', 'tag': '0x', 'name': '0x'},
        {'tag': '0xbtc', 'symbol': '0xBTC', 'name': '0xBitcoin'},
        {'tag': '1inch', 'symbol': '1INCH', 'name': '1inch'},
        {'tag': '2give', 'name': '2GIVE', 'symbol': '2GIVE'},
        {'symbol': 'AAVE', 'tag': 'aave', 'name': 'Aave'},
    ]

    def test_crypto_list(self):
        assert inv.crypto.get_list()[:6] == self.start_crypto_list

    def test_empty_symbol_and_name(self):
        error_msg = 'Necessary crypto indentifier. Please provide a crypto Symbol or name.'
        with pytest.raises(ValueError, match=error_msg):
            inv.crypto.get_historical_data(symbol=None, name=None)

    def test_bad_email(self):
        instance = Invest('your@email.com')
        error_msg = 'Failure in get crypto data. Bad request. 401: Please specify a valid email address in "email='
        with pytest.raises(httpx.HTTPError, match=error_msg):
            instance.crypto.get_historical_data(symbol='BTC')

    def test_sent_mail_to_valid_email(self):
        instance = Invest('pyinvest@gmail.com')
        error_msg = 'The Scrapper API sent to your email address the verification link. Please verify your email before run the code again.'
        with pytest.raises(PermissionError, match=error_msg):
            instance.crypto.get_historical_data(symbol='BTC')
