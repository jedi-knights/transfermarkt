import bs4

from transfermarkt.page import utils


class TestGetHrefFromAnchor:
    def test_undefined(self):
        assert utils.get_href_from_anchor(None) is None

    def test_anchor(self):
        html = "<a href='https://www.acme.com'>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_href_from_anchor(anchor) == "https://www.acme.com"

    def test_container(self):
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
        assert utils.get_text_from_anchor(None) is None

    def test_anchor(self):
        html = "<a href='https://www.acme.com'>Acme</a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(anchor) == "Acme"

    def test_container(self):
        html = "<div><a href='https://www.acme.com'>Acme</a></div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(container) == "Acme"

    def test_no_anchor(self):
        html = "<div>Acme</div>"
        container = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(container) is None

    def test_no_text(self):
        html = "<a href='https://www.acme.com'></a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(anchor) is None

    def test_text_with_only_spaces(self):
        html = "<a href='https://www.acme.com'>  </a>"
        anchor = bs4.BeautifulSoup(html, "html.parser")
        assert utils.get_text_from_anchor(anchor) is None
