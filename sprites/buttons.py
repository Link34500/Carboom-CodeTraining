import pygame

from game import Game
from config import Song
from sprites.elements import Elements


class Button(Elements):
    def __init__(self, image=None, image_cob="error.png", cob_scale_x=1, cob_scale_y=1, scale_x=1, scale_y=1, font_scale=None, font=None, text=None, color="ffffff", xpos=None, ypos=None, state_changer=None):
        super().__init__(image, scale_x, scale_y, font_scale, font, text, color, xpos, ypos)
        self.image_cob = image_cob
        self.image_og = image
        self.og_scale_x = scale_x
        self.og_scale_y = scale_y
        self.cob_scale_x = cob_scale_x
        self.cob_scale_y = cob_scale_y
        self.cob_played = False
        self.state_changer = state_changer

    def image_button_cursor(self):
        if self.is_cursor_in_button():
            self.image = self.image_cob
            self.scale_x = self.cob_scale_x
            self.scale_y = self.cob_scale_y
            if not self.cob_played:
                self.cob_played = True
                Game.play(Song.BUTTON_OVER_IT)
        else:
            self.cob_played = False
            self.image = self.image_og
            self.scale_y = self.og_scale_y
            self.scale_x = self.og_scale_x

    def is_cursor_in_button(self):
        button_rect = pygame.Rect(int(self.x - self.get_width() / 2),
                                  int(self.y - self.get_height() / 2), int(self.get_width()),
                                  int(self.get_height()))
        return button_rect.collidepoint(Game.MOUSE_X, Game.MOUSE_Y)


    def button_pressed(self):
        if self.is_cursor_in_button():
            if pygame.mouse.get_pressed()[0]:
                Game.play(Song.BUTTON_CLICK)
                Game.CURRENT_STATE = self.state_changer

    def get_element(self):
        # Image Element ?
        if self.image is not None:
            try:
                element = pygame.image.load("assets/sprites/" + self.image).convert_alpha()
            except FileNotFoundError:
                element = pygame.image.load("../assets/sprites/error.png").convert_alpha()
            new_width = int(element.get_width() * self.scale_x * min(Game.RATIO_X, Game.RATIO_Y))
            new_height = int(element.get_height() * self.scale_y * min(Game.RATIO_X, Game.RATIO_Y))
            self.element = pygame.transform.scale(element, (new_width, new_height))
        if self.text is not None:
            self.load_text()

        return self.element, self.element_text,self.element_text_pos