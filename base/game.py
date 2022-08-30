from player import *
from app import *
from ui_elements import Text, Button, Scene
from menu import *
import pygame
from pygame.locals import *

class Game(App):

    def __init__(self, width, height):
        super().__init__(width, height)

        # create all menu objects
        self.start_menu = StartMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.settings_menu = SettingsMenu(self)
        self.main_menu = MainMenu(self)
        self.curr_menu = self.start_menu

    # redraw what the user will be seeing
    def update(self):
        # set background
        self.background = pygame.image.load('./sprites/backgrounds/menus/StartBackground.jpg') # background

    # main loop for the game
    def game_loop(self):
        while self.running:
            self.curr_menu.display_menu()
            self.run()

    # running the game itself
    def run(self):

        while self.playing:

            self.check_events()

            if self.START_KEY:
                self.playing = False

            self.display.fill(self.BLACK)
            # self.draw_obj(Text('Retro Shooter', pos=(self.width/2, self.height/2), opitions = {'fontsize: 20'}))
            self.screen.blit(self.display, (0,0)) # aligning display with window
            pygame.display.update() # update computer screen
            self.reset_keys() # reset keys to track next command from user


    # checking possible events in this menu
    def check_events(self):
        # pygame events, key presses from user etc
        for event in pygame.event.get():
            # indicate the exiting of the game
            if event.type == pygame.QUIT: #or (event.type == 2 and event.dict['key'] == 27):
                self.running, self.playing = False, False
                self.curr_menu.run_display = False

            if event.type == KEYDOWN:
                self.do_shortcut(event)
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
