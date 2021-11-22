class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}" + self.team + " " + str(self.goals) + " + " + str(self.assists) + " = " + str(self.points)
