from transfermarket.models.meta import MetaProperty
from transfermarket.models.team import Team


class TestTeamConstructor:
    def test_id(self):
        team = Team(id="test")
        assert team.id == "test"

    def test_title(self):
        team = Team(title="test")
        assert team.title == "test"

    def test_abbreviation(self):
        team = Team(abbreviation="test")
        assert team.abbreviation == "test"

    def test_meta(self):
        team = Team(meta=[MetaProperty(name="test", value="value")])
        assert team.meta == [MetaProperty(name="test", value="value")]


def test_repr():
    team = Team(id="test", title="test")
    assert repr(team) == "<Team(id='test', title='test')>"
