from diceCup import DiceCup
from unittest import mock
from unittest import TestCase


class TestDiceCup(TestCase):
    def setUp(self):
        self.diceCup = DiceCup()
    
    def tearDown(self):
        pass

    @mock.patch('diceCup.roll_dice_poly', return_value=3, autospec=True)
    def test_roll_dice(self, mock_roll_dice_poly):
        self.diceCup.roll_dice()
        mock_roll_dice_poly.assert_called_with(6, 5)

    def test_peek(self):
        self.assertEqual(self.diceCup.peek(), None)