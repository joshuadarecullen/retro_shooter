from base import *

# inherit from the abstract class Agent, check it out
# allows for less rep
class Player(Agent):
    def __init__(self, x, y, theta):
        super().__init__(x,y,theta) # super is the parent of Player: Agent, we have inherited x, y and theta as attributes for use in this class.
    def player_draw(self):
        pass
