#from die import Die
from dice_roll import roll_Die
from dice_roll import roll_dice_poly
import logging

logger = logging.getLogger(__name__)


class DiceCup:
    '''
    The Dice Cup object. Each player has one Dice Cup throughout the game.
    This is an object that holds 5 dice and is meant to hide the results
    from the players and allow the owner to peek.
    '''
    def __init__(self):
        self.dice = None
        logger.debug(self.dice)
    
    def roll_dice(self):
        '''
        This will roll all the dice in the cup and reset the values facing up.
        This is only done at the start of the game.
        '''
        self.dice = roll_dice_poly(6, 5)

    def peek(self):
        '''
        Look at the dice under the cup. Returns the array of dice faces.
        '''
        return self.dice

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