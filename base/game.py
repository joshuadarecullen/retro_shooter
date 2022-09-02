from app import Application
from menu import StartMenu
from util import load_save


class Game(Application):
    def __init__(self, title, resolution, update_rate):
        super().__init__(title=title, resolution=resolution, update_rate=update_rate)

        # load saved controls
        save = load_save()

    # main loop for the game
    def game_loop(self):
        start = StartMenu()
        self.run()

