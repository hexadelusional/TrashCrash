from random import randint
import pygame

class Rock_platform(pygame.sprite.Sprite):
	def __init__(self, window_size):
		super().__init__()
		self.image = pygame.image.load(f'assets/images/rock_platforms/{randint(1,2)}.png')
		self.rect = self.image.get_rect()
		self.rect.x = window_size[0]
		self.rect.y = randint(200, window_size[1] - self.rect.height - 100)
		self.speed = 0.7 + randint(0, 1)

	def update(self):
		self.rect.x -= self.speed

	def draw(self, window):
		window.blit(self.image, self.rect)
s