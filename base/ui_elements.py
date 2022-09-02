import pygame
import pygame.font
from pygame.locals import *


# Creating Text
class Text:
    """Create a text object."""
    def __init__(self, text, position, **options):
        self.text = text
        self._pos = position

        self._fontname = options['fontname'] if 'fontname' in options.keys() else None
        self._fontsize = options['fontsize'] if 'fontsize' in options.keys() else 20
        self._fontcolour = Color(options['fontcolour']) if 'fontcolour' in options.keys() else Color('white')
        self.set_font()
        self.render()

    @property
    def font(self):
        return self.font

    @font.setter
    def font(self, value):
        """Set the font from its name and size."""
        self._font = pygame.font.Font(self.fontname, self.fontsize)

    def set_font(self):
        """Set the font from its name and size."""
        self._font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self._font.render(self.text, True, self._fontcolour)
        self.rect = self.img.get_rect()
        self.rect.center = self._pos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def fontcolour(self):
        return self._fontcolour

    @fontcolour.setter
    def fontcolour(self, value):
        self._fontcolour = value

    @property
    def fontsize(self):
        return self._fontsize

    @fontsize.setter
    def fontsize(self, value):
        self._fontsize = value

    @property
    def fontname(self):
        return self._fontname

    @fontname.setter
    def fontname(self, value):
        self._fontname = value

    def draw(self, screen):
        self.set_font()
        self.render()
        """Draw the text image to the screen."""
        screen.blit(self.img, self.rect)


class Button(Text):

    def __init__(self, text, pos, **options):
        super().__init__(text, pos, **options)
        self.button_colour = options['button_colour'] if 'button_colour' in options.keys() else (0, 0, 0)

    # overiding the draw function in Text class
    def draw(self, screen):
        """Draw the button image to the screen."""
        # Difference between Text class is that we fill area surrounding the text
        screen.fill(self.button_colour, self.rect)
        screen.blit(self.img, self.rect)

