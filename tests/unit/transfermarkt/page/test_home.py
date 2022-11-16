import bs4
import pytest
import requests_mock

from transfermarkt.page.home import HomePage


@pytest.fixture(scope="module", params=["Hello World!"])
def home(request):
    with requests_mock.Mocker() as m:
        m.get("https://www.transfermarkt.com", text=request.param)

        return HomePage()


class TestConstructor:
    def test_url(self, home):
        assert home.url == "https://www.transfermarkt.com"

    def test_headers(self, home):
        assert home.headers is not None
        assert home.headers["user-agent"] == "transfermarkt"

    def test_soup(self, home):
        assert home.soup is not None

    def test_response(self, home):
        assert home.response is not None
        assert home.response.text == "Hello World!"

    def test_status_code(self, home):
        assert home.status_code == 200


class TestGetDomains:
    def test_with_empty_soup(self, home):
        # Arrange
        home.soup = bs4.BeautifulSoup("", "html.parser")

        # Act
        domains = home.get_domains()

        # Assert
        assert type(domains) == list
        assert len(domains) == 0

    def test_with_valid_soup(self, home):
        # Arrange
        markup = """
            <div class="tm-domainswitcher-box">
              <ul>
                <li><a href="https://test1.com">Test 1</a></li>
                <li><a href="https://test2.com">Test 2</a></li>
              </ul>
            </div>
        """

        home.soup = bs4.BeautifulSoup(markup, "html.parser")

        # Act
        domains = home.get_domains()

        # Assert
        assert domains is not None
        assert len(domains) == 2
        assert domains[0].name == "Test 1"
        assert domains[0].url == "https://test1.com"
        assert domains[1].name == "Test 2"
        assert domains[1].url == "https://test2.com"
