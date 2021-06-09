import logging

logger = logging.getLogger(__name__)


class Player():
    def __init__(self, player_name):
        self.player_name = player_name
        logger.debug('Init: ' + player_name)
        self.player_bet = [None, None]
    
    def get_name(self):
        return self.player_name
    