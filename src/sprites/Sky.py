import pygame

window_size = (1280, 720)
MOUNTAINS = [
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount1.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount2.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount3.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount4.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount5.png'), window_size),
]

SKIES = [
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/sky1.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/sky2.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/sky3.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/sky4.png'), window_size),
	pygame.transform.scale(pygame.image.load('assets/images/fond_1/sky5.png'), window_size),
]

class Sky():
	def __init__(self):
		super().__init__()
		self.image = SKIES[0]
		self.image.blit(MOUNTAINS[0], (0, 0))
		self.i = 0
		self.rect = self.image.get_rect()

	def update(self):
		self.i += 1
		if self.i >= len(MOUNTAINS):
			self.i = len(MOUNTAINS) - 1
		self.image = SKIES[self.i]
		self.image.blit(MOUNTAINS[self.i], (0, 0))

	def draw(self, window):
		window.blit(self.image, self.rect)