import pytest

from transfermarkt.market import Market
from transfermarkt.models.competition import Competition
from transfermarkt.page.competitions import CompetitionsPage
from transfermarkt.services.market import MarketService


@pytest.fixture
def service():
    return MarketService()


@pytest.fixture
def page():
    return CompetitionsPage()


@pytest.fixture
def market(service, page):
    return Market(market_service=service, competitions_page=page)


@pytest.fixture
def test_competitions():
    return [
        Competition(id=1, name="Competition 1"),
        Competition(id=2, name="Competition 2"),
        Competition(id=3, name="Competition 3"),
    ]
