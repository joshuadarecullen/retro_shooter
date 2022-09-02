import game_files
from game_files.game import Game


if __name__ == "__main__":

    app = Game(title='Retro Shooter', resolution=(680,480), update_rate=30)

    app.game_loop()

    # # main loop for the game
    # start = StartMenu()
    # app.run(start)
