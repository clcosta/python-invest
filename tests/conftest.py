import pytest

from python_invest import Invest

from .utils import get_data


class BaseHistorical:
    def __init__(self, interval: str) -> None:
        self.interval = interval
        self.expected_asdict, self.expected_asdf = get_data(interval)

    def __repr__(self) -> str:
        return f'BaseHistorical({self.interval})'


@pytest.fixture
def interval_data(interval: str) -> BaseHistorical:
    yield BaseHistorical(interval)


@pytest.fixture
def inv(email: str = None) -> Invest:
    # Return Invest instance using Temp-mail verified
    yield Invest(email if email else 'secov14820@vootin.com')
