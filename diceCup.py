from die import Die
from dice_roll import roll_Die
import logging

logger = logging.getLogger(__name__)


class DiceCup:
    '''
    The Dice Cup object. Each player has one Dice Cup throughout the game.
    This is an object that holds 5 dice and is meant to hide the results
    from the players and allow the owner to peek.
    '''
    def __init__(self):
        self.dice = [Die(), Die(), Die(), Die(), Die()]
        logger.debug(self.dice)
    
    def roll_dice(self):
        for die in self.dice:
            die.roll(roll_Die())

    def peek(self):
        '''
        Look at the dice under the cup. Returns the array of dice faces.
        '''
        return [self.dice[0].get_face_up(),
                self.dice[1].get_face_up(),
                self.dice[2].get_face_up(),
                self.dice[3].get_face_up(),
                self.dice[4].get_face_up()]