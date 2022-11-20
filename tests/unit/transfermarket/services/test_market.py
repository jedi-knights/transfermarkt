import pytest
import requests_mock

from transfermarket.common.gender import Gender
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


def test_headers(service):
    """
    Test the headers property.
    """
    assert service.headers == {"User-Agent": "transfermarkt"}


def test_get(service):
    """
    Test the get method.
    """
    with requests_mock.Mocker() as m:
        m.get("https://www.transfermarkt.com/quickselect/teams/1", json=[])
        res = service.get("/quickselect/teams/1")

    assert res.status_code == 200


def test_get_teams(service):
    """
    Test the get_teams method.
    """
    teams = [
        {"id": 1, "name": "Team 1", "link": "/team/1"},
        {"id": 2, "name": "Team 2", "link": "/team/2"},
    ]

    with requests_mock.Mocker() as m:
        m.get("https://www.transfermarkt.com/quickselect/teams/1", json=teams)
        result = service.get_teams("1")

    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].title == "Team 1"
    assert result[0].get_property("id") == '1'
    assert result[0].get_property("link") == "/team/1"

    assert result[1].id == 2
    assert result[1].title == "Team 2"
    assert result[1].get_property("id") == '2'
    assert result[1].get_property("link") == "/team/2"


def test_get_players(service):
    players = [
        {"id": 1, "name": "Player 1", "positionId": "4", "shirtNumber": "10"},
    ]

    with requests_mock.Mocker() as m:
        m.get("https://www.transfermarkt.com/quickselect/players/1", json=players)
        result = service.get_players("1")


    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].name == "Player 1"
    assert result[0].position == "Forward"
    assert result[0].gender == Gender.Male
    assert result[0].get_property("id") == '1'
    assert result[0].get_property("position_id") == '4'
    assert result[0].get_property("jersey_number") == '10'


def test_get_players_invalid_position(service):
    players = [
        {"id": 1, "name": "Player 1", "positionId": "5", "shirtNumber": "10"}
    ]

    with pytest.raises(ValueError, match="Unknown position identifier: 5"):
        with requests_mock.Mocker() as m:
            m.get("https://www.transfermarkt.com/quickselect/players/1", json=players)
            service.get_players("1")
