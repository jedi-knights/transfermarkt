import bs4
import requests

from transfermarkt.common.currency import Currency
from transfermarkt.common.utils import urljoin


class CurrencyService:
    BASE_URL = "https://www.x-rates.com"

    def __init__(self, **kwargs):
        pass

    def get_exchange_rate(self, from_currency: Currency, to_currency: Currency) -> float:
        params = f"?from={from_currency.name}&to={to_currency.name}&amount=1"

        url = urljoin(self.BASE_URL, "calculator")
        url = urljoin(url, params)

        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.content, "html.parser")

        element = soup.find("span", class_=["ccOutputRslt"])

        if element is None:
            raise ValueError("Could not find output result element")

        value = element.text
        pivot = value.find(" ")
        value = value[:pivot]

        return float(value)

    def convert(self, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        return amount * self.get_exchange_rate(from_currency, to_currency)
