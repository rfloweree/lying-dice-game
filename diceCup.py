from die import Die
import logging

logger = logging.getLogger(__name__)


class DiceCup:
    '''
    '''
    def __init__(self):
        self.dice = [Die(), Die(), Die(), Die(), Die(), Die()]
        logger.debug(self.dice)
        for die in self.dice:
            die.roll()
    
    def peek(self):
        '''
        '''
        return self.dice