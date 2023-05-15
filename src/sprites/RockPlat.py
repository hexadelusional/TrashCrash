from random import randint
import pygame




class MyRockPlatform(pygame.sprite.Sprite):
	def __init__(self, window_width, rock_list_left, rock_list_right):
		super().__init__()
		self.image = pygame.image.load('assets/images/rock_platforms/1.png')
		self.rect = self.image.get_rect()
		self.side = randint(0, 1)
		bounds = [(0, window_width//2), (window_width//2,window_width-self.rect.width)]
		self.rect.x = randint(bounds[self.side][0],bounds[self.side][1])
		if not(self.side) and not(rock_list_left) or self.side and not(rock_list_right) : 
			self.rect.y = 520
		elif not(self.side) : 
			self.rect.y = rock_list_left[-1].rect.top - 120
		else : 
			self.rect.y = rock_list_right[-1].rect.top - 120
		self.rect.height = 5
	

	def draw(self, window):
		window.blit(self.image, self.rect)

