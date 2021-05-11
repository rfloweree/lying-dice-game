from player import Player
from unittest import TestCase


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Alice")
    
    def tearDown(self):
        pass

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), 'Alice')
    
    def test_get_bet(self):
        self.assertEqual(self.player.get_bet(), [None, None])

    def test_set_bet(self):
        self.player.set_bet([5, 5])
        self.assertEqual(self.player.get_bet(), [5, 5])
