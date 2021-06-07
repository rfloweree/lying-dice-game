from random import seed
from random import choice
import logging

logger = logging.getLogger(__name__)

seed()
faces = [1, 2, 3, 4, 5, 6]

def roll_Die():
    '''
    Rolls a single six-sided die.
    Returns the integer value of thh side facing up.
    '''
    return choice(faces)

def roll_dice():
    '''
    Rolls two six-sided dice.
    Returns a tuple of the integer value of the side facing up for each die.
    '''
    return (choice(faces), choice(faces))

def roll_dice_poly(number_faces, number_dice):
    '''
    Rolls a given number of n-sided dice. 
    Returns a list of the integer value of the side facing up for each die.
    '''
    dice_faces = []
    dice_rolls = []
    for num in range(1, number_faces+1):
        dice_faces.append(num)
    for dice in  range(number_dice):
        dice_rolls.append(choice(dice_faces))
    return dice_rolls