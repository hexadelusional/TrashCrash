import pygame

window_size = (1280, 720)
MOUNTAINS = {
	'mount1': pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount1.png'), window_size),
	'mount2': pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount2.png'), window_size),
	'mount3': pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount3.png'), window_size),
	'mount4': pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount4.png'), window_size),
	'mount5': pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount5.png'), window_size),
}

class Sky():
	def __init__(self, landscape):
		super().__init__()
		self.image = MOUNTAINS[landscape]
		self.rect = self.image.get_rect()
		self.image_asset = self.image.copy()
		self.speed = 0.5
		self.x = window_size[0]

	def update(self):
		self.image.blit(self.image_asset, (self.x, 0))
		self.image.blit(self.image_asset, (self.x - self.image_asset.get_width(), 0))
		self.x -= self.speed
		if self.x <= 0:
			self.x = self.image_asset.get_width()

	def draw(self, window):
		window.blit(self.image, self.rect)