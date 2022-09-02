import pygame, sys
base_files = f'{os.path.dirname(os.getcwd())}/base'
from base_files import *

# from ui_elements import Text
# from util import write_save
# from scene import Scene

class Controls_Hander(Menu):

    def __init__(self, save):
        super().__init__(title='Control Profile')
        self.save_file = save
        self.curr_block = save['current_profile'] #put in key to get desired controls
        self.controls = self.save_file['controls'][str(self.curr_block)]


    def on_enter(self, previous_scene):

        self.application.title = self.title
        self.application.resolution = self.resolution
        self.application.update_rate = self.update_rate

        self.selected = False
        self.curr_index = 0
        self.cursor_dict = {}
        self.control_tobj = []

        x, y = self.application.resolution

        # create menu and current profile text objects
        self.menu_title = Text(f'{self.title}-{self.curr_block+1}', pos=(x/2, y/16)

        # mapping controls
        for i, control in enumerate(self.controls):
            self.cursor_dict[i] = control

            i *= 30
            # create text object for every control and map it to its respective key
            self.control_tobj.append(
                    Text(f'control-{pygame.key.name(controls[control])}', pos=(x/2, y/8+i)
                    )
        self.set_profile = Text(f'Set Current Profile', pos=(x/2,y/8+i))

        self.cursor_dict[i] = 'Set' # set the profile controls

        if self.curr_block == self.save_file['current_profile']: self.cursor_rect.midtop = self.set_profile.pos

        super().on_enter()

    def handle_event(self, event):
        pass

    def update(self, actions):
        pass

    def draw(self, screen):
        super().draw(screen)

        colour = (255,13,5) if self.selected else (255,250,239)
        self.menu_title.draw(screen)
        self.set_profile.draw(screen)
        for control in self.control_tobj:
            control.fontcolour(colour)
            control.draw(screen)

