from base import *
from healthbar import HealthBar
from weapon import Weapon

# inherit from the abstract class Agent, check it out
# allows for less rep
class Player(Agent):

    def __init__(self, x, y, position, width, height, velocity, game_width, game_height, game, lives=5):
        super().__init__(x, y, position) # super is the parent of Player: Agent, we have inherited x, y and theta as attributes for use in this class.

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

        self.actions = {'Left': False, 'Right': False, 'Down': False, 'Up': False}


    ''' The function that will handle the users keyboard input, and set the 
        current move state to true '''
    def step(self, keys):

        if keys[pygame.K_DOWN]:
            self.y -= self.velocity
            self.set_state(flag=1)

        elif keys[pygame.K_LEFT]:
            self.x -= self.velocity
            self.set_state(flag=2)

        elif keys[pygame.K_RIGHT]:
            self.x += self.velocity
            self.set_state(flag=3)

        elif keys[pygame.K_UP]:
            self.y += self.velocity
            self.set_state(flag=4)

        else:
            self.standing = True


    # set the current state of the players action
    def set_state(self, flag):

        if flag == 1:
            self.up, self.right, self.left, self.down, self.standing = False, False, False, True, False
        elif flag == 2:
            self.up, self.right, self.left, self.down, self.standing = False, False, True, False, False
        elif flag == 3:
            self.up, self.right, self.left, self.down, self.standing = False, True, False, False, False
        elif flag == 4:
            self.up, self.right, self.left, self.down, self.standing = True, False, False, False, False


    # drawing the new position of the player
    def draw(self, width, height):

        # check we are not standing
        if not self.standing:
            # these two if states check whether we are within the bounds
            temp = self.x + x_add
            if temp < width and temp > -width:
                self.x += x_add
                window.blit(self.walk_left[0], (self.x, self.y))

            temp = self.y + y_add
            if temp < height and temp > -height:
                self.y += y_add
                window.blit(self.walk_left[0], (self.x, self.y))

        else:
            pass

        self.hitbox = (self.x, self.y, self.width, self.height)


    # reset the spawn
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
