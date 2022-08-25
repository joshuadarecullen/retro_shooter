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

        # images for changing direction of the character
        self.walk_right = []
        self.walk_left = []


    # the function that will handle the users keyboard input
    def step(self):

        if keys[pygame.K_DOWN] and self.weapon:
            drop_thread = Thread(target=self.weapon.drop, daemon=True)
            drop_thread.start()
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
            self.left, self.right, self.standing = True, False, False
            if self.weapon:
                self.weapon.left, self.weapon.right = True, False
        elif keys[pygame.K_RIGHT]:
            self.x += self.velocity
            self.left, self.right, self.standing = False, True, False
            if self.weapon:
                self.weapon.left, self.weapon.right = False, True
        else:
            self.standing, self.walk_count = True, 0


    # drawing the new position of the player
    def player_drawing(self, width, height, x_add=False, y_add=False):

        if x_add:
            temp = self.x + x_add
            if temp < width and temp > -width:
                self.x += x_add

        if y_add:
            temp = self.y + y_add
            if temp < height and temp > -height:
                self.y += y_add


    def initialise_respawn(self, x, y):
        self.x = x
        self.y = y
        self.heathbar.reset_health()

### get methods for fetching players variable and states
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_position(self):
        return self.theta

    def get_health(self):
        pass

    def get_player_data(self):
        pass
