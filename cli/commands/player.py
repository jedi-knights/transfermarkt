import click

from transfermarket.market import Market

@click.group()
def cli():
    """Interact with player data"""
    pass


@cli.command("list")
@click.argument("team_id")
def list_players(team_id):
    """List all players for a given team."""
    market = Market()
    players = market.get_players(team_id)

    for player in players:
        click.echo(player)
