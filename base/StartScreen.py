import pygame
from game import Game
from button import Start

#TODO: set background, rethinking how the background will change

class StartMenu(Game):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.initialize_game()

        self.window = pygame.display.set_mode((width, height))
        self.background = pygame.image.load('./sprites/backgrounds/menus/StartBackground.jpg') # background
        self.start_button = Start(window = self.window, y=self.width, x=self.height)

        self.characters = self.get_characters()
        self.selected_character = None

        self.main_running = True


    def initialize_game(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Start Menu")
        pygame.mixer.set_num_channels(8)


    def draw_character_window(selection):
        pass


    def draw_start_window(self):
        self.window.blit(self.background, (0, 0))
        self.start_button.draw_button()
        pygame.display.update()


    # get the character they selected
    def get_characters(self):
        pass


    # main start functions
    def main(self):

        self.draw_start_window()
        # keep application running
        while self.main_running:
            self.clock.tick(40)

            if self.endgame:
                self.main_running = False


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_button.on_click(event)

            pygame.display.update()


        pygame.quit()

