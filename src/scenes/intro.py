import pygame

from core.Scene import Scene


def on_enter(scene):
	scene.efrei_card = pygame.image.load('assets/ui/efrei.png')
	scene.efrei_card = scene.efrei_card.convert_alpha()
	scene.dim = pygame.Surface((1280, 720))
	scene.dim.fill((0, 0, 0))
	scene.dim.set_alpha(150)
	scene.alpha = 254
	scene.step = 0
	scene.hold = 0

def on_loop(scene, window):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
				scene.switcher.switch_to('main_menu')
				return

	if scene.alpha >= 255:
		scene.switcher.switch_to('main_menu')
		return

	window.blit(scene.efrei_card, (0, 0))
	scene.dim.set_alpha(scene.alpha)
	window.blit(scene.dim, (0, 0))
	if scene.step == 0:
		scene.alpha-=3
		if scene.alpha <= 1:
			scene.step = 1
	elif scene.step == 1:
		scene.hold+=1
		if scene.hold >= 60:
			scene.step = 2
	else:
		scene.alpha+=2

intro_scene = Scene(on_enter, on_loop)