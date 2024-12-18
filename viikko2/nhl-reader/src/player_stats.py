class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        return sorted(
            [player for player in self.players if player.nationality == nationality],
            key=lambda p: p.goals + p.assists,
            reverse=True
        )
    
    def get_all_nats(self):
        nats = {player.nationality for player in self.players}
        return list(nats)

    def __str__(self):
        return f"PlayerStats"
