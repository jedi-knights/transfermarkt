import datetime

import bs4
from freezegun import freeze_time

from transfermarket.page import utils


class TestGetHrefFromAnchor:
    def test_undefined(self):
        """
        Test that the function returns None when the anchor is undefined.
        """
        assert utils.get_href_from_anchor(None) is None

    def test_anchor(self):
        """
        Test that the function returns the href of the anchor.
        """
        html = "<a href='https://www.acme.com'>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_href_from_anchor(anchor) == "https://www.acme.com"

    def test_container(self):
        """
        Test that the function returns the href of the anchor.
        """
        html = "<div><a href='https://www.acme.com'>Acme</a></div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_href_from_anchor(container) == "https://www.acme.com"

    def test_no_anchor(self):
        html = "<div>Acme</div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_href_from_anchor(container) is None

    def test_no_href(self):
        html = "<a>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_href_from_anchor(anchor) is None

    def test_empty_href(self):
        html = "<a href=''>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_href_from_anchor(anchor) is None


class TestGetTextFromAnchor:
    def test_undefined(self):
        """
        This test is here to ensure that the function does not fail when
        """
        assert utils.get_text_from_anchor(None) is None

    def test_with_anchor(self):
        """
        Make sure the get_text_from_anchor function returns the text from the anchor.
        """
        html = "<a href='https://www.acme.com'>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(anchor) == "Acme"

    def test_no_anchor(self):
        """
        Make sure the get_text_from_anchor function returns None when there is no anchor.
        """
        html = "<div>Acme</div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(container) is None

    def test_no_text(self):
        """
        Make sure the get_text_from_anchor function returns None when there is no text.
        """
        html = "<a href='https://www.acme.com'></a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(anchor) is None

    def test_text_with_only_spaces(self):
        """
        Make sure the get_text_from_anchor function returns None when there is only spaces.
        """
        html = "<a href='https://www.acme.com'>  </a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(anchor) is None


@freeze_time("2020-11-04")
def test_current_season(mocker):
    # Arrange
    mocked_get_season = mocker.patch.object(utils, "__get_season", return_value=13)

    # Act
    season = utils.current_season()

    # Assert
    mocked_get_season.assert_called_once_with(datetime.date(2020, 11, 4))
    assert season == 13


@freeze_time("2020-11-04")
def test_get_season():
    # Arrange
    input_date = datetime.date(2020, 11, 4)

    # Act
    season = utils.__get_season(input_date)

    # Assert
    assert season == 2020


def test_get_season_same_day():
    # Arrange
    input_date = datetime.date(2020, 6, 30)

    # Act
    season = utils.__get_season(input_date)

    # Assert
    assert season == 2019
