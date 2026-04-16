class TennisGame2:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        """
        Initialize game.
        
        p1 = points of player 1
        p2 = points of player 2
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
        Add a point to the current player.
        """
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        """
        Return current score
        """
        if self.p1points == self.p2points:
            return self._equal_score()

        if self.p1points >= 4 or self.p2points >= 4:
            return self._endgame_score()

        return f"{self._score_name(self.p1points)}-{self._score_name(self.p2points)}"

    def _equal_score(self):
        if self.p1points < 3:
            return f"{self._score_name(self.p1points)}-All"
        return "Deuce"

    def _endgame_score(self):
        diff = self.p1points - self.p2points

        if diff == 1:
            return "Advantage player1"
        if diff == -1:
            return "Advantage player2"
        if diff >= 2:
            return "Win for player1"
        return "Win for player2"

    def _score_name(self, points):
        return self.SCORES[points]