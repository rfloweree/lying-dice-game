from unittest import mock
from unittest import TestCase
import dice_roll


class TestDice_Roll(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('dice_roll.choice', return_value=3, autospec=True)
    def test_roll_dice(self, mock_choice):
        self.assertEqual(dice_roll.roll_Die(), 3)
        mock_choice.assert_called_with([1, 2, 3, 4, 5, 6])
