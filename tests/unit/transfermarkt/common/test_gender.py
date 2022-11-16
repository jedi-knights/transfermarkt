import pytest

from transfermarkt.common.gender import Gender, string_to_gender


def test_male_repr():
    assert repr(Gender.Male) == "male"


def test_female_repr():
    assert repr(Gender.Female) =="female"


def test_male_str():
    assert str(Gender.Male) == "male"


def test_female_str():
    assert str(Gender.Female) == "female"


class TestStringToGender:
    def test_none(self):
        with pytest.raises(ValueError, match="Undefined gender string!"):
            string_to_gender(None)

    def test_empty(self):
        with pytest.raises(ValueError, match="Empty gender string!"):
            string_to_gender("")

    def test_spaces(self):
        with pytest.raises(ValueError, match="Empty gender string!"):
            string_to_gender("     ")

    def test_all(self):
        assert string_to_gender("all") == Gender.All

    def test_m(self):
        assert string_to_gender("m") == Gender.Male

    def test_male(self):
        assert string_to_gender("male") == Gender.Male

    def test_male_uppercase(self):
        assert string_to_gender("MALE") == Gender.Male

    def test_male_with_spaces(self):
        assert string_to_gender("  male ") == Gender.Male

    def test_f(self):
        assert string_to_gender("f") == Gender.Female

    def test_female(self):
        assert string_to_gender("female") == Gender.Female

    def test_invalid(self):
        with pytest.raises(ValueError, match="Invalid gender string 'whatever'!"):
            string_to_gender("whatever")
