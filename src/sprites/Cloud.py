from random import randint
import pygame

class Cloud():
	def __init__(self, window_size):
		self.image = pygame.image.load(f'assets/images/dark_clouds/{randint(0,5)}.png')
		self.rect = self.image.get_rect()
		val = randint(0, 1)
		self.direction = [-1, 1][val]
		self.rect.x = [window_size[0] - self.rect.width, 0][val]
		self.rect.y = randint(0, window_size[1] - self.rect.height - 500)
		self.speed = 1 + randint(0, 1)

	def update(self):
		self.rect.x += self.speed * self.direction	

	def draw(self, window):
		window.blit(self.image, self.rect)