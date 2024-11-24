class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    WIN_THRESHOLD = 4
    ADVANTAGE_PLAYER1 = 1
    ADVANTAGE_PLAYER2 = -1
    WIN_PLAYER1 = 2
    WIN_PLAYER2 = -2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = self.LOVE
        self.player2_score = self.LOVE

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._score_is_tied()
        if self.player1_score >= self.WIN_THRESHOLD or self.player2_score >= self.WIN_THRESHOLD:
            return self._winner_or_advantage()
        return self._score_is_normal()
    
    def _score_is_tied(self):
        score_mapping = {self.LOVE: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        return score_mapping.get(self.player1_score, "Deuce")
    
    def _score_is_normal(self):
        score_mapping = {self.LOVE: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return f"{score_mapping[self.player1_score]}-{score_mapping[self.player2_score]}"
    
    def _winner_or_advantage(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == self.ADVANTAGE_PLAYER1:
            return f"Advantage {self.player1_name}"
        elif score_difference == self.ADVANTAGE_PLAYER2:
            return f"Advantage {self.player2_name}"
        elif score_difference >= self.WIN_PLAYER1:
            return f"Win for {self.player1_name}"
        elif score_difference <= self.WIN_PLAYER2:
            return f"Win for {self.player2_name}"
