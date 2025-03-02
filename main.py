import os

import pygame
from pygame.locals import *

from game import Game
from config import GameState
from shop_screen import ShopScreen
from title_screen import TitleScreen
from volume import Volume
Game.start()
Volume.mute_music()

def cursorDraw():
    if pygame.mouse.get_focused():
        Game.WINDOW.blit(TitleScreen.CURSOR, (Game.MOUSE_X, Game.MOUSE_Y))
    else:
        drawState()

def drawMainMenu():
    Game.WINDOW.blit(Game.BACKGROUND_SURFACE, (0, 0))
    TitleScreen.TITLE.draw()
    TitleScreen.drawButtons()



def drawShop():
    Game.WINDOW.blit(Game.BACKGROUND_SURFACE,(0,0))
    ShopScreen.TITLE.draw()


def drawGame():
    background_pos = (0, 0)
    background = pygame.image.load(f"assets/scenes/desert_background.png")
    background_rect = background.get_rect()
    Game.WINDOW.blit(background,background_pos)


def drawState():
    match Game.CURRENT_STATE:
        case GameState.MENU:
            drawMainMenu()
        case GameState.SHOP:
            drawShop()
        case GameState.GAME:
            drawGame()
        case _:
            pass

while Game.RUNNING:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                Game.RUNNING = False
            case pygame.VIDEORESIZE:
                Game.WIDTH, Game.HEIGHT = event.w, event.h

                if Game.HEIGHT < 720:
                    Game.HEIGHT = 720
                if Game.HEIGHT > Game.WIDTH:
                    Game.WIDTH = Game.HEIGHT

                Game.RATIO_X = Game.WIDTH / 1080
                Game.RATIO_Y = Game.HEIGHT / 720
                Game.WINDOW = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT), RESIZABLE)
                # Redéfinition des positions
                Game.BACKGROUND_SURFACE = pygame.Surface((Game.WIDTH, Game.HEIGHT))
                TitleScreen.TITLE.redefine_pos()
                TitleScreen.PLAY_BUTTON.redefine_pos()
                TitleScreen.SHOP_BUTTON.redefine_pos()
                ShopScreen.TITLE.redefine_pos()
                # Recreate the background surface on resize to avoid black screen
                Game.load_background()
    # For method cursor_draw()
    Game.MOUSE_X,Game.MOUSE_Y = pygame.mouse.get_pos()
    drawState()
    cursorDraw()
    pygame.display.update()

pygame.quit()
