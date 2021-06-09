from player import Player
from unittest import TestCase


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Alice")
    
    def tearDown(self):
        pass

    def test_get_name(self):
        self.assertEqual(self.player.get_name(), 'Alice')
        