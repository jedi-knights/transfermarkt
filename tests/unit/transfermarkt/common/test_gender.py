import pytest

from transfermarkt.common.gender import Gender, string_to_gender


def test_male_repr():
    assert repr(Gender.Male) == "male"


def test_female_repr():
    assert repr(Gender.Female) == "female"


def test_male_str():
    assert str(Gender.Male) == "male"


def test_female_str():
    assert str(Gender.Female) == "female"


class TestStringToGender:
    def test_none(self):
        """
        Make sure it raises a ValueError
        """
        with pytest.raises(ValueError, match="Undefined gender string!"):
            string_to_gender(None)

    def test_empty(self):
        """
        Make sure it raises a ValueError
        """
        with pytest.raises(ValueError, match="Empty gender string!"):
            string_to_gender("")

    def test_spaces(self):
        """
        Make sure it raises a ValueError
        """
        with pytest.raises(ValueError, match="Empty gender string!"):
            string_to_gender("     ")

    def test_all(self):
        """
        Ensure the string_to_gender function returns Gender.All when given "all"
        """
        assert string_to_gender("all") == Gender.All

    def test_m(self):
        """
        Ensure the string_to_gender function returns Gender.Male when given "m".
        """
        assert string_to_gender("m") == Gender.Male

    def test_male(self):
        """
        Ensure the string_to_gender function returns Gender.Male when given "male".
        """
        assert string_to_gender("male") == Gender.Male

    def test_male_uppercase(self):
        """
        Ensure the string_to_gender function returns Gender.Male when given "MALE".
        """
        assert string_to_gender("MALE") == Gender.Male

    def test_male_with_spaces(self):
        """
        Ensure the string_to_gender function returns Gender.Male when given "   male  "
        """
        assert string_to_gender("  male ") == Gender.Male

    def test_f(self):
        """
        Ensure the string_to_gender function returns Gender.Female when given "f".
        """
        assert string_to_gender("f") == Gender.Female

    def test_female(self):
        """
        Ensure the string_to_gender function returns Gender.Female when given "female".
        """
        assert string_to_gender("female") == Gender.Female

    def test_invalid(self):
        """
        Ensure the string_to_gender function raises a ValueError when given "whatever".
        """
        with pytest.raises(ValueError, match="Invalid gender string 'whatever'!"):
            string_to_gender("whatever")
