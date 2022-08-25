import pygame

class Game:

    def __init__(self, width, height):
        self.initialise_game()
        self.pygame.display.set_mode((width, height))
        self.background = None
        self.clock

    def initialise_game(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Game")
        pygame.display.set_num_channels(8)


    def run(self):
        pass


