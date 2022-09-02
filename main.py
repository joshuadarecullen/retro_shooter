import sys
sys.path.append('./base')
# from game import Game

from app import Application
from menu import StartMenu

if __name__ == "__main__":

    app = Application(
            title='Retro Shooter',
            resolution=(1280, 720),
            update_rate=60
            )

    # main loop for the game
    start = StartMenu()
    app.run(start)
