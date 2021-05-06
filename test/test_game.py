from game import Game
from player import Player
from unittest import TestCase


class TestGame(TestCase):
    def setUp(self):
        players = [Player("Alice"),
                    Player("Bob"),
                    Player("Cara")]
        self.game = Game(players)

    def tearDown(self):
        pass

    def test_start(self):
        self.game.start()
