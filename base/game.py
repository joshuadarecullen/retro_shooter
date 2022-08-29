from player import * # importing from PLayer.py everything
# from ui_controls import Text, Button
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
        Game.screen = pygame.display.set_mode((width, height), flags)

        # UI start screen initialisation
        self.background = pygame.image.load('./sprites/backgrounds/menus/StartBackground.jpg') # background
        # window variables
        self.width = width
        self.height = height

        Game.start_text = Text('Retro Shooter', pos=(20,20))

        # self.start_button = Start(window = self.window, y=self.width, x=self.height)
        self.clock = pygame.time.Clock() # useful to keep track of time for in game stats

        #  for main hyper-loop keeping the application running
        self.running = True 
        self.endgame = False


        # agents within the game player and computer
        self.user_player = None
        self.characters = self.get_characters()
        self.selected_character = None


    # Here we initialise pygame and the window
    def initialise_game(self):
        pygame.init()
        # pygame.mixer.init()
        # pygame.display.set_caption("Retro Shooter")
        # pygame.display.set_num_channels(8)


    # redraw what the user will be seeing
    def redraw_window(self, window, background):

        # set background
        window.blit(background, (0,0))

        # redraw the player in new state
        self.user_player.player_drawing(window)


    def respawn_player(self, player):
        pass


    # get available characters
    def get_characters(self):
        pass


    # running the game itself
    def run(self):

        # self.user_player = player 
        # self.initialise_real_game()

        # TODO: initialise the computer enemies

        while self.running:

            if self.endgame:
                self.running = False

            # pygame events that indicate the exiting of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #or (event.type == 2 and event.dict['key'] == 27):
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            Game.start_text.draw()
            pygame.display.update()


            # keys = pygame.key.get_pressed() # grab the key the user pressed
            # self.user_player.step(keys) # take action on the users player with respect to the key pressed
            # self.redraw_window(seld.window, self.background) # redraw with respect to new state of the game

        pygame.quit()


# Text class
class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        Game.screen.blit(self.img, self.rect)
