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
