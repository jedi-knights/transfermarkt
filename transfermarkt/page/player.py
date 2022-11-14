import datetime as dt

from transfermarkt.page.object import PageObject
from transfermarkt.models.domain import Domain
from transfermarkt.page.utils import get_href_from_anchor, get_text_from_anchor
from common.utils import slugify

from common.services import currency_service


class PlayerPage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        slug = kwargs.get("slug")
        if slug is None:
            name = kwargs.get("name")
            if name is not None:
                slug = slugify(name)

        identifier = kwargs.get("identifier")

        user_agent = 'Mozilla/5.0'
        user_agent += '(X11; Linux x86_64)'
        user_agent += ' AppleWebKit/537.36'
        user_agent += ' (KHTML, like Gecko)'
        user_agent += ' Chrome/47.0.2526.106'
        user_agent += ' Safari/537.36'

        self.headers = {
            'User-Agent': user_agent
        }

        self.url = f"https://www.transfermarkt.com/{slug}/profil/spieler/{identifier}"
        self.load()

    @property
    def name(self) -> str:
        return self.soup.find("h1", class_=["data-header__headline-wrapper"]).text.strip()

    @property
    def height(self) -> str:
        return self.soup.find("span", {"itemprop": "height"}).text.strip()

    @property
    def citizenship(self) -> str:
        return self.soup.find("span", {"itemprop": "nationality"}).text.strip()

    @property
    def position(self) -> str:
        raise NotImplementedError()

    @property
    def caps(self) -> str:
        raise NotImplementedError()

    @property
    def goals(self) -> str:
        raise NotImplementedError()

    @property
    def market_value(self) -> str:
        wrapper = self.soup.find("a", class_=["data-header__market-value-wrapper"])
        value = wrapper.text.strip()

        pivot = value.find(" ")
        value = value[:pivot]

        symbol = value[0]

        unit = value[-1]
        if unit == "m":
            value = value[1:-1]
            value = float(value) * 1000000
        elif unit == "k":
            value = value[1:-1]
            value = float(value) * 1000
        else:
            value = value[1:]
            value = float(value)

        if symbol == "\N{euro sign}":
            value = currency_service.convert_euros_to_dollars(value)

        value = round(value, 2)

        return value

    @property
    def date_of_birth(self) -> dt.datetime:
        value = self.soup.find("span", {"itemprop": "birthDate"}).text.strip()

        lparen = value.index("(")
        if lparen is not None:
            value = value[:lparen].strip()

        return dt.datetime.strptime(value, "%b %d, %Y")

    @property
    def age(self) -> int:
        return (dt.datetime.now() - self.date_of_birth).days // 365

    @property
    def place_of_birth(self) -> str:
        return self.soup.find("span", {"itemprop": "birthPlace"}).text.strip()


if __name__ == "__main__":
    # page = PlayerPage(slug="eder", identifier="84481")
    page = PlayerPage(slug="lionel-messi", identifier="28003")

    print(page.market_value)
