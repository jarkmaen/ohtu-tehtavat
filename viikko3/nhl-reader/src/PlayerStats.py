class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        filter = []

        for player in self.players:
            if player.nationality == nationality:
                filter.append(player)

        return sorted(filter, key=lambda item: item.points, reverse=True)
