import pygame
# import pygame.font
from pygame.locals import *


# Creating Text
class Text:
    """Create a text object."""
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = options['fontname'] if 'fontname' in options.keys() else None
        self.fontsize = options['fontsize'] if 'fontsize' in options.keys() else 72
        self.fontcolour = Color(options['fontcolour']) if 'fontcolour' in options.keys() else Color('white')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolour)
        self.rect = self.img.get_rect()
        self.rect.center = self.pos

    def draw(self, screen):
        """Draw the text image to the screen."""
        screen.blit(self.img, self.rect)
        print(f'inside: {screen}')


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


# Creating different scenes for the game, each screen an object
class Scene:

    def __init__(self, *args, **kwargs):
        # Append the new scene and make it the current scene
        self.scenes.append(self)
        self.scene = self
        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
        self.file = Scene.options['file']

        if self.file != '':
            self.img = pygame.image.load(self.file)
            size = self.screen.get_size()
            self.img = pygame.transform.smoothscale(self.img, size)
        self.enter()

    def draw(self, screen):
        """Draw all objects in the scene."""
        screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def __str__(self):
        return f'Scene {self.id}'

