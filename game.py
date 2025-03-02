import abc
import pygame
from pygame.locals import *
import config


class Game(abc.ABC):
    WIDTH = 1080
    HEIGHT = 720
    VOLUME = 0.25
    RATIO_X = WIDTH / 1080
    RATIO_Y = HEIGHT / 720
    WINDOW = None
    ICON = pygame.image.load("assets/icons/icon.png")
    RUNNING = False
    MOUSE_X = None
    MOUSE_Y = None
    CURRENT_STATE = config.GameState.MENU
    MUSICS = {}
    GAME_SONG = {}
    SOUNDS = {}
    BACKGROUND = None
    BACKGROUND_SURFACE = None

    @staticmethod
    def start():
        pygame.init()
        Game.load_sounds()
        Game.create_window()
        Game.setup_mouse()
        Game.load_assets()
        Game.load_background()
        Game.start_music()
        Game.load_title_screen()
        Game.load_shop_screen()
        Game.RUNNING = True



    @staticmethod
    def load_sounds():
        print("Chargement des sons")
        Game.SongLoad.MAIN_MENU_MUSIC = pygame.mixer.Sound("assets/songs/main_menu.mp3")
        Game.SongLoad.CURSOR_IN_BUTTON = pygame.mixer.Sound("assets/songs/switch-a.ogg")
        Game.SongLoad.CLICK_BUTTON = pygame.mixer.Sound("assets/songs/switch-a.ogg")
        Game.MUSICS = {config.Song.MAIN_MENU: Game.SongLoad.MAIN_MENU_MUSIC,}
        Game.GAME_SONG = {config.Song.BUTTON_OVER_IT: Game.SongLoad.CURSOR_IN_BUTTON,config.Song.BUTTON_CLICK : Game.SongLoad.CLICK_BUTTON}
        Game.SOUNDS = Game.MUSICS | Game.GAME_SONG
        from volume import Volume
        Volume.set_volume(Game.VOLUME)
        Volume.set_game(Game.VOLUME)
        Volume.set_music(Game.VOLUME)

    @staticmethod
    def create_window():
        print("Définition du titre et de l'icône")
        pygame.display.set_icon(Game.ICON)
        pygame.display.set_caption('Carboom')
        print("Chargement de la fenêtre")
        Game.WINDOW = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT), RESIZABLE)

    @staticmethod
    def setup_mouse():
        print("Définition des Valeurs Souris")
        Game.MOUSE_X, Game.MOUSE_Y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)

    @staticmethod
    def load_assets():
        print("Chargement des assets curseurs")
        Game.BACKGROUND = pygame.image.load("assets/background.png").convert()
        Game.BACKGROUND_SURFACE = pygame.Surface((Game.WIDTH, Game.HEIGHT))

    @staticmethod
    def start_music():
        print("Lancemment de la musique de fond")
        Game.play(config.Song.MAIN_MENU, -1)

    @staticmethod
    def load_title_screen():
        print("Chargement du Menu Principal")
        from title_screen import TitleScreen
        TitleScreen.loadMenuElement()

    @staticmethod
    def load_shop_screen():
        print("Chargement des assets boutique")
        from shop_screen import ShopScreen
        ShopScreen.loadShopElement()


    @staticmethod
    def load_background(): # Method to load background
        tile_w, tile_h = Game.BACKGROUND.get_size()
        for x in range(0, Game.WIDTH, tile_w):
            for y in range(0, Game.HEIGHT, tile_h):
                Game.BACKGROUND_SURFACE.blit(Game.BACKGROUND, (x, y))

    # Methods to play a song
    @staticmethod
    def play(song, r : int =0):
        if song in Game.SOUNDS:
            Game.SOUNDS[song].play(r)
    class SongLoad:
        MAIN_MENU_MUSIC = None
        CURSOR_IN_BUTTON = None
        CLICK_BUTTON = None
