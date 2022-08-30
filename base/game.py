from player import *
from ui_elements import Text, Button, Scene

import pygame
from pygame.locals import *


# Class for the managing of the game and application
class Game:

    # this is important, this classes initialisation function
    # sets up the attributes in the class and gives them initial values
    def __init__(self, width, height, position=None):

        # initialise pygame and application
        self.initialise_game()
        flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 240)
        self.screen = pygame.display.set_mode(self.rect.size, flags)

        # UI start screen initialisation
        self.background = None
        # window variables
        self.width = width
        self.height = height

        self.start_text = Text('Retro Shooter', pos=(20,20))

        # self.start_button = Start(window = self.window, y=self.width, x=self.height)
        self.clock = pygame.time.Clock() # useful to keep track of time for in game stats

        #  for main hyper-loop keeping the application running
        self.running, self.player = True, False

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False,False,False,False

        # agents within the game player and computer
        self.user_player = None
        self.characters = self.get_characters()
        self.selected_character = None

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'print("ctrl+X")',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
            (K_f, KMOD_LMETA): 'self.toggle_fullscreen()',
            (K_r, KMOD_LMETA): 'self.toggle_resizable()',
            (K_g, KMOD_LMETA): 'self.toggle_frame()',
        }

    def get_scenes(self):

        Scene(img_folder='./sprites/backgrounds/menus', file='StartBackground.jpg', caption='Intro')
        Text('Scene 0')
        Text('Introduction screen the app')

        Scene(bg=Color('yellow'), caption='Options')
        Text('Scene 1')
        Text('Option screen of the app')

        Scene(bg=Color('green'), caption='Main')
        Text('Scene 2')
        Text('Main screen of the app')
        self.scene = self.scenes[0]

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])


    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)


    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)


    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)


    # Here we initialise pygame and the window
    def initialise_game(self):
        pygame.init()
        # pygame.mixer.init()
        # pygame.display.set_caption("Retro Shooter")
        # pygame.display.set_num_channels(8)


    # redraw what the user will be seeing
    def redraw_window(self):

        # set background
        self.background = pygame.image.load('./sprites/backgrounds/menus/StartBackground.jpg') # background

        # # redraw the player in new state
        # self.user_player.player_drawing(window)


    def respawn_player(self, player):
        pass


    # get available characters
    def get_characters(self):
        pass


    def check_events(self):
        # pygame events that indicate the exiting of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #or (event.type == 2 and event.dict['key'] == 27):
                self.running self.player = False, False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == KEYDOWN:
                self.do_shortcut(event)

    # running the game itself
    def run(self):

        # self.user_player = player 

        # TODO: initialise the computer enemies

        while self.running:

            self.check_events()

            pygame.display.update()


            # keys = pygame.key.get_pressed() # grab the key the user pressed
            # self.user_player.step(keys) # take action on the users player with respect to the key pressed
            # self.redraw_window(seld.window, self.background) # redraw with respect to new state of the game

        pygame.quit()
