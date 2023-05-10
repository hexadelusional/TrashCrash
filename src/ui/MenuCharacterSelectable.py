import pygame

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
