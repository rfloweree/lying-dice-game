from die import Die
from unittest import mock
from unittest import TestCase

class TestDie(TestCase):
    def setUp(self):
        self.die = Die()
    
    def tearDown(self):
        pass

    def test_get_face_up(self):
        self.assertEqual(self.die.get_face_up(), None)
    
    def test_roll(self):
        self.die.roll(3)
        self.assertEqual(self.die.get_face_up(), 3)
        