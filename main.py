import sys
import numpy as np

sys.path.append('./base')
from StartScreen import StartMenu
# from game import Game

if __name__ == "__main__":
    test_game = StartMenu(1131, 675)
    test_game.run()
