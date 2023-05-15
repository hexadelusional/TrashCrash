from random import randint, choice
import pygame

IMAGES = [pygame.image.load(f'assets/images/platforms/{i}.png') for i in range(3)]

class Platform(pygame.sprite.Sprite):
	def __init__(self, window_width, rock_list_left, rock_list_right):
		super().__init__()
		self.side = randint(0, 1)
		bounds = [(0, window_width//2), (window_width//2,window_width)]
		self.image = choice(IMAGES)
		self.rect = self.image.get_rect()
		self.rect.x = randint(bounds[self.side][0],bounds[self.side][1])
		if not(self.side) and not(rock_list_left) or self.side and not(rock_list_right):
			self.rect.y = 520
		elif not(self.side):
			self.rect.y = rock_list_left[-1].rect.top - 120
		else:
			self.rect.y = rock_list_right[-1].rect.top - 120
		self.rect.height = 5

	def draw(self, window):
		window.blit(self.image, self.rect)