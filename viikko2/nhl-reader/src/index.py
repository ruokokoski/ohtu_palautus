from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()
    console.print("NHL statistics by nationality\n", style="italic")
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    season = Prompt.ask("Select season: ", choices=seasons)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.get_all_nats()
    nationalities.append("quit")
    while True:
        nationality = Prompt.ask("\nSelect nationality: ", choices=nationalities)
        if nationality == "quit":
            break
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top Scorers of {nationality} season {season}")
        table.add_column("Name", justify="left", style="yellow")
        table.add_column("Team", justify="center", style="cyan")
        table.add_column("Goals", justify="center", style="green")
        table.add_column("Assists", justify="center", style="green")
        table.add_column("Points", justify="center", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))

        console.print(table)
    
if __name__ == "__main__":
    main()
