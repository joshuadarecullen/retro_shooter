from base import *
from heathbar import HealthBar
from weapon import Weapon

# inherit from the abstract class Agent, check it out
# allows for less rep
class Player(Agent):

    def __init__(self, x, y, position, width, height, game_width, game_height, game, lives=5):
        super().__init__(x,y,position) # super is the parent of Player: Agent, we have inherited x, y and theta as attributes for use in this class.

        # physical characteristics of the player
        self.width = width
        self.height = height
        self.velocity = velocity
        self.hitbox = (self.x, self.y, self.width, self.height)

        # game object itself and its characteristics
        self.game = game
        self.game_width = game_width
        self.game_height = game_height

        # states and stats
        self.standing = True
        self.lives = lives

        # additional objects
        self.health_bar = HealthBar(self, self.game)
        self.weapon = None


    def step(self):
        pass


    def player_drawing(self):
        pass


    def initialise_respawn(self, x, y):
        self.x = x
        self.y = y
        self.heathbar.reset_health()
