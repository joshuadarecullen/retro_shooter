from .base.app import Application
from .menus.menu import StartMenu
from .base.util import load_save


class Game(Application):
    def __init__(self, title, resolution, update_rate):
        super().__init__(title=title, resolution=resolution, update_rate=update_rate)

        # load saved controls
        # save = load_save()

    # main loop for the game
    def game_loop(self):
        start = StartMenu()
        self.run(start)

