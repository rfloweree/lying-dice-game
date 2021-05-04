from die import Die
from unittest import mock
from unittest import TestCase

class TestDie(TestCase):
    def setUp(self):
        self.die = Die()
    
    def tearDown(self):
        pass

    def test_get_face_up(self):
        print('test_get_face_up')
        self.assertEqual(self.die.get_face_up(), None)
    
    @mock.patch('die.choice', return_value=3, autospec=True)
    def test_roll(self, mock_choice):
        print('test_roll')
        self.die.roll()
        mock_choice.assert_called_with([1, 2, 3, 4, 5, 6])
        