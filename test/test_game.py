from game import Game
from game import Profile
from player import Player
from unittest import mock
from unittest import TestCase
import game

class TestGame(TestCase):
    def setUp(self):
        players = [Player("Alice"),
                    Player("Bob"),
                    Player("Cara")]
        self.game = Game(players)

    def tearDown(self):
        pass

    def test_start(self):
        pass
        # self.game.start()
        # self.assertEqual(self.game.profiles[0][0].get_name(), "Alice")

    # def test_dice_rolls(self):
    #     print(list(self.game.get_dice_rolls()))

    def test_game_main(self):
        game.main()

class TestProfile(TestCase):
    def setUp(self):
        player = Player("Alice")
        self.profile = Profile(player)

    def tearDown(self):
        pass

    def test_getPlayerName(self):
        self.assertEqual(self.profile.getPlayerName(), 'Alice')
    
    def test_getPlayerbet(self):
        self.assertEqual(self.profile.getPlayerBet(), [None, None])

    def test_getTurnRoll(self):
        self.assertEqual(self.profile.getTurnRoll(), None)

    @mock.patch('game.Profile.setup.roll_dice_poly', return_value=3, autospec=True)
    def test_setup(self, mock_roll_dice_poly):
        self.profile.setup()
        mock_roll_dice_poly.assert_called_with(6, 5)