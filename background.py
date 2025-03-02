import pygame

from game import Game


class Background:
    def __init__(self, image=None, xpos=None, ypos=None):
        self.image = image
        self.x_ratio = xpos / Game.WIDTH
        self.y_ratio = ypos / Game.HEIGHT
        self.x = xpos
        self.y = ypos
        self.background = None
        self.background_text = None
        self.background_text_pos = None

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
    def get_background(self):
        # Image Element ?
        if self.image is not None:
            try:
                background = pygame.image.load("assets/scenes/" + self.image).convert_alpha()
            except FileNotFoundError:
                background = pygame.image.load("assets/sprites/error.png").convert_alpha()
            self.background = pygame.transform.scale(background, (0 , 0))

        return self.background

    def draw(self):
        self.get_background()
        if self.background is not None:
            Game.WINDOW.blit(self.background, (self.x - self.background.get_width() // 2, self.y - self.background.get_height() // 2))
            if self.background_text is not None:
                Game.WINDOW.blit(self.background_text,self.background_text_pos)
        elif self.background_text is not None:
            Game.WINDOW.blit(self.background_text,self.background_text_pos)

    def get_pos_x(self):
        return self.x
    def get_pos_y(self):
        return self.y
    def get_width(self):
        if self.background is None : self.get_background()
        return self.background.get_width()

    def get_height(self):
        if self.background is None: self.get_background()
        return self.background.get_height()

