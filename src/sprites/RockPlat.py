from random import randint, random
import pygame




class MyRockPlatform(pygame.sprite.Sprite):
	def __init__(self, image, window_width, rock_list):
		super().__init__()
		val = randint(0, 1)
		self.image = image
		self.rect = self.image.get_rect()
		self.direction = [-1, 1][val]
		self.rect.x = [window_width - self.rect.width, 0][val]
		self.rect.y = 520 if not rock_list else rock_list[-1].rect.top - 120
		self.rect.height = 5
		self.speed = 0.7 + random()
		
		

	def update(self, window_width):
		self.rect.x -= self.speed * self.direction
		
		if self.rect.left < 0 or self.rect.right > window_width : 
			self.direction *= -1

	def draw(self, window):
		window.blit(self.image, self.rect)

