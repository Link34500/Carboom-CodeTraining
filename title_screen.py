import pygame.image

from config import GameState
from game import Game
from sprites.buttons import Button
from sprites.elements import Elements


class TitleScreen:
    TITLE = None
    PLAY_BUTTON = None
    SHOP_BUTTON = None
    CURSOR = None
    BUTTONS = []
    @staticmethod
    def loadMenuElement():
        TitleScreen.TITLE = Elements(font="LuckiestGuy-Regular.ttf", text="Carboom", color="#db0726", xpos=Game.WIDTH / 2, ypos=200,font_scale=95)
        TitleScreen.PLAY_BUTTON = Button("buttons/button.png", "buttons/selected_button.png", 2, 2, 2, 2, 60, "Kenney Future.ttf","Play", "ffffff", Game.WIDTH / 2, Game.HEIGHT / 2, GameState.GAME)
        TitleScreen.SHOP_BUTTON = Button("buttons/button.png", "buttons/selected_button.png", 2, 2, 2, 2, 60, "Kenney Future.ttf","Shop", "ffffff", Game.WIDTH / 2, Game.HEIGHT / 2 + TitleScreen.PLAY_BUTTON.get_height() + 25,GameState.SHOP)
        TitleScreen.CURSOR = pygame.image.load("assets/sprites/cursor.png")
        TitleScreen.BUTTONS = [TitleScreen.PLAY_BUTTON, TitleScreen.SHOP_BUTTON]
    @staticmethod
    def drawButtons():
        for button in TitleScreen.BUTTONS:
            button.image_button_cursor()
            button.button_pressed()
            button.draw()