import bs4
import pytest
import requests_mock

from transfermarket.page.competitions import CompetitionsPage


@pytest.fixture
def page():
    """
    Returns a CompetitionsPage instance.
    """
    return CompetitionsPage(auto_load=False)


class TestConstructor:
    def test_url(self, page):
        """
        Test the url property.
        """
        # Arrange
        expected = "https://www.transfermarkt.com/wettbewerbe/europa?ajax=yw1&page=1"

        # Act
        actual = page.url

        # Assert
        assert actual == expected

    def test_headers(self, page):
        """
        Test the headers property.
        """
        # Arrange
        expected = {"user-agent": "transfermarkt"}

        # Act
        actual = page.headers

        # Assert
        assert actual == expected

    def test_load(self, mocker):
        """
        Test the load method.
        """
        # Arrange
        mocked_load = mocker.patch("transfermarket.page.competitions.CompetitionsPage.load")

        # Act
        with requests_mock.Mocker() as m:
            m.get("https://www.transfermarkt.com/wettbewerbe/europa?ajax=yw1&page=1", text="Hello World!")
            CompetitionsPage(auto_load=True)

        # Assert
        assert mocked_load.called_once()


def test_page_count(page):
    """
    Test the page_count property.
    """
    # Arrange
    markup = """
    <ul class="tm-pagination">
        <li class="tm-pagination__list-item">
          <a href="/wettbewerbe/europa?page=10"
             title="Page 10"
             class="tm-pagination__link">10</a>
        </li>
        <li></li>
        <li></li>
    </ul>
    """
    page.soup = bs4.BeautifulSoup(markup, "html.parser")

    # Act
    actual = page.get_page_count()

    # Assert
    assert actual == 10
