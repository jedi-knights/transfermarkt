from transfermarkt.models.competition import Competition


class TestCompetitionConstructor:
    def test_id(self):
        assert Competition(id=1).id == 1

    def test_name(self):
        assert Competition(name="test").name == "test"

    def test_country(self):
        assert Competition(country="test").country == "test"

    def test_total_clubs(self):
        assert Competition(total_clubs=1).total_clubs == 1

    def test_total_players(self):
        assert Competition(total_players=1).total_players == 1

    def test_avg_age(self):
        assert Competition(avg_age=1.0).avg_age == 1.0

    def test_foreigners_percent(self):
        assert Competition(foreigners_percent=1.0).foreigners_percent == 1.0

    def test_total_value(self):
        assert Competition(total_value="test").total_value == "test"

    def test_tier(self):
        assert Competition(tier="test").tier == "test"


def test_repr():
    competition = Competition(
        id=1,
        name="test",
        country="test",
        total_clubs=1,
        total_players=1,
        avg_age=1.0,
        foreigners_percent=1.0,
        total_value="test",
        tier="test",
    )
    assert repr(competition) == (
        "Competition("
        "id='1', "
        "name='test', "
        "country='test', "
        "total_clubs=1, "
        "total_players=1, "
        "avg_age=1.0, "
        "foreigners_percent=1.0, "
        "total_value='test', "
        "tier='test'"
        ")"
    )
