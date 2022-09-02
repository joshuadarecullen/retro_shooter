# abstract class of a scene in the game
class Scene:

    title = None
    resolution = None
    update_rate = None

    def __init__(self, title=None, resolution=None, update_rate=None):
        self._application = None
        if title is not None:
            self.title = title
        if resolution is not None:
            self.resolution = resolution
        if update_rate is not None:
            self.update_rate = update_rate

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    @property
    def application(self):
        """The host application that's currently running the scene."""
        return self._application

    def draw(self, screen):
        """Override this with the scene drawing.
        :param pygame.Surface screen: screen to draw the scene on
        """

    def update(self, dt):
        """Override this with the scene update tick.
        :param int dt: time in milliseconds since the last update
        """

    def handle_event(self, event):
        """Override this to handle an event in the scene.
        All of :mod:`pygame`'s events are sent here, so filtering
        should be applied manually in the subclass.
        :param pygame.event.Event event: event to handle
        """

    def on_enter(self, previous_scene):
        """Override this to initialize upon scene entering.
        The :attr:`application` property is initialized at this point,
        so you are free to access it through ``self.application``.
        Stuff like changing resolution etc. should be done here.
        If you override this method and want to use class variables
        to change the application's settings, you must call
        ``super().on_enter(previous_scene)`` in the subclass.
        :param Scene|None previous_scene: previous scene to run
        """
        for attr in ('title', 'resolution', 'update_rate'):
            value = getattr(self, attr)
            if value is not None:
                setattr(self.application, attr.lower(), value)

    def on_exit(self, next_scene):
        """Override this to deinitialize upon scene exiting.
        The :attr:`application` property is still initialized at this
        point. Feel free to do saving, settings reset, etc. here.
        :param Scene|None next_scene: next scene to run
        """
