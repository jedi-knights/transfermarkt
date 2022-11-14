import pytest

from transfermarkt.common.currency import Currency, string_to_currency


class TestStringToCurrency:
    def test_eur(self):
        assert string_to_currency("€") == Currency.EUR

    def test_eur_name(self):
        assert string_to_currency("EUR") == Currency.EUR

    def test_gbp(self):
        assert string_to_currency("£") == Currency.GBP

    def test_gbp_name(self):
        assert string_to_currency("GBP") == Currency.GBP

    def test_usd(self):
        assert string_to_currency("$") == Currency.USD

    def test_usd_name(self):
        assert string_to_currency("USD") == Currency.USD

    def test_jpy(self):
        assert string_to_currency("¥") == Currency.JPY

    def test_jpy_name(self):
        assert string_to_currency("JPY") == Currency.JPY

    def test_krw(self):
        assert string_to_currency("₩") == Currency.KRW

    def test_krw_name(self):
        assert string_to_currency("KRW") == Currency.KRW

    def test_inr(self):
        assert string_to_currency("₹") == Currency.INR

    def test_inr_name(self):
        assert string_to_currency("INR") == Currency.INR

    def test_rub(self):
        assert string_to_currency("₽") == Currency.RUB

    def test_rub_name(self):
        assert string_to_currency("RUB") == Currency.RUB

    def test_unknown(self):
        with pytest.raises(ValueError):
            string_to_currency("unknown")

    # noinspection PyTypeChecker
    def test_none(self):
        with pytest.raises(ValueError):
            string_to_currency(None)
