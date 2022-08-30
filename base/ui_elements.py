import pygame
# import pygame.font
from pygame.locals import *

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


# Creating Text
class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self, screen):
        """Draw the text image to the screen."""
        screen.blit(self.img, self.rect)


# creating buttons
class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The Button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
