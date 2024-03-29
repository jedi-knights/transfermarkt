import datetime

import bs4
import pytest

from transfermarket.common.currency import Currency
from transfermarket.page.player import PlayerPage


@pytest.fixture
def player():
    """Returns a PlayerPage instance for Kevin De Bruyne

    url: https://www.transfermarkt.com/kevin-de-bruyne/profil/spieler/88755
    """
    return PlayerPage(slug="kevin-de-bruyne", identifier="88755", auto_load=False)


class TestConstructor:
    """
    Test the player constructor.
    """

    def test_url_with_slug(self, player):
        """
        Test the url property when the slug is provided.
        """
        assert player.url == "https://www.transfermarkt.com/kevin-de-bruyne/profil/spieler/88755"

    def test_url_with_name(self):
        """
        Test the url property when the name is provided.
        """
        player = PlayerPage(name="Kevin De Bruyne", identifier="88755", auto_load=False)

        assert player.url == "https://www.transfermarkt.com/kevin-de-bruyne/profil/spieler/88755"

    def test_currency_service(self, player):
        """
        Test the currency service property.
        """
        assert player.currency_service is not None

    def test_headers(self, player):
        """
        Test the headers property.
        """
        assert player.headers is not None
        assert player.headers["user-agent"] == "transfermarkt"
        assert len(player.headers) == 1

    def test_auto_load(self, mocker):
        """
        Test the auto_load property.
        """
        mocked_load = mocker.patch("transfermarket.page.player.PlayerPage.load")

        PlayerPage(slug="kevin-de-bruyne", identifier="88755", auto_load=True)

        assert mocked_load.called_once()


def test_height(player):
    """
    Test the height property.
    """
    # Arrange
    markup = """
        <span itemprop="height">1,80 m</span>
    """

    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.height == "1,80 m"


def test_citizenship(player):
    """
    Test the citizenship property.
    """
    # Arrange
    markup = """
        <span itemprop="nationality">Belgium</span>
    """

    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.citizenship == "Belgium"


def test_name(player):
    """
    Test the name property.
    """
    # Arrange
    markup = """
        <h1 class="data-header__headline-wrapper">Kevin De Bruyne</h1>
    """

    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.name == "Kevin De Bruyne"


def test_position(player):
    """
    Test the position property.
    """
    with pytest.raises(NotImplementedError):
        assert player.position


def test_caps(player):
    """
    Test the caps property.
    """
    with pytest.raises(NotImplementedError):
        assert player.caps


def test_goals(player):
    """
    Test the goals property.
    """
    with pytest.raises(NotImplementedError):
        assert player.goals


def test_date_of_birth(player):
    """
    Test the date_of_birth property.
    """
    # Arrange
    markup = """
        <span itemprop="birthDate">Jun 28, 1991 (31)</span>
    """

    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.date_of_birth == datetime.datetime(1991, 6, 28, 0, 0)


def test_age(player):
    """
    Test the age property.
    """
    # Arrange
    markup = """
        <span itemprop="birthDate">Jun 28, 1991 (31)</span>
    """

    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.age == 31


def test_place_of_birth(player):
    """
    Test the place_of_birth property.
    """
    # Arrange
    markup = """
        <span itemprop="birthPlace">Bruges, Belgium</span>
    """

    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.place_of_birth == "Bruges, Belgium"


def test_market_value_millions(player, mocker):
    """
    Test the market_value property when the value is in millions.
    """
    # Arrange
    markup = """
        <a href="/kevin-de-bruyne/marktwertverlauf/spieler/88755" class="data-header__market-value-wrapper">
            <span class="waehrung">€</span>
            "80.00"
            <span class="waehrung">m</span>
            <p class="data-header__last-update">Last update: Nov 3, 2022</p>
        </a>
    """
    mocker.patch.object(player.currency_service, "convert", return_value=1.23)
    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.market_value == "1.23"
    assert player.currency_service.convert.called_once_with("80.00", "€", "m")


def test_market_value_thousands(player, mocker):
    """
    Test the market_value property when the value is in thousands.
    """
    # Arrange
    markup = """
        <a href="/kevin-de-bruyne/marktwertverlauf/spieler/88755" class="data-header__market-value-wrapper">
            <span class="waehrung">€</span>
            "80.00"
            <span class="waehrung">k</span>
            <p class="data-header__last-update">Last update: Nov 3, 2022</p>
        </a>
    """
    mocker.patch.object(player.currency_service, "convert", return_value=1.23)
    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.market_value == "1.23"
    assert player.currency_service.convert.called_once_with("80.00", Currency.EUR, Currency.USD)


def test_market_value_question_unit(player, mocker):
    """
    Test the market_value property when the value is in unknown units.
    """
    # Arrange
    markup = """
        <a href="/kevin-de-bruyne/marktwertverlauf/spieler/88755" class="data-header__market-value-wrapper">
            <span class="waehrung">€</span>
            "80.00"
            <span class="waehrung">?</span>
            <p class="data-header__last-update">Last update: Nov 3, 2022</p>
        </a>
    """
    mocker.patch.object(player.currency_service, "convert", return_value=1.23)
    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    assert player.market_value == "1.23"
    assert player.currency_service.convert.called_once_with("80.00", Currency.EUR, Currency.USD)


def test_malformed_market_value(player, mocker):
    """
    Test the market_value property when the value is malformed.
    """
    # Arrange
    markup = """
        <a href="/kevin-de-bruyne/marktwertverlauf/spieler/88755" class="data-header__market-value-wrapper">
            "80.00"
            <span class="waehrung">m</span>
            <p class="data-header__last-update">Last update: Nov 3, 2022</p>
        </a>
    """
    mocked_convert = mocker.patch.object(player.currency_service, "convert", return_value=1.23)
    player.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act/Assert
    with pytest.raises(ValueError, match="Could not parse market value"):
        assert player.market_value

    assert mocked_convert.not_called()
