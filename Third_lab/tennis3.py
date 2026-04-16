class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        """
        Initialize game.
        
        p1 = points of player 1
        p2 = points of player 2
        """
        self.p1_n = player1_name
        self.p2_n = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        """
        Add a point to the given player.
        """
        if n == "player1":
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        """
        Return current score.
        """
        if self._is_normal_game():
            return self._normal_score()

        if self.p1 == self.p2:
            return "Deuce"

        return self._end_game_score()

    def _is_normal_game(self):
        """
        Check normal phase of the game.
        """
        return self.p1 < 4 and self.p2 < 4 and (self.p1 + self.p2 < 6)

    def _normal_score(self):
        """
        Score during normal play.
        """
        if self.p1 == self.p2:
            return f"{self.SCORE_NAMES[self.p1]}-All"
        return f"{self.SCORE_NAMES[self.p1]}-{self.SCORE_NAMES[self.p2]}"

    def _end_game_score(self):
        """
        Return score for advantage or win situations.
        """
        winner = self.p1_n if self.p1 > self.p2 else self.p2_n

        if abs(self.p1 - self.p2) == 1:
            return f"Advantage {winner}"
        return f"Win for {winner}"
