from base import *
from heathbar import HealthBar
from weapon import Weapon

# inherit from the abstract class Agent, check it out
# allows for less rep
class Player(Agent):

    def __init__(self, x, y, position, width, height, game_width, game_height, game, lives=5):
        super().__init__(x,y,position) # super is the parent of Player: Agent, we have inherited x, y and theta as attributes for use in this class.
        self.width = width
        self.height = height
        self.velocity = velocity
        self.game_width = game_width
        self.game_height = game_height

        self.standing = True
        self.lives = lives
        self.health_bar = HealthBar()
        self.weapon = Weapon()
        self.hitbox = (self.x, self.y, self.width, self.height)

    def step(self):
        pass

    def player_drawing(self):
        pass
