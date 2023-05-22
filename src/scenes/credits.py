import pygame
from core.Scene import Scene
from ui.Button import Button

image = pygame.image.load('assets/ui/credits.png')

def on_enter(scene):
	scene.back = Button(10, 10, 'Back', lambda: scene.switcher.switch_to('main_menu'), font_size=20)

def on_loop(scene, window):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
				scene.switcher.switch_to('main_menu')
				return
		scene.back.update(event)
	
	window.blit(image, (0, 0))
	scene.back.draw(window)

credits_scene = Scene(on_enter, on_loop)