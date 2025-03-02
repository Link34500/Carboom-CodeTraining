import pygame

from game import Game
from utils import hex_to_rgb


class Elements:
    def __init__(self, image=None, scale_x=1, scale_y=1, font_scale=None, font=None, text=None, color="ffffff", xpos=None, ypos=None):
        self.image = image
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.font_scale = font_scale
        self.font = font  # Font name
        self.text = text
        self.color = color
        self.x_ratio = xpos / Game.WIDTH
        self.y_ratio = ypos / Game.HEIGHT
        self.x = xpos
        self.y = ypos
        self.element = None
        self.element_text = None
        self.element_text_pos = None

    def redefine_pos(self):
        self.x = int(self.x_ratio * Game.WIDTH)
        self.y = int(self.y_ratio * Game.HEIGHT)

        if Game.WIDTH > 1080:
            self.y = int(self.y_ratio * Game.HEIGHT)
            return
        if Game.WIDTH < 1080:
            self.y = int(self.y_ratio * Game.HEIGHT) * (Game.WIDTH / 1080)
            return
        if Game.HEIGHT > 720:
            self.y = int(self.y_ratio * Game.HEIGHT) / (Game.HEIGHT / 720)
            return
    def get_element(self):
        # Image Element ?
        if self.image is not None:
            try:
                element = pygame.image.load("assets/sprites/" + self.image).convert_alpha()
            except FileNotFoundError:
                element = pygame.image.load("assets/sprites/error.png").convert_alpha()
            new_width = int(element.get_width() * self.scale_x * min(Game.RATIO_X, Game.RATIO_Y))
            new_height = int(element.get_height() * self.scale_y * min(Game.RATIO_X, Game.RATIO_Y))
            self.element = pygame.transform.scale(element, (new_width, new_height))

        if self.text is not None:
            self.load_text()

        return self.element, self.element_text,self.element_text_pos

    def load_text(self):
        font_size = int(self.font_scale * min(Game.RATIO_X, Game.RATIO_Y))
        if self.font is not None:
            font = pygame.font.Font("assets/fonts/" + self.font, font_size)
        else:
            font = pygame.font.Font(None, font_size)
        self.element_text = font.render(self.text, True, hex_to_rgb(self.color))
        self.element_text_pos = self.element_text.get_rect(center=(self.x, self.y))

        return self.element_text, self.element_text_pos



    def draw(self):
        self.get_element()
        if self.element is not None:
            Game.WINDOW.blit(self.element, (self.x - self.element.get_width() // 2, self.y - self.element.get_height() // 2))
            if self.element_text is not None:
                Game.WINDOW.blit(self.element_text,self.element_text_pos)
        elif self.element_text is not None:
            Game.WINDOW.blit(self.element_text,self.element_text_pos)

    def get_pos_x(self):
        return self.x
    def get_pos_y(self):
        return self.y
    def get_width(self):
        if self.element is None : self.get_element()
        return self.element.get_width()

    def get_height(self):
        if self.element is None: self.get_element()
        return self.element.get_height()

    def get_text(self):
        return self.text
