import logging

logger = logging.getLogger(__name__)


class Game:
    def __init__(self, players):
        self.players = players
        logger.debug('Init game')
    
    def start(self):
        pass