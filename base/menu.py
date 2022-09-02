import pygame
from pygame.locals import *
from ui_elements import Text, Button
from util import reset_keys, load_save
from scene import Scene

# Menu abstract class
class Menu(Scene):

    def __init__(self, title='', resolution=(640,480), update_rate=30):
        super().__init__(title=title, resolution=resolution, update_rate=update_rate)

        self.mid_w, self.mid_h = resolution
        self.cursor_rect = pygame.Rect(0,0,20,20) # cursor rectangle
        self.offset = 50 # dont want cursor on top of text
        self.options = {'fontsize': 20} # option for the class variables in Text

        # default action keys for all menus
        self.default_actions = {'UP_KEY':False, 'DOWN_KEY':False, 'START_KEY':False, 'BACK_KEY':False}

    def draw(self, screen):
        self.cursor.pos = (self.cursor_rect.x, self.cursor_rect.y)
        self.cursor.draw(screen)

    # call this from a subclass of menu to create the cursor, set .midtop to desired position before calling
    def on_enter(self):
        self.cursor = Text('*', position=(self.cursor_rect.x,self.cursor_rect.y + self.offset), **self.options)

    # default event handling, TODO: left and right keys
    def handle_event(self, event):
        # pygame events, key presses from user etc
        if event.type == pygame.KEYDOWN:
            # self.application.do_shortcut(event)
            if event.key == pygame.K_RETURN:
                self.default_actions['START_KEY'] = True
            if event.key == pygame.K_BACKSPACE:
                self.default_actions['BACK_KEY'] = True
            if event.key == pygame.K_DOWN:
                self.default_actions['DOWN_KEY'] = True
            if event.key == pygame.K_UP:
                self.default_actions['UP_KEY'] = True


class StartMenu(Menu):

    def __init__(self):
        # self.font = pygame.font.Font(...) for setting a specifc font for the menu
        super().__init__(title='Start Menu')

    def on_enter(self, previous_scene):

        # create the cursor
        super().on_enter()

        # TODO: clean this up, on_enter function in scene shouldnt be touched
        self.application.title = self.title
        self.application.resolution = self.resolution
        self.application.update_rate = self.update_rate

        # state of the start menu
        self.state = 'Start'

        # possible options for the start menu
        self.titles = ['Enter', 'Settings', 'Credits']

        # creating the position of each title on the canvas, shape=(2,3)
        self.poses = [[self.mid_w/2, self.mid_h/4 + x] for x in range(30, 71, 20)]

        # cursor off set for each title, shape = (2,3)
        self.offsets = {self.titles[i]: (self.poses[i][0] + self.offset, self.poses[i][1]) for i in range(3)}

        # options to configure the Text object
        self.options = {'fontsize': 20, 'fontcolour': 'white'}

        self.menu_title = Text('Start Menu', position=(self.mid_w/2,self.mid_h/8), **self.options)

        # A list of text objects (each object in the list corresponds to a title)
        self.text_objs = [Text(self.titles[i], position=tuple(self.poses[i]), **self.options) for i in range(3)]

        # doesnt matter but nice to set cursor to top of the options
        # plus if we dont have this here the cursor wont be visible until user hits an arrow key
        self.cursor_rect.midtop = self.offsets['Enter']


    # after events are handled and updates undertaken: draw changes
    def draw(self, screen):

        # wipe canvas
        screen.fill(self.BLACK)

        # Set the title
        self.menu_title.draw(screen)

        # display the text objects for the start menu
        for obj in self.text_objs:
            obj.draw(screen)

        # draw cursor
        super().draw(screen)

        reset_keys(self.default_actions)


    def update(self, dt):

        # if down key pressed check the current state and adjust accordingly
        if self.default_actions['DOWN_KEY']:

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
        if self.default_actions['UP_KEY']:

            if self.state == 'Start':
                self.cursor_rect.midtop = tuple(self.offsets['Credits'])
                self.state = 'Credits'

            elif self.state == 'Settings':
                self.cursor_rect.midtop = tuple(self.offsets['Enter'])
                self.state = 'Start'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = tuple(self.offsets['Settings'])
                self.state = 'Settings'

        if self.default_actions['START_KEY']:
            if self.state == 'Start':
                self.application.change_scene(MainMenu())
            elif self.state == 'Settings':
                self.application.change_scene(SettingsMenu())
            elif self.state == 'Credits':
                self.application.change_scene(Credits())


class SettingsMenu(Menu):

    def __init__(self):
        super().__init__(title='Settings')

    def on_enter(self, previous_scene):

        self.application.title = self.title
        self.application.resolution = self.resolution
        self.application.update_rate = self.update_rate

        self.previous_scene = previous_scene

        self.scene_title = Text(self.title, position=self.resolution)

        reset_keys()

    def update(self):
         if self.BACKSPACE:
             self.application.change_scene(self.previous_scene)

    def draw(self):
        pass


class Credits(Menu):

    def __init__(self):
        super().__init__(title='Credit')
        self.options = {'fontsize': 20}

    def on_enter(self, previous_scene):

        reset_keys(self.default_actions)

        self.previous_scene = previous_scene

        self.application.title = self.title
        self.application.resolution = self.resolution
        self.application.update_rate = self.update_rate

        self.main_title = Text('Credits', position=resolution)
        self.main_texts = Text('Made by me, soon to be bradley the bum', position=(self.mid_w/2, self.mid_h/2.5), **self.options)


    def update(self, dt):
         if self.BACKSPACE:
             self.application.change_scene(self.previous_scene)

    def draw(self, screen):
        pass


class MainMenu(Menu):

    def __init__(self):
        super().__init__(title='Main Menu')
        self.state = 'Start'
        self.options = {'fontsize': 20}

    def on_enter(self, previous_scene):

        self.previous_scene = previous_scene
        reset_keys(self.default_actions)

        self.application.title = self.title
        self.application.resolution = self.resolution
        self.application.update_rate = self.update_rate

    def update(self, dt):
        pass
        # check if user wants to go back to start screen

        # Set the title

    def draw(self, screen):
        pass

class GameMenu(Menu):
    def __init__(self):
        pass
