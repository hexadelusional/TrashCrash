import pygame
import math

IMAGE = pygame.image.load('assets/images/projectile.png')

class Projectile(pygame.sprite.Sprite):
	instances = pygame.sprite.Group()
	def __init__(self, x, y, gauge_value, angle, mirror, trash):
		super().__init__()
		self.image = trash.image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.acc_y = 0.5 # Gravity
		self.vel_y = -(5 + (gauge_value / 100) * math.sin(angle * math.pi / 180) * 20)
		self.vel_x = (5 + (gauge_value / 100) * math.cos(angle * math.pi / 180) * 5) * (-1 if mirror else 1)
		Projectile.instances.add(self)

	def apply_gravity(self):
		self.vel_y += self.acc_y

	def collide(self, platforms, direction):
		if direction == 'y':
			for platform in platforms:
				if self.rect.colliderect(platform.rect):
					if self.vel_y > 0:
						self.rect.bottom = platform.rect.top
					elif self.vel_y < 0:
						self.rect.top = platform.rect.bottom
					self.vel_y = -self.vel_y * 0.5
					self.vel_x *= 0.5
					if abs(self.vel_y) < 1.2:
						self.vel_y = 0
		elif direction == 'x':
			for platform in platforms:
				if self.rect.colliderect(platform.rect):
					if self.vel_x > 0:
						self.rect.right = platform.rect.left
					elif self.vel_x < 0:
						self.rect.left = platform.rect.right
					self.vel_x = -self.vel_x * 0.5


	def update(self, platforms):
		self.apply_gravity()
		self.rect.x += self.vel_x
		self.collide(platforms, 'x')
		self.rect.y += self.vel_y
		self.collide(platforms, 'y')
	
	def draw(self, window):
		window.blit(self.image, (self.rect.x, self.rect.y))