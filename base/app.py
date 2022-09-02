import pygame


class Application:

    '''
        1. title of the application window
        2. resolution or size of the application 
        3. frame rate, how many times run() is going to execute per second
    '''
    def __init__(self,
                 title=None,
                 resolution=None,
                 update_rate=None):
        pygame.init()

        # current scene and screen
        self._scene = None
        self._screen = None

        # Trigger property setters
        self.title = title
        self.resolution = resolution
        self.update_rate = update_rate

        # list of short cuts
        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'print("ctrl+X")',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
            (K_f, KMOD_LMETA): 'self.toggle_fullscreen()',
            (K_r, KMOD_LMETA): 'self.toggle_resizable()',
            (K_g, KMOD_LMETA): 'self.toggle_frame()',
        }

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    # TODO: fix these
    # def toggle_fullscreen(self):
    #     """Toggle between full screen and windowed screen."""
    #     self.flags ^= FULLSCREEN
    #     pygame.display.set_mode((0, 0), self.flags)

    # def toggle_resizable(self):
    #     """Toggle between resizable and fixed-size window."""
    #     self.flags ^= pygame.RESIZABLE
    #     pygame.display.set_mode(self.rect.size, self.flags)
    #     self.screen = pygame.display.set_mode(self.rect.size, flags)

    # def toggle_frame(self):
    #     """Toggle between frame and noframe window."""
    #     self.flags ^= NOFRAME
    #     pygame.display.set_mode(self.rect.size, self.flags)

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

    def run(self, scene=None):
        """Execute the application.
        :param scene.Scene|None scene: scene to start the execution from
        """
        if scene is None:
            if self.active_scene is None:
                raise ValueError('No scene provided')
        else:
            self.change_scene(scene)

        clock = pygame.time.Clock()

        while self.active_scene is not None:

            for event in pygame.event.get():
                self.active_scene.handle_event(event)
                if event.type == pygame.QUIT:
                    self.change_scene(None)  # Trigger Scene.on_exit()
                    return

            dt = clock.tick(self.update_rate)
            self.active_scene.update(dt)

            self.active_scene.draw(self._screen)
            pygame.display.update()
