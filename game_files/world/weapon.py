from base import *

class Weapon(Agent):
    def __init__(self, player):
        self.player = player
        self.x = player.x
        self.y = player.y

        super().__init__(player.x, player.y, player.position)

    def step(self):
        pass

    def draw(self):
        pass

        
