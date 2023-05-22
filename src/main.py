import pygame
from core.Character import Character

from core.SceneSwitcher import SceneSwitcher
from scenes.game import game_scene
from scenes.intro import intro_scene
from scenes.menu import main_menu_scene
from scenes.credits import credits_scene

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
switcher.add_scene('credits', credits_scene)
switcher.add_scene('game', game_scene)

pink = Character('Pink', 'assets/ui/characters/pink.png', 'The Pink Bolt', {'strength': 0.4, 'speed': 0.8, 'weight': 0.5, 'accuracy': 0.94}, 'Runs fast')
blue = Character('Blue', 'assets/ui/characters/blue.png', 'The Blue Rabbit', {'strength': 0.2, 'speed': 0.9, 'weight': 0.7, 'accuracy': 1}, 'Jumps high')
white = Character('White', 'assets/ui/characters/white.png', 'The White Bodybuilder', {'strength': 0.95, 'speed': 0.4, 'weight': 0.9, 'accuracy': 0.2}, 'Throws hard')
	
switcher.switch_to('game', {'p1': pink, 'p2': white})

running = True
while running:
    for event in pygame.event.get(eventtype=pygame.QUIT):
        running = False
    switcher.loop()

pygame.quit()
