import pygame
from ui.MenuGauge import MenuGauge

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
