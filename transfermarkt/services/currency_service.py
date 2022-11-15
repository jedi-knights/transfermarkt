import bs4
import requests


def get_euro_to_dollar_exchange_rate():
    url = "https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1"

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


def convert_euros_to_dollars(euros: float):
    return euros * (1/get_euro_to_dollar_exchange_rate())


if __name__ == "__main__":
    print(f"Euro to USD: {get_euro_to_dollar_exchange_rate()}")

    print(f"300,000 Euros to USD: {convert_euros_to_dollars(300000):.2f}")
