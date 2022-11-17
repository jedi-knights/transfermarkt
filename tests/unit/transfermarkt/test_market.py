import pytest

from transfermarkt.market import Market
from transfermarkt.models.competition import Competition
from transfermarkt.page.competitions import CompetitionsPage
from transfermarkt.services.market import MarketService


@pytest.fixture
def service():
    """
    Returns a MarketService instance.
    """
    return MarketService()


@pytest.fixture
def page():
    """
    Returns a CompetitionsPage instance.
    """
    return CompetitionsPage()


@pytest.fixture
def market(service, page):
    """
    Returns a Market instance.
    """
    return Market(market_service=service, competitions_page=page)


@pytest.fixture
def test_competitions():
    """
    Returns a list of Competition instances.
    """
    return [
        Competition(id=1, name="Competition 1"),
        Competition(id=2, name="Competition 2"),
        Competition(id=3, name="Competition 3"),
    ]
