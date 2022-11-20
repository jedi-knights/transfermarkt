import pytest

from transfermarket.models.player import Player
from transfermarket.models.team import Team
from transfermarket.page.competitions import CompetitionsPage
from transfermarket.market import Market
from transfermarket.models.competition import Competition
from transfermarket.services.market import MarketService


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

@pytest.fixture
def test_teams():
    """
    Returns a list of Team instances.
    """
    return [
        Team(id=1, name="Team 1"),
        Team(id=2, name="Team 2"),
        Team(id=3, name="Team 3"),
    ]


@pytest.fixture
def test_players():
    """
    Returns a list of Player instances.
    """
    return [
        Player(id=1, name="Player 1"),
        Player(id=2, name="Player 2")
    ]


class TestConstructor:
    def test_market_service(self, market):
        """
        Test the market_service property.
        """
        assert isinstance(market.market_service, MarketService)

    def test_competitions_page(self, market):
        """
        Test the competitions_page property.
        """
        assert isinstance(market.competitions_page, CompetitionsPage)


def test_get_competitions(market, page, test_competitions, mocker):
    """
    Test the get_competitions method.
    """
    # Arrange
    mocked_get_competitions = mocker.patch.object(page, "get_competitions", return_value=test_competitions)

    # Act
    competitions = market.get_competitions()

    # Assert
    assert mocked_get_competitions.called_once()
    assert competitions == test_competitions


def test_get_teams(market, service, test_teams, mocker):
    """
    Test the get_teams method.
    """
    # Arrange
    mocked_get_teams = mocker.patch.object(service, "get_teams", return_value=test_teams)

    # Act
    teams = market.get_teams("1")

    # Assert
    assert mocked_get_teams.called_once_with("1")
    assert teams == test_teams


def test_get_players(market, service, test_players, mocker):
    """
    Test the get_players method.
    """
    # Arrange
    mocked_get_players = mocker.patch.object(service, "get_players", return_value=test_players)

    # Act
    players = market.get_players("1")

    # Assert
    assert mocked_get_players.called_once_with("1")
    assert players == test_players
