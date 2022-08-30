from ui_elements import Text, Button, Scene

import pygame
from pygame.locals import *


# Class for the managing of the game and application
class App:

    # this is important, this classes initialisation function
    # sets up the attributes in the class and gives them initial values
    def __init__(self, width, height):

        # Here we initialise pygame
        pygame.init()

        # window variables
        self.width = width
        self.height = height
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # initialise pygame and window
        # flags = pygame.RESIZABLE
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.display = pygame.Surface(self.rect.size)  #, flags) this is the canvas
        self.screen = pygame.display.set_mode(self.rect.size) #, flags)

        pygame.display.set_caption('Retro Shooter')
        self.background = None

        # useful to keep track of time for in game stats
        self.clock = pygame.time.Clock() 

        #  for main hyper-loop keeping the application running
        self.running, self.playing = True, False

        # arrow keys for navigation, keep track of whihc one has been pressed
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False,False,False,False

        # list of short cuts
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


    # drawing elements to the screen
    def draw_obj(self, object):
        # use display here so we can add multply elements before updating screen
        object.draw(self.display)

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
        self.flags ^= pygame.RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)
        self.screen = pygame.display.set_mode(self.rect.size, flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False,False,False,False

    def title(self, value):
        pygame.display.set_caption(value)


