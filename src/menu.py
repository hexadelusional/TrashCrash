# This will be split into multiple files and merged with main project when scene system is implemented
import pygame
from pygame.locals import *

class Button(): 
	def __init__(self, x, y, text, action=None, width=None, font_size=32):
		self.x = x
		self.y = y
		self.text = text
		self.color = pygame.Color(52, 195, 235)
		self.text_color = pygame.Color(255, 255, 255)
		self.action = action
		self.font = pygame.font.Font('assets/grobold.ttf', font_size)
		self.text_render = self.font.render(self.text, True, self.text_color)
		self.text_rect = self.text_render.get_rect()
		if width is not None:
			self.text_rect.center = (self.x + (width / 2), self.y + 30)
		else:
			self.text_rect.topleft = (self.x + 10, self.y + 10)
		self.rect = pygame.Rect(self.x, self.y, width or self.text_rect.width + 20, self.text_rect.height + 20)

	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect, border_radius=10)
		window.blit(self.text_render, self.text_rect)

	def update(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				if self.action is not None:
					self.action()
		if event.type == pygame.MOUSEMOTION:
			if self.rect.collidepoint(event.pos):
				self.color = pygame.Color(255, 255, 255)
				self.text_color = pygame.Color(52, 195, 235)
				self.text_render = self.font.render(self.text, True, self.text_color)
			else:
				self.color = pygame.Color(52, 195, 235)
				self.text_color = pygame.Color(255, 255, 255)
				self.text_render = self.font.render(self.text, True, self.text_color)

class MenuCharacterCard():
	# Character should be implemented later on
	# It should have the following attributes: name, image, description, stats, [special_skill]
	def __init__(self, character, position='top'):
		self.character = character
		self.image = pygame.image.load(self.character.image)
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.rect = pygame.Rect(530, 370 if position == 'bottom' else 20, 730,  310)
		self.image_rect = self.image.get_rect()
		self.image_rect.center = (self.rect.x + self.image_rect.width / 2, self.rect.centery)
		self.title_font = pygame.font.Font('assets/grobold.ttf', 48)
		self.desc_font = pygame.font.Font('assets/grobold.ttf', 16)
		self.name_render = self.title_font.render(self.character.name, True, pygame.Color(0,0,0))
		self.name_rect = self.name_render.get_rect()
		self.name_rect.centerx = self.rect.centerx
		self.name_rect.y = self.rect.y + 10
		self.description_render = self.desc_font.render(self.character.description, True, pygame.Color(0,0,0))
		self.description_rect = self.description_render.get_rect()
		self.description_rect.centerx = self.rect.centerx
		self.description_rect.y = self.name_rect.bottom + 5
		self.skill_render = self.desc_font.render(self.character.special_skill, True, pygame.Color(0,0,0))
		self.skill_rect = self.skill_render.get_rect()
		self.skill_rect.centerx = self.rect.centerx
		self.skill_rect.y = self.rect.bottom - self.skill_rect.height - 10

	def update(self, character):
		self.character = character
		self.image = pygame.image.load(self.character.image)
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.name_render = self.title_font.render(self.character.name, True, pygame.Color(0,0,0))
		self.description_render = self.desc_font.render(self.character.description, True, pygame.Color(0,0,0))
		self.skill_render = self.desc_font.render(self.character.special_skill, True, pygame.Color(0,0,0))

	def render_stat(self, stat, x, y, window):
		stat_render = self.desc_font.render(stat, True, pygame.Color(0,0,0))
		stat_rect = stat_render.get_rect()
		stat_rect.topleft = (self.image_rect.right + x, self.description_rect.bottom + y)
		stat_gauge = MenuGauge(stat_rect.x, stat_rect.y + 20, self.character.stats[stat])
		window.blit(stat_render, stat_rect)
		stat_gauge.draw(window)

	def draw(self, window):
		# Main box
		pygame.draw.rect(window, pygame.Color(255, 255, 255), self.rect, border_radius=30)
		# Title / Description / Image
		window.blit(self.name_render, self.name_rect)
		window.blit(self.description_render, self.description_rect)
		window.blit(self.image, self.image_rect)
		# Stats
		self.render_stat('strength', 10, 50, window)
		self.render_stat('speed', 230, 50, window)
		self.render_stat('weight', 10, 90, window)
		self.render_stat('accuracy', 230, 90, window)
		# Special skill
		window.blit(self.skill_render, self.skill_rect)

class MenuGauge():
	def __init__(self,x, y, value):
		self.x = x
		self.y = y
		self.value = value
		self.rect = pygame.Rect(self.x, self.y, 200, 4)

	def draw(self, window):
		pygame.draw.rect(window, pygame.Color(240, 188, 192), self.rect, border_radius=100)
		pygame.draw.rect(window, pygame.Color(201, 44, 57), pygame.Rect(self.x, self.y, self.value * self.rect.width, 4), border_radius=100)


class Character(): # Placeholder, will be replaced with actual character class later on
	def __init__(self, name, image, description, stats, special_skill=None):
		self.name = name
		self.image = image
		self.description = description
		self.stats = stats
		self.special_skill = special_skill

class MenuCharacterSelectable():
	def __init__(self, character, index, x, y):
		self.index = index
		self.character = character
		self.rect = pygame.Rect(x, y, 64, 64)
		self.image = pygame.image.load(f'assets/ui/characters/{self.character}.png')
		self.image = pygame.transform.scale(self.image, (55, 55))
		self.image_rect = (x + 4, y + 4, 55, 55)
		self.font = pygame.font.Font('assets/grobold.ttf', 12)

	def draw(self, window, p1_selection, p2_selection):
		window.blit(self.image, self.image_rect)
		pygame.draw.rect(window, pygame.Color('white'), self.rect, 3, border_radius=10)
		if self.index == p1_selection:
			center = pygame.Vector2(self.rect.x + 5, self.rect.y + 5)
			pygame.draw.circle(window, pygame.Color(201, 44, 57), center, 10)
			text = self.font.render('1', True, pygame.Color(255, 255, 255))
			window.blit(text, (center.x - text.get_width() / 2, center.y - text.get_height() / 2))
		if self.index == p2_selection:
			center = pygame.Vector2(self.rect.x + self.rect.width - 5, self.rect.y + 5)
			pygame.draw.circle(window, pygame.Color(42, 209, 13), center, 10)
			text = self.font.render('2', True, pygame.Color(255, 255, 255))
			window.blit(text, (center.x - text.get_width() / 2, center.y - text.get_height() / 2))

class CharacterSelect(): 
	def __init__(self, characters):
		self.characters = characters
		self.p1_selection = 0
		self.p2_selection = 1
		self.selectables = []
		for (i, character) in enumerate(self.characters):
			self.selectables.append(MenuCharacterSelectable(character.name.lower(), i, 63 + i * 100, 328))

	def draw(self, window):
		for selectable in self.selectables:
			selectable.draw(window, self.p1_selection, self.p2_selection)

	def handle_input(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				self.p1_selection = (self.p1_selection - 1) % len(self.characters)
			if event.key == pygame.K_d:
				self.p1_selection = (self.p1_selection + 1) % len(self.characters)
			if event.key == pygame.K_j:
				self.p2_selection = (self.p2_selection - 1) % len(self.characters)
			if event.key == pygame.K_l:
				self.p2_selection = (self.p2_selection + 1) % len(self.characters)

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