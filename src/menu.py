import pygame
from ui.Button import Button
from core.Character import Character
from ui.CharacterSelect import CharacterSelect
from ui.MenuCharacterCard import MenuCharacterCard
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# 0 for main menu, 1 for character select
menu_section = 0
def set_menu_section(section):
	global menu_section
	menu_section = section

def quit():
	global running
	running = False

efrei_card = pygame.image.load('assets/ui/efrei.png')
efrei_card = efrei_card.convert_alpha()

play_btn = Button(390, 260, 'Play!', lambda: set_menu_section(1), 500)
tutorial_btn = Button(390, 360, 'Tutorial', lambda: print('Tutorial'), 500)
quit_btn = Button(390, 460, 'Quit', quit, 500)
logo = pygame.image.load('assets/logo.png')
logo_rect = logo.get_rect()
logo_rect.centerx = 640
logo_rect.y = 30

pink = Character('Pink', 'assets/ui/characters/pink.png', 'pygame sucks', {'strength': 0.4, 'speed': 0.8, 'weight': 0.5, 'accuracy': 0.94}, 'runs fast')
blue = Character('Blue', 'assets/ui/characters/blue.png', 'trash pygame', {'strength': 0.2, 'speed': 0.9, 'weight': 0.7, 'accuracy': 1}, 'jumps high')
white = Character('White', 'assets/ui/characters/white.png', 'laissez moi mourir', {'strength': 0.95, 'speed': 0.4, 'weight': 0.9, 'accuracy': 0.2}, 'zzccmxtp')


character_select = CharacterSelect([pink, blue, white])

card1 = MenuCharacterCard(character_select.characters[character_select.p1_selection])
card2 = MenuCharacterCard(character_select.characters[character_select.p2_selection], 'bottom')

p1_kb = pygame.image.load('assets/ui/zqsd.png')
p2_kb = pygame.image.load('assets/ui/ijkl.png')
indicator_font = pygame.font.Font('assets/grobold.ttf', 14)
p1_indictor_render = indicator_font.render('Player 1:', True, (255, 255, 255))
p1_indictor_rect = p1_indictor_render.get_rect()
p1_indictor_rect.bottom = 710
p1_indictor_rect.left = 10

p2_indictor_render = indicator_font.render('Player 2:', True, (255, 255, 255))
p2_indictor_rect = p2_indictor_render.get_rect()
p2_indictor_rect.bottom = 710
p2_indictor_rect.left = p1_indictor_rect.right + 78

dim = pygame.Surface((1280, 720))
dim.fill((0, 0, 0))
dim.set_alpha(150)
ready_font = pygame.font.Font('assets/grobold.ttf', 100)
ready_render = ready_font.render('Ready?', True, (255,255,255))
ready_render = pygame.transform.rotozoom(ready_render, 8, 1)
ready_rect = ready_render.get_rect()
ready_rect.center = (640, 360)


# == Efrei logo intro ==
running = True

intro_step = 0
alpha = 254
hold = 0
while running and alpha < 255:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				alpha = 500
	window.blit(efrei_card, (0, 0))
	dim.set_alpha(alpha)
	window.blit(dim, (0, 0))
	clock.tick(60)
	pygame.display.update()
	if intro_step == 0:
		alpha-=3
		if alpha <= 1:
			intro_step = 1
	elif intro_step == 1:
		hold+=1
		if hold >= 60:
			intro_step = 2
	else:
		alpha+=2


# == Menu loop ==
ready = False
while running:
	window.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if ready:
					ready = False
				elif menu_section > 0:
					set_menu_section(menu_section-1)
			if event.key == pygame.K_RETURN:
				if not ready:
					ready = True
				else:
					print('Game launched')
					set_menu_section(0)
					ready = False				
		if menu_section == 0:
			play_btn.update(event)
			tutorial_btn.update(event)
			quit_btn.update(event)
		else:
			character_select.handle_input(event)
			card1.update(character_select.characters[character_select.p1_selection])
			card2.update(character_select.characters[character_select.p2_selection])

	if menu_section == 0:
		window.blit(logo, logo_rect)
		play_btn.draw(window)
		tutorial_btn.draw(window)
		quit_btn.draw(window)
	else:
		character_select.draw(window)
		card1.draw(window)
		card2.draw(window)
		window.blit(p1_kb, (p1_indictor_rect.right + 10, 710 - p1_kb.get_height()))
		window.blit(p1_indictor_render, p1_indictor_rect)
		window.blit(p2_kb, (p2_indictor_rect.right + 10, 710 - p2_kb.get_height()))
		window.blit(p2_indictor_render, p2_indictor_rect)
		if ready:
			dim = pygame.Surface((1280, 720))
			dim.fill((0, 0, 0))
			dim.set_alpha(150)
			window.blit(dim, (0, 0))
			window.blit(ready_render, ready_rect)
	clock.tick(60)

	pygame.display.update()