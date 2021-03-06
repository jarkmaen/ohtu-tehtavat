import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.get_players(requests.get(self.url).json())

    def get_players(self, response):
        players = []

        for player_dict in response:
            player = Player(
                player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality']
            )
            players.append(player)

        self.players = players
