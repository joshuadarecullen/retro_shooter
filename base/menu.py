import pygame
from ui_elements import Text, Button

# Menu abstract class
class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.width/2, self.game.height/2
        self.run_display = True # tell our menu to keep running
        self.cursor_rect = pygame.Rect(0,0,20,20) # cursor
        self.offset = -100 # dont want cursor on top of text

    def draw_cursor(self):
        self.game.draw_obj(Text('*', pos=(self.cursor_rect.x,self.cursor_rect.y), opitions = {'fontsize: 20'}))

    def blit_screen(self):
        self.game.screen.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.reset_keys()

    def handle_event(self, event):
        pass


# Menu for the Start screen
class StartMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        self.state = 'Start'

        # possible options for the start menu
        self.titles = ['Enter', 'Setting', 'Credits']

        # creating the position of each title on the canvas, shape=(2,3)
        self.poses = [(self.mid_w, self.mid_h + x) for x in range(30, 71, 20)]

        # cursor off set for each title, shape = (2,3)
        self.offsets = {self.titles[i]: self.poses[i] for i in range(3)}

        # options to configure the Text object
        self.options = {'fontsize': 20, 'fontcolour': 'white'}

        # A list of text objects (each object in he list corresponds to a title)
        self.text_objs = [Text(self.titles[i], pos=tuple(self.poses[i]), **self.options) for i in range(3)]


    # diplaying the start menu
    def display_menu(self):

        self.run_display = True # here only to make sure it is True when we call this function

        # another loop to keep the diplay showing until otherwise
        while self.run_display:

            # get users input to primarily set the logic for the cursor movement
            self.game.check_events()

            # check for user selection from start menu
            self.check_input()

            # wipe canvas
            self.game.display.fill(self.game.BLACK)

            # Set the title
            self.game.draw_obj(Text('Start Menu', pos=(self.game.width/2, self.game.height), **self.options))

            # display the text objects for the start menu
            for obj in self.text_objs:
                self.game.draw_obj(obj)

            self.draw_cursor()

            # update the screen from events occured
            self.blit_screen()


    def move_cursor(self):

        # if down key pressed check the current state and adjust accordingly
        if self.game.DOWN_KEY:

            if self.state == 'Start':
                self.cursor_rect.midtop = tuple(self.offsets['Settings'])
                self.state = 'Settings'

            elif self.state == 'Settings':
                self.cursor_rect.midtop = tuple(self.offsets['Credits'])
                self.state = 'Credits'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = tuple(self.offsets['Enter'])
                self.state = 'Start'

        # same logic for user pressing the up key
        if self.game.UP_KEY:

            if self.state == 'Start':
                self.cursor_rect.midtop = tuple(self.offsets['Credits'])
                self.state = 'Credits'

            elif self.state == 'Settings':
                self.cursor_rect.midtop = tuple(self.offsets['Enter'])
                self.state = 'Start'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = tuple(self.offsets['Settings'])
                self.state = 'Settings'

    def check_input(self):

        self.move_cursor()

        if self.game.START_KEY:

            if self.state == 'Start':
                self.game.playing = True

            elif self.state == 'Settings':
                pass

            elif self.state == 'Credits':
                pass

        self.run_display = False # when play selects with start key it will tell the display menu function to stop


class SettingsMenu(Menu):

    def __init__(self, game):
        super().__init__(game)


class MainMenu(Menu):

    def __init__(self, game):
        super().__init__(game)


class GameMenu(Menu):

    def __init__(self, game):
        super().__init__(game)
