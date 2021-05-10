import logging

logger = logging.getLogger(__name__)


class Die:
    '''
    Object that represents a six-sided die used in the game.
    '''
    def __init__(self):
        self.face_up = None
        logger.debug('Init: ' + str(self.face_up))

    def get_face_up(self):
        '''
        Gets the value showing on the face up on the die.
        '''
        return self.face_up

    def roll(self, new_face):
        '''
        Rerolls the die. Sets a new random value for the die side facing up. 
        '''
        self.face_up = new_face
        logger.debug('Roll: ' + str(new_face))