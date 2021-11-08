import unittest
from statistics import Statistics
from player import Player
from player_reader import PlayerReader


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_konstruktori_luo_pelaajalistan(self):
        self.assertEqual(len(self.statistics._players), 5)

    def test_pelaajahaku_palauttaa_oikean_pelaajan(self):
        viides_pelaaja = self.statistics._players[4]
        haku = self.statistics.search("Gretzky")
        self.assertEqual(viides_pelaaja, haku)

    def test_haku_palauttaa_tyhjaa_jos_pelaajaa_ei_loydy(self):
        self.assertIsNone(self.statistics.search("Testi"))

    def test_joukkuehaku_palauttaa_saman_joukkueen_pelaajat(self):
        haku = self.statistics.team("EDM")
        self.assertEqual(len(haku), 3)

    def test_top_scores_palauttaa_oikeassa_jarjestyksessa(self):
        lista = self.statistics.top_scorers(4)
        self.assertEqual("Gretzky", lista[0].name)
        self.assertEqual("Lemieux", lista[1].name)
        self.assertEqual("Yzerman", lista[2].name)
        self.assertEqual("Kurri", lista[3].name)
        self.assertEqual("Semenko", lista[4].name)
