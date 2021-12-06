class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.tied_score(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.deuce(self.m_score1 - self.m_score2)
        else:
            return self.score_calling(self.m_score1) + "-" + self.score_calling(self.m_score2)

    def tied_score(self, score):
        if score > 3:
            return "Deuce"
        else:
            return self.score_calling(score) + "-All"

    def deuce(self, difference):
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def score_calling(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
