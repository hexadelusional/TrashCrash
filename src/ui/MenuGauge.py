import pygame

class MenuGauge():
	def __init__(self,x, y, value):
		self.x = x
		self.y = y
		self.value = value
		self.rect = pygame.Rect(self.x, self.y, 200, 4)

	def draw(self, window):
		pygame.draw.rect(window, pygame.Color(240, 188, 192), self.rect, border_radius=100)
		pygame.draw.rect(window, pygame.Color(201, 44, 57), pygame.Rect(self.x, self.y, self.value * self.rect.width, 4), border_radius=100)