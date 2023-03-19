import pygame

class Sky():
	def __init__(self, window_size):
		self.image = pygame.image.load('assets/images/sky.png')
		self.image = pygame.transform.scale(self.image, window_size)
		self.rect = self.image.get_rect()
		self.image_asset = self.image.copy()
		self.speed = 1
		self.x = window_size[0]

	def update(self):
		self.image.blit(self.image_asset, (self.x, 0))
		self.image.blit(self.image_asset, (self.x - self.image_asset.get_width(), 0))
		self.x -= self.speed
		if self.x <= 0:
			self.x = self.image_asset.get_width()

	def draw(self, window):
		window.blit(self.image, self.rect)