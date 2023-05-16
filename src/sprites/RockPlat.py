import pygame


class MyRockPlatform(pygame.sprite.Sprite):
	def __init__(self, window_width, side, rock_list_left, rock_list_right):
		super().__init__()
		self.image = pygame.image.load('assets/images/rock_platforms/1.png')
		self.rect = self.image.get_rect()
		self.side = side
		if not(self.side) :
			self.rect.x = 20 + len(rock_list_left)*self.rect.width
		else :
			self.rect.x = window_width - 20 - (len(rock_list_right)+1)*self.rect.width

		if not(self.side) and not(rock_list_left) or self.side and not(rock_list_right) : 
			self.rect.y = 520
		elif not(self.side) : 
			self.rect.y = rock_list_left[-1].rect.top - 120
		else : 
			self.rect.y = rock_list_right[-1].rect.top - 120
		self.rect.height = 5
	

	def draw(self, window):
		window.blit(self.image, self.rect)

