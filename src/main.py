from functools import partial

import pygame

from core.SceneSwitcher import SceneSwitcher
from scenes.game import game_scene

# Initialize game window
pygame.init()
WINDOW_SIZE = (1280, 720)
icon = pygame.image.load('assets/icon.png')
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Trash Crash')
pygame.display.set_icon(icon)
debug_font = pygame.font.SysFont('Arial', 20)

switcher = SceneSwitcher(window)
switcher.add_scene('game', game_scene)
switcher.switch_to('game', {})

running = True
while running:
    switcher.loop()
    for event in pygame.event.get(eventtype=pygame.QUIT):
        running = False
pygame.quit()
