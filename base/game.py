from player import *
from app import *
from ui_elements import Text, Button, Scene
from menu import StartMenu

class Game(App):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.curr_men = StartMenu(self)


    # redraw what the user will be seeing
    def update(self):
        # set background
        self.background = pygame.image.load('./sprites/backgrounds/menus/StartBackground.jpg') # background

    # running the game itself, overided Apps loop
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

        pygame.quit()


    # drawing elements to the screen
    def draw_obj(self, object):
        object.draw(self.display)


    # checking possible events in this menu
    def check_events(self):

        # pygame events, key presses from user etc
        for event in pygame.event.get():

            # indicate the exiting of the game
            if event.type == pygame.QUIT: #or (event.type == 2 and event.dict['key'] == 27):
                self.running, self.playing = False, False
                self.curr_men.run_display = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pass

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


    # main loop for the game
    def game_loop(self):
        while self.running:
            self.curr_men.display_menu()
            self.playing = True
            self.run()
