from transfermarket.models.club import Club


class TestClubConstructor:
    def test_id(self):
        assert Club(id=1).id == 1

    def test_name(self):
        assert Club(name="test").name == "test"

    def test_total_players(self):
        assert Club(total_players=1).total_players == 1

    def test_avg_age(self):
        assert Club(avg_age=1.0).avg_age == 1.0

    def test_total_foreigners(self):
        assert Club(total_foreigners=1).total_foreigners == 1

    def test_avg_market_value(self):
        assert Club(avg_market_value="1").avg_market_value == "1"

    def test_market_value(self):
        assert Club(market_value="1").market_value == "1"


def test_repr():
    club = Club(
        id=1,
        name="test",
        total_players=1,
        avg_age=1.0,
        total_foreigners=1,
        avg_market_value="1",
        market_value="1",
    )
    assert repr(club) == (
        "Club("
        "id=1, "
        "name='test', "
        "total_players=1, "
        "avg_age=1.0, "
        "total_foreigners=1, "
        "avg_market_value='1', "
        "market_value='1'"
        ")"
    )
