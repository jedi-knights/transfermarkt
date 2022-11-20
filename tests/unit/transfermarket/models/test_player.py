import pytest

from transfermarket.common.gender import Gender
from transfermarket.models.player import Player


@pytest.fixture
def player():
    return Player(
        id=1,
        gender=Gender.Female,
        first_name="Wilma",
        last_name="Flintstone",
        club="Bedrock",
        state="CA",
        position="Forward",
    )


class TestPlayerConstructor:
    def test_id(self):
        """
        Tests that the id property is set.
        """
        player = Player(id="test")
        assert player.id == "test"

    def test_gender_female(self):
        """
        Tests that the gender property is set when the gender is Gender.Female.
        """
        player = Player(gender=Gender.Female)
        assert player.gender == Gender.Female

    def test_gender_male(self):
        """
        Tests that the gender property is set when the gender is Gender.Male.
        """
        player = Player(gender=Gender.Male)
        assert player.gender == Gender.Male

    def test_first_name(self):
        """
        Tests that the first_name property is set.
        """
        player = Player(first_name="test")
        assert player.first_name == "test"

    def test_last_name(self):
        """
        Tests that the last_name property is set.
        """
        player = Player(last_name="test")
        assert player.last_name == "test"

    def test_club(self):
        """
        Tests that the club property is set.
        """
        player = Player(club="test")
        assert player.club == "test"

    def test_state(self):
        """
        Tests that the state property is set.
        """
        player = Player(state="test")
        assert player.state == "test"

    def test_position(self):
        """
        Tests that the position property is set.
        """
        player = Player(position="test")
        assert player.position == "test"


def test_name(player):
    """
    Tests that the name property returns the first and last name.
    """
    assert player.name == "Wilma Flintstone"


def test_name_setter_1(player):
    """
    Test that the name setter works as expected with a single name
    """
    player.name = "Betty"
    assert player.first_name == "Betty"
    assert player.last_name is None


def test_name_setter_2(player):
    """
    Test that the name setter works as expected with a first and last name.
    """
    player.name = "Fred Flintstone"
    assert player.first_name == "Fred"
    assert player.last_name == "Flintstone"


def test_name_setter_3(player):
    """
    Test that the name setter works as expected with a first, middle, and last name.
    """
    player.name = "Barney Tiberius Rubble"
    assert player.first_name == "Barney"
    assert player.last_name == "Rubble"


def test_year_from_grad_year(player):
    """
    Tests that the graduation year can be retrieved from meta data.
    """
    player.add_property("grad_year", "2021")

    assert player.year == "2021"


def test_year_from_graduation_year(player):
    """
    Tests that the graduation year can be retrieved from meta data.
    """
    player.add_property("graduation_year", "2021")

    assert player.year == "2021"


def test_commitment_from_commitment(player):
    """
    Tests that the commitment can be retrieved from meta data.
    """
    player.add_property("commitment", "test")

    assert player.commitment == "test"


def test_commitment_from_college_team(player):
    """
    Tests that the commitment can be retrieved from meta data.
    """
    player.add_property("college_team", "test")

    assert player.commitment == "test"


def test_commitment_with_women_suffix(player):
    """
    Tests that the commitment property removes the substring " Women" from the college team.
    """
    player.add_property("college_team", "Bedrock Women")
    assert player.commitment == "Bedrock"


def test_commitment_with_men_suffix(player):
    """
    Tests that the commitment property removes the substring " Men" from the college team.
    """
    player.add_property("college_team", "Bedrock Men")
    assert player.commitment == "Bedrock"


def test_committed_true(player):
    """
    Tests that committed returns true when the player has a commitment.
    """
    player.add_property("commitment", "test")

    assert player.is_committed


def test_committed_false(player):
    """
    Tests that committed returns false when the player does not have a commitment.
    """
    assert not player.is_committed


def test_repr(player):
    """
    Tests that the repr method returns the expected string.
    """
    assert (
        repr(player)
        == "<Player(id='1', name='Wilma Flintstone', gender='Female', state='CA', position='Forward', club='Bedrock')>"
    )


def test_repr_with_grad_year(player):
    """
    Tests that the repr method returns the expected string.
    """
    expected = "<Player(id='1', name='Wilma Flintstone', year='2021', gender='Female',"
    expected += " state='CA', position='Forward', club='Bedrock')>"
    player.add_property("grad_year", "2021")
    assert repr(player) == expected


def test_repr_committed(player):
    """
    Tests that the repr method returns the expected string.
    """
    expected = "<Player(id='1', name='Wilma Flintstone', gender='Female', state='CA',"
    expected += " position='Forward', club='Bedrock', commitment='test')>"
    player.add_property("commitment", "test")
    assert repr(player) == expected


def test_repr_with_string_gender(player):
    """
    Tests that the repr method returns the expected string.
    """
    expected = "<Player(id='1', name='Wilma Flintstone', gender='female', state='CA',"
    expected += " position='Forward', club='Bedrock')>"

    player.gender = "female"
    assert repr(player) == expected
