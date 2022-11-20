import os

from transfermarket.market import Market

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