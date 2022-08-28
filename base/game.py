from player import * # importing from PLayer.py everything
import pygame


# Class for the managing of the game and application
class Game:

    # this is important, this classes initialisation function
    # sets up the attributes in the class and gives them initial values
    def __init__(self, width, height, position=None):

        self.clock = pygame.time.Clock() # useful to keep track of time for in game stats
        self.main_running = True #  for main hyper-loop keeping the application running
        self.endgame = False

        # window variables
        self.width = width
        self.height = height
        self.background = None

        # agents within the game player and computer
        self.user_player = None


    # Here we initialise pygame and the window
    def initialise_game(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Game")
        pygame.display.set_num_channels(8)


    # redraw what the user will be seeing
    def redraw_window(self, window, background):

        # set background
        window.blit(background, (0,0))

        # redraw the player in new state
        self.user_player.player_drawing(window)


    def respawn_player(self, player):
        pass


    def initialise_real_game(self):
        self.window = pygame.display.set_mode((self.width, self.height)) # set window
        self.background = pygame.image.load('./images/backgrounds/menus/InGameBackground.jpg') # background
        self.player.initialise_respawn() # set to the start position
        self.redraw_window(self.window)


    # running the game itself
    def run(self, player):

        self.user_player = player 
        self.initialise_real_game()

        # TODO: initialise the computer enemies

        while self.main_running:

            if self.endgame:
                self.main_running = False

            # pygame events that indicate the exiting of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == 2 and event.dict['key'] == 27):
                    self.main_running = False

            keys = pygame.key.get_pressed() # grab the key the user pressed
            self.user_player.step(keys) # take action on the users player with respect to the key pressed
            self.redraw_window(seld.window, self.background) # redraw with respect to new state of the game

        pygame.quit()
