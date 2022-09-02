from ui_elements import Text, Button, Scene

import pygame
from pygame.locals import *


# Class for the managing of the game and application
class App:

    # this is important, this classes initialisation function
    # sets up the attributes in the class and gives them initial values
    def __init__(self,title=None, resolution=None, update_rate=None):

        # Here we initialise pygame
        pygame.init()

        self.update_rate = update_rate
        self._scene = None
        self.title = title
        self.resolution = resolution





    # a cool technqiue to set and get values
    @property
    def title(self):
        return pygame.display.get_caption()

    @title.setter
    def title(self, value):
        pygame.display.set_caption(value)

    @property
    def resolution(self):
        return self._screen.get_size()

    @resolution.setter
    def resolution(self, value):
        self._screen = pygame.display.set_mode(value)

    @property
    def active_scene(self):
        """The currently active scene. Can be ``None``."""
        return self._scene

    @resolution.setter
    def resolution(self, value):
        self._screen = pygame.display.set_mode(value)

    @property
    def active_scene(self):
        """The currently active scene. Can be ``None``."""
        return self._scene

    def change_scene(self, scene):
        """Change the currently active scene.
        This will invoke :meth:`.Scene.on_exit` and
        :meth:`.Scene.on_enter` methods on the switching scenes.
        If ``None`` is provided, the application's execution will end.
        :param Scene|None scene: the scene to change into
        """
        if self.active_scene is not None:
            self.active_scene.on_exit(next_scene=scene)
            self.active_scene._application = None
        self._scene, old_scene = scene, self.active_scene
        if self.active_scene is not None:
            self.active_scene._application = self
            self.active_scene.on_enter(previous_scene=old_scene)

