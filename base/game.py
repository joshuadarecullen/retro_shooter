from player import * # importing from PLayer.py everything
import pygame


# Class for the managing of the game and application
class Game:

    # this is important, this classes initialisation function
    # sets up the attributes in the class and gives them initial values
    def __init__(self, width, height, position=None):
        self.initialise_game()
        self.window = pygame.display.set_mode((width, height)) # set window
        self.background = pygame.image.load('./images/backgrounds/menus/StartBackground.jpg') # background
        self.clock = pygame.time.Clock() # useful to keep track of time for in game stats
        self.running = True #  for main hyper-loop keeping the application running
        self.endgame = False
        self.user_player = Player(width, height, position) # inital the Player class

    # Here we initialise pygame and the window
    def initialise_game(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Game")
        # pygame.display.set_num_channels(8)

    # redraw what the user will be seeing
    def redraw_window(self, window, background):

        # set background
        window.blit(background, (0,0))

        # redraw the player in new state
        self.user_player.player_drawing(window)

    def respawn_player(self, player):
        pass

    # running the game itself
    def run(self):

        while self.running:

            print('runnin')

            if self.endgame:
                self.running = False

            # self.endgame = True
