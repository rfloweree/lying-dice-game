from die import Die
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
        for die in self.dice:
            die.roll()
    
    def peek(self):
        '''
        Look at the dice under the cup. Returns the array of dice faces.
        '''
        return self.dice