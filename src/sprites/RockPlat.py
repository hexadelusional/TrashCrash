from random import randint, random
import pygame

class MyRockPlatform(pygame.sprite.Sprite):
	def __init__(self, image, dir, x, y, width):
		super().__init__()
		self.image = pygame.transform.scale(image, (width, 65))
		self.rect = self.image.get_rect()
		self.direction = dir
		self.rect.x = x
		self.rect.y = y
		self.speed = 0.7 + random()
		

	def update(self, window_width):
		self.rect.x -= self.speed * self.direction
		
		if self.rect.left < 0 or self.rect.right > window_width : 
			self.direction *= -1

	def draw(self, window):
		window.blit(self.image, self.rect)

