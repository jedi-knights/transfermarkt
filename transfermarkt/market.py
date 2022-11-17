"""
This module contains the main entry point for the package.
"""

import os

from transfermarkt.page.competitions import CompetitionsPage

# from transfermarkt.common.gender import Gender
# from transfermarkt.common.model.player import Player
# from transfermarkt.common.model.team import Team
# from transfermarkt.common.utils import urljoin
from transfermarkt.services.market import MarketService


class Market:
    """
    This class contains the main interface into the Transfermarkt package.
    """

    def __init__(self, **kwargs):
        self.market_service = kwargs.get("market_service", MarketService())
        self.competitions_page = kwargs.get("competitions_page", CompetitionsPage())

    def get_competitions(self):
        """
        Returns a list of competitions.
        """
        return self.competitions_page.get_competitions()

    def get_teams(self, competition_id: str):
        """
        Returns a list of teams for a given competition.
        """
        return self.market_service.get_teams(competition_id)

    def get_players(self, team_id: str):
        """
        Returns a list of players for a given team.
        """
        return self.market_service.get_players(team_id)


if __name__ == "__main__":
    market = Market()

    competition_count = 0
    team_count = 0
    player_count = 0
    competitions = market.get_competitions()

    if os.path.isfile("output.txt"):
        os.remove("output.txt")

    with open("output.txt", "w") as f:
        for competition in competitions:
            try:
                competition_count += 1
                print(competition)
                f.write(f"{competition}\n")

                teams = market.get_teams(competition.id)
                for team in teams:
                    team_count += 1
                    print(f"\t{team}")
                    f.write(f"\t{team}\n")

                    players = market.get_players(team.id)
                    for player in players:
                        player_count += 1
                        f.write(f"\t\t{player}\n")

                    f.write("\n")

                f.write("\n")
            except ValueError as e:
                print(e)

    print(f"Competitions: {competition_count}")
    print(f"Teams: {team_count}")
    print(f"Players: {player_count}")
