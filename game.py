from diceCup import DiceCup
from dice_roll import roll_dice
import logging

logger = logging.getLogger(__name__)


class Game:
    def __init__(self, players=None):
        self.profiles = []
        if players is None:
            self.players = []
        else:
            self.players = players
        logger.debug('Init game')
    
    def get_players(self):
        '''Returns the list of players initialized for the game.'''
        return self.players

    def start(self):
        '''go into the Setup Phase'''
        
    def setupPhase(self):
        '''
        Setup Phase of the game.
        This is where the player profiles are created and turn order is determined.
        '''
        logger.debug('Setup Phase')
        for player in self.players:
            dice1, dice2 = roll_dice()
            roll_sum = dice1 + dice2
            logger.debug('Dice Roll Sum: ' + str(roll_sum))
            profile = (player, DiceCup(), roll_sum)
            logger.debug('Create profile for: ' + player.get_name())
            self.profiles.append(profile)
        return True
    
    def bettingPhase(self):
        pass

    def endPhase(self):
        pass

    def get_dice_rolls(self):
        for player in self.players:
            dice1, dice2 = roll_dice()
            roll_sum = dice1 + dice2
        yield roll_sum

def _create_profiles(players):
    for player in players:
        name = player.get_name()
        profile = {
            name: player,
            'dice cup': DiceCup()
        }
    yield profile

class Profile:
    def __init__(self, player):
        self.player_name = player.get_name()
        self.diceCup = DiceCup()
        self.player_bet = [None, None]
        self.turn_roll = None

    def setup(self):
        '''
        Setups the player profile for the start of the game.
        '''
        self.diceCup.roll_dice()
        dice1, dice2 = roll_dice()
        self.turn_roll = dice1 + dice2

    def getPlayerName(self):
        return self.player_name

    def getPlayerBet(self):
        return self.player_bet
    
    def getTurnRoll(self):
        '''
        Gets the value of the turn roll for the player.
        This will be used to determine the starting player.
        '''
        return self.turn_roll

# class Phase:
#     def __init__(self, name):
#         self.name = name

#     def run():
#         pass


# class Setup(Phase):
#     def __init__(self, name):
#         super().__init__(name)

#     def run():
#         print('Run ' + self.name + ' phase')


# class Betting(Phase):
#     def __init__(self, name):
#         super().__init__(name)

#     def run():
#         print('Run ' + self.name + ' phase')


# class End(Phase):
#     def __init__(self, name):
#         super().__init__(name)

#     def run():
#         print('Run ' + self.name + ' phase')

def main():
    game = Game()
    if game.setupPhase():
        '''go to the Betting phase'''
        state = game.bettingPhase()
        if state == 'end_phase':
            game.endPhase()


if __name__ == '__main__':
    main()