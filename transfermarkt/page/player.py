import datetime as dt

import bs4

from transfermarkt.common.currency import Currency
from transfermarkt.common.utils import slugify
from transfermarkt.page.object import PageObject
from transfermarkt.services.currency import CurrencyService


class PlayerPage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        slug = kwargs.get("slug")
        if slug is None:
            name = kwargs.get("name")
            if name is not None:
                slug = slugify(name)

        identifier = kwargs.get("identifier")
        self.currency_service = kwargs.get("currency_service", CurrencyService())

        user_agent = "transfermarkt"

        self.headers = {"user-agent": user_agent}

        self.url = f"https://www.transfermarkt.com/{slug}/profil/spieler/{identifier}"

        if kwargs.get("auto_load", False):
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
        value = "0.0"

        wrapper = self.soup.find("a", class_=["data-header__market-value-wrapper"])

        waehrung_items = wrapper.find_all("span", class_=["waehrung"])

        if len(waehrung_items) == 2:
            symbol = waehrung_items[0].text.strip()
            unit = waehrung_items[1].text.strip()

            for child in list(wrapper.children):
                if type(child) == bs4.element.NavigableString:
                    value = child.strip()
                    if len(value) > 0:
                        value = value.replace('"', "")
                        break

            if unit == "m":
                value = float(value) * 1000000
            elif unit == "k":
                value = float(value) * 1000
            else:
                value = float(value)

            if symbol == "\N{euro sign}":
                value = self.currency_service.convert(value, Currency.EUR, Currency.USD)

            value = round(value, 2)
            value = str(value)
        else:
            raise ValueError("Could not parse market value")

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
