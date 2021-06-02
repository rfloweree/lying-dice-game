from random import seed
from random import choice
import logging

logger = logging.getLogger(__name__)

seed()
faces =[1, 2, 3, 4, 5, 6]

def roll_Die():
    return choice(faces)

def roll_dice():
    return (choice(faces), choice(faces))