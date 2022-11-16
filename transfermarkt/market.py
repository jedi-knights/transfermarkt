from transfermarkt.page.competitions import CompetitionsPage

# from transfermarkt.common.gender import Gender
# from transfermarkt.common.model.player import Player
# from transfermarkt.common.model.team import Team
# from transfermarkt.common.utils import urljoin
from transfermarkt.services.market import MarketService


class Market:
    def __init__(self, **kwargs):
        pass

    def get_competitions(self):
        return CompetitionsPage().get_competitions()

    def teams(self, competition_id):
        pass


if __name__ == "__main__":
    service = MarketService()

    competition_count = 0
    team_count = 0
    player_count = 0
    competitions = CompetitionsPage.get_all_competitions()
    for competition in competitions:
        try:
            competition_count += 1
            print(competition)

            teams = service.get_teams(identifier=competition.id)
            for team in teams:
                team_count += 1
                print(f"\t{team}")

                players = service.get_players(identifier=team.id)
                for player in players:
                    player_count += 1
                    print(f"\t\t{player}")
        except Exception as e:
            print(e)

    print(f"Competitions: {competition_count}")
    print(f"Teams: {team_count}")
    print(f"Players: {player_count}")
