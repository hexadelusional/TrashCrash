import pygame

class Floor(pygame.sprite.Sprite):
	def __init__(self, height, window_size):
		super().__init__()
		self.image = pygame.Surface((window_size[0], height))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = window_size[1] - height
		self.rect.width = window_size[0]
		self.rect.height = height
		platform_image = pygame.image.load('assets/images/floor.png')
		for i in range(0, self.rect.width, platform_image.get_width()):
			for j in range(0, height, platform_image.get_height()):
				self.image.blit(platform_image, (i, j))
		