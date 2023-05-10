from functools import partial

import pygame

from core.SceneSwitcher import SceneSwitcher
from scenes.game import game_scene
from scenes.intro import intro_scene
from scenes.menu import main_menu_scene



# Initialize game window
mainClock = pygame.time.Clock()
pygame.init()
WINDOW_SIZE = (1280, 720)
icon = pygame.image.load('assets/icon.png')
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Trash Crash')
pygame.display.set_icon(icon)

switcher = SceneSwitcher(window)
switcher.add_scene('intro', intro_scene)
switcher.add_scene('main_menu', main_menu_scene)
switcher.add_scene('game', game_scene)
switcher.switch_to('intro')

running = True
while running:
    for event in pygame.event.get(eventtype=pygame.QUIT):
        running = False
    switcher.loop()
pygame.quit()
