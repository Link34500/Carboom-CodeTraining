from game import Game
from sprites.elements import Elements


class ShopScreen:
    TITLE = None
    CURSOR = None
    BUTTONS = []
    @staticmethod
    def loadShopElement():
        ShopScreen.TITLE = Elements(font="Kenney Future Narrow.ttf", text="Shop", color="#db0726", xpos=Game.WIDTH / 2, ypos=100,font_scale=55)