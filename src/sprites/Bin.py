import pygame

BIN_DIMENSIONS = (80, 80)
IMAGES = {
	'blue': pygame.transform.scale(pygame.image.load('assets/images/bins/blue.png'), BIN_DIMENSIONS),
	'red': pygame.transform.scale(pygame.image.load('assets/images/bins/red.png'), BIN_DIMENSIONS),
	'yellow': pygame.transform.scale(pygame.image.load('assets/images/bins/yellow.png'), BIN_DIMENSIONS)
}

class Bin(pygame.sprite.Sprite):
	def __init__(self, x, y, color):
		super().__init__()
		self.image = IMAGES[color]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	   
	def draw(self, window):
		window.blit(self.image, self.rect, (0, 0, self.rect.width, self.rect.height))