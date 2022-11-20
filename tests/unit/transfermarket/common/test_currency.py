import pytest

from transfermarket.common.currency import Currency, string_to_currency


class TestStringToCurrency:
    def test_eur(self):
        """
        Make sure it the string_to_currency function returns the correct currency for EUR.
        """
        assert string_to_currency("€") == Currency.EUR

    def test_eur_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for EUR.
        """
        assert string_to_currency("EUR") == Currency.EUR

    def test_gbp(self):
        """
        Make sure it the string_to_currency function returns the correct currency for GBP.
        """
        assert string_to_currency("£") == Currency.GBP

    def test_gbp_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for GBP.
        """
        assert string_to_currency("GBP") == Currency.GBP

    def test_usd(self):
        """
        Make sure it the string_to_currency function returns the correct currency for USD.
        """
        assert string_to_currency("$") == Currency.USD

    def test_usd_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for USD.
        """
        assert string_to_currency("USD") == Currency.USD

    def test_jpy(self):
        """
        Make sure it the string_to_currency function returns the correct currency for JPY.
        """
        assert string_to_currency("¥") == Currency.JPY

    def test_jpy_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for JPY.
        """
        assert string_to_currency("JPY") == Currency.JPY

    def test_krw(self):
        """
        Make sure it the string_to_currency function returns the correct currency for KRW.
        """
        assert string_to_currency("₩") == Currency.KRW

    def test_krw_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for KRW.
        """
        assert string_to_currency("KRW") == Currency.KRW

    def test_inr(self):
        """
        Make sure it the string_to_currency function returns the correct currency for INR.
        """
        assert string_to_currency("₹") == Currency.INR

    def test_inr_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for INR.
        """
        assert string_to_currency("INR") == Currency.INR

    def test_rub(self):
        """
        Make sure it the string_to_currency function returns the correct currency for RUB.
        """
        assert string_to_currency("₽") == Currency.RUB

    def test_rub_name(self):
        """
        Make sure it the string_to_currency function returns the correct currency for RUB.
        """
        assert string_to_currency("RUB") == Currency.RUB

    def test_unknown(self):
        """
        Make sure it the string_to_currency function raises a ValueError for an unknown currency.
        """
        with pytest.raises(ValueError):
            string_to_currency("unknown")

    # noinspection PyTypeChecker
    def test_none(self):
        """
        Make sure it the string_to_currency function raises a ValueError for None.
        """
        with pytest.raises(ValueError):
            string_to_currency(None)


class TestCurrencyRepr:
    def test_eur(self):
        """
        Make sure the repr function returns the correct string for EUR.
        """
        assert repr(Currency.EUR) == "Currency.EUR"

    def test_gbp(self):
        """
        Make sure the repr function returns the correct string for GBP.
        """
        assert repr(Currency.GBP) == "Currency.GBP"

    def test_usd(self):
        """
        Make sure the repr function returns the correct string for USD.
        """
        assert repr(Currency.USD) == "Currency.USD"

    def test_jpy(self):
        """
        Make sure the repr function returns the correct string for JPY.
        """
        assert repr(Currency.JPY) == "Currency.JPY"

    def test_krw(self):
        """
        Make sure the repr function returns the correct string for KRW.
        """
        assert repr(Currency.KRW) == "Currency.KRW"

    def test_inr(self):
        """
        Make sure the repr function returns the correct string for INR.
        """
        assert repr(Currency.INR) == "Currency.INR"

    def test_rub(self):
        """
        Make sure the repr function returns the correct string for RUB.
        """
        assert repr(Currency.RUB) == "Currency.RUB"
