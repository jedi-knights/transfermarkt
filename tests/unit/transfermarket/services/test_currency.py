import pytest
import requests_mock

from transfermarket.common.currency import Currency
from transfermarket.services.currency import CurrencyService


@pytest.fixture
def service():
    """
    Returns a CurrencyService instance.
    """
    return CurrencyService()


def test_get_exchange_rate(service):
    """
    This test is a bit of a cheat, because we are mocking the service method
    """

    # Arrange
    url = "https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1"

    with requests_mock.Mocker() as m:
        m.get(url, text="<span class='ccOutputRslt'>1.2 $</span>")

        # Act
        result = service.get_exchange_rate(Currency.EUR, Currency.USD)

    # Assert
    assert result == 1.2


def test_get_exchange_rate_missing_span(service):
    """
    This test is a bit of a cheat, because we are mocking the service method
    """

    # Arrange
    url = "https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1"

    with requests_mock.Mocker() as m:
        m.get(url, text="<h1>something</h1>")

        # Act/Assert
        with pytest.raises(ValueError, match="Could not find output result element"):
            service.get_exchange_rate(Currency.EUR, Currency.USD)


def test_convert(service, mocker):
    """
    This test is a bit of a cheat, because we are mocking the service method
    """

    # Arrange
    mocker.patch.object(service, "get_exchange_rate", return_value=1.2)

    # Act
    result = service.convert(100, Currency.EUR, Currency.USD)

    # Assert
    assert result == 120
