from dataclasses import dataclass


@dataclass
class Competition:
    id: str
    name: str
    country: str
    total_clubs: int
    total_players: int
    avg_age: float
    foreigners_percent: float
    total_value: str
    tier: str

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.country = kwargs.get("country")
        self.total_clubs = kwargs.get("total_clubs")
        self.total_players = kwargs.get("total_players")
        self.avg_age = kwargs.get("avg_age")
        self.foreigners_percent = kwargs.get("foreigners_percent")
        self.total_value = kwargs.get("total_value")
        self.tier = kwargs.get("tier")

    def __repr__(self):
        return f"Competition(id='{self.id}', name='{self.name}', country='{self.country}', total_clubs={self.total_clubs}, total_players={self.total_players}, avg_age={self.avg_age}, foreigners_percent={self.foreigners_percent}, total_value='{self.total_value}' tier='{self.tier}')"
