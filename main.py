import sys
import numpy as np

sys.path.append('./base')
from game import Game

if __name__ == "__main__":

    test = Game(1131, 675)

    test.game_loop()
