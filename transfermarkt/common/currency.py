from enum import Enum

class Currency(Enum):
    EUR = "€"
    GBP = "£"
    USD = "$"
    JPY = "¥"
    KRW = "₩"
    INR = "₹"
    RUB = "₽"

    def __repr__(self):
        return f"Currency.{self.name}"


def string_to_currency(string: str) -> Currency:
    for currency in Currency:
        if currency.value == string or currency.name == string:
            return currency

    raise ValueError(f"Currency {string} not found")

if __name__ == "__main__":
    for currency in Currency:
        print(currency)