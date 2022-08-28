import pygame.font

class Button:
    def __init__(self, x, y, window):
        ''' initialise button attributes '''
        self.width, self.height  = 110, 50
        self.x = x - self.width // 2
        self.y = y - self.height // 2
        self.window = window
        self.window_rect = self.window.get_rect()

        # superficial design attributes
        self.button_clicked = False
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 35)


        # Build the buttons rect object and center it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.window_rect.center


        # build text change when clicked
        self.text_clicked = self.font.render("Clicked", True, self.text_colour)

        # size of the clickable area of the button
        self.hitbox = (self.x, self.y, self.width, self.height)


    def draw_button(self):

        # Draw blank button and then draw the message
        self.window.fill(self.button_colour, self.rect)
        self.window.blit(self.text, self.rect)


    # when clicked
    def on_click(self, event):

        if self.text_rect.collidepoint(event.pos):
            self.button_clicked = True
            self.window.blit(self.text_clicked, self.text_rect)
        else:
            self.button_clicked = False
            self.window.blit(self.text_clicked, self.text_rect)

        # Update the display using flip
        pygame.display.update()


    def get_button_state(self):
        return self.button_clicked


class Start(Button):
    def __init__(self, window=None, x=0, y=0):
        super().__init__(x, y, window)

        self.text = self.font.render("Enter", True, self.text_colour)
        self.text_rect = self.text.get_rect()

    def on_click(self, event):

        if self.text_rect.collidepoint(event.pos):
            self.button_clicked = False
            self.window.blit(self.text, self.text_rect)
        else:
            self.button_clicked = True 
            self.clck_text_rect = self.text_clicked.get_rect()
            self.clck_text_rect.center = self.window_rect.center
            self.window.blit(self.text_clicked, self.clck_text_rect)

    def draw_button(self):
        
        # Draw blank button and then draw the message
        self.window.fill(self.button_colour, self.rect)
        self.window.blit(self.text, self.rect)

