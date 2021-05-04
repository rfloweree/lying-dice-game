from random import seed
from random import choice
import logging

logger = logging.getLogger(__name__)

seed()

faces = [1, 2, 3, 4, 5, 6]


class Die:
    def __init__(self):
        self.face_up = None
        logger.debug('Init: ' + str(self.face_up))

    def get_face_up(self):
        '''
        Gets the value showing on the face up on the die.
        '''
        return self.face_up

    def roll(self):
        '''
        Rerolls the die. Sets a new random value for the die side facing up. 
        '''
        self.face_up = choice(faces)
        logger.debug('Roll: ' + str(self.face_up))