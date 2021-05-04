from diceCup import DiceCup
from unittest import mock
from unittest import TestCase


class TestDiceCup(TestCase):

    @mock.patch('die.choice', return_value=3, autospec=True)
    def setUp(self):
        self.diceCup = DiceCup()
    
    def tearDown(self):
        pass

    def test_peek(self):
        self.assertEqual(self.diceCup.peek(), '3 3 3 3 3')