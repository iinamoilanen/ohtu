import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_loytaa_pelaajan(self):
        player = self.stats.search("Yzerman")
        self.assertAlmostEqual(player.name, "Yzerman")

    def test_ei_loyda_pelaajaa(self):
        player = self.stats.search("Kaapo")
        self.assertIsNone(player)

    def test_loytaa_tiimin(self):
        team_players = self.stats.team("DET")
        self.assertAlmostEqual(len(team_players), 1)

    def test_ei_ole_oikea_joukkue(self):
        team_players = self.stats.team("JYP")
        self.assertAlmostEqual(len(team_players), 0)

    def test_pelaajat_jarjestykseen_parhaasta(self):
        top_players = self.stats.top(1)
        self.assertAlmostEqual(top_players[0].name, "Gretzky")

if __name__ == "__main__":
    unittest.main()
