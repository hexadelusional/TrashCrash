import pygame

from core.Scene import Scene


def on_enter(scene):
	scene.font = pygame.font.Font(None, 30)
	scene.bg = pygame.image.load('assets/ui/menu_background.png')

def on_loop(scene, window):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
				scene.switcher.switch_to('main_menu')
				return
	
	window.blit(scene.bg, (0, 0))
	text = scene.font.render('Credits', True, (255, 255, 255))
	window.blit(text, (210, 300))
	text = scene.font.render('iri paul coco adele maxime ^^', True, (255, 255, 255))
	window.blit(text, (210, 340))

credits_scene = Scene(on_enter, on_loop)