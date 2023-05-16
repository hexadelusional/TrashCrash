import pygame
from pygame.locals import *

from core.Character import Character
from core.Scene import Scene
from ui.Button import Button
from ui.CharacterSelect import CharacterSelect
from ui.MenuCharacterCard import MenuCharacterCard


def on_enter(scene):
	if not pygame.mixer.music.get_busy():
		pygame.mixer.music.load('assets/music/menu.mp3')
		pygame.mixer.music.play(-1)
	scene.menu_section = 0
	scene.ready = False
	scene.bg = pygame.image.load('assets/ui/menu_background.png')
	# Section 0 : Main menu
	scene.logo = pygame.image.load('assets/logo.png')
	scene.logo_rect = scene.logo.get_rect()
	scene.logo_rect.centerx = 640
	scene.logo_rect.y = 30
	scene.play_btn = Button(390, 260, 'Play!', lambda: setattr(scene, 'menu_section', 1), 500)
	scene.tutorial_btn = Button(390, 360, 'Credits', lambda: scene.switcher.switch_to('credits'), 500)
	scene.quit_btn = Button(390, 460, 'Quit', quit, 500)
	# Section 1 : Character select
	# - Body
	pink = Character('Pink', 'assets/ui/characters/pink.png', 'The Pink Bolt', {'strength': 0.4, 'speed': 0.8, 'weight': 0.5, 'accuracy': 0.94}, 'Runs fast')
	blue = Character('Blue', 'assets/ui/characters/blue.png', 'The Blue Rabbit', {'strength': 0.2, 'speed': 0.9, 'weight': 0.7, 'accuracy': 1}, 'Jumps high')
	white = Character('White', 'assets/ui/characters/white.png', 'The White Bodybuilder', {'strength': 0.95, 'speed': 0.4, 'weight': 0.9, 'accuracy': 0.2}, 'Throws hard')
	scene.character_select = CharacterSelect([pink, blue, white])
	scene.card1 = MenuCharacterCard(scene.character_select.characters[scene.character_select.p1_selection])
	scene.card2 = MenuCharacterCard(scene.character_select.characters[scene.character_select.p2_selection], 'bottom')
	# - Footer
	scene.p1_kb = pygame.image.load('assets/ui/zqsd.png')
	scene.p2_kb = pygame.image.load('assets/ui/ijkl.png')
	indicator_font = pygame.font.Font('assets/grobold.ttf', 14)
	scene.p1_indictor_render = indicator_font.render('Player 1:', True, (255, 255, 255))
	scene.p1_indictor_rect = scene.p1_indictor_render.get_rect()
	scene.p1_indictor_rect.bottom = 710
	scene.p1_indictor_rect.left = 10
	scene.p2_indictor_render = indicator_font.render('Player 2:', True, (255, 255, 255))
	scene.p2_indictor_rect = scene.p2_indictor_render.get_rect()
	scene.p2_indictor_rect.bottom = 710
	scene.p2_indictor_rect.left = scene.p1_indictor_rect.right + 78
	# - Hover text
	ready_font = pygame.font.Font('assets/grobold.ttf', 100)
	scene.ready_render = ready_font.render('Ready?', True, (255,255,255))
	scene.ready_render = pygame.transform.rotozoom(scene.ready_render, 8, 1)
	scene.ready_rect = scene.ready_render.get_rect()
	scene.ready_rect.center = (640, 360)

def on_loop(scene, window):
	window.blit(scene.bg, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if scene.ready:
					scene.ready = False
				elif scene.menu_section > 0:
					scene.menu_section -= 1
			if event.key == pygame.K_RETURN:
				if not scene.ready:
					scene.ready = True
				else:
					scene.switcher.switch_to('game', {
						'p1': scene.character_select.characters[scene.character_select.p1_selection],
						'p2': scene.character_select.characters[scene.character_select.p2_selection]
					})
					scene.ready = False
					return

		if scene.menu_section == 0:
			scene.play_btn.update(event)
			scene.tutorial_btn.update(event)
			scene.quit_btn.update(event)
		else:
			scene.character_select.handle_input(event)
			scene.card1.update(scene.character_select.characters[scene.character_select.p1_selection])
			scene.card2.update(scene.character_select.characters[scene.character_select.p2_selection])
	
	if scene.menu_section == 0:
		window.blit(scene.logo, scene.logo_rect)
		scene.play_btn.draw(window)
		scene.tutorial_btn.draw(window)
		scene.quit_btn.draw(window)
	else:
		scene.character_select.draw(window)
		scene.card1.draw(window)
		scene.card2.draw(window)
		window.blit(scene.p1_kb, (scene.p1_indictor_rect.right + 10, 710 - scene.p1_kb.get_height()))
		window.blit(scene.p1_indictor_render, scene.p1_indictor_rect)
		window.blit(scene.p2_kb, (scene.p2_indictor_rect.right + 10, 710 - scene.p2_kb.get_height()))
		window.blit(scene.p2_indictor_render, scene.p2_indictor_rect)
		if scene.ready:
			dim = pygame.Surface((1280, 720))
			dim.fill((0, 0, 0))
			dim.set_alpha(150)
			window.blit(dim, (0, 0))
			window.blit(scene.ready_render, scene.ready_rect)

main_menu_scene = Scene(on_enter, on_loop)