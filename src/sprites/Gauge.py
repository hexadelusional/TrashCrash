import pygame

class Gauge():
	def __init__(self, x, y): 
		self.x = x
		self.y = y
		self.width = 10
		self.height = 40
		self.padding = 2
		self.value = 0
		self.direction = 4
		self.max_value = 100
		self.color = (63, 234, 42)
	
	def update(self, x, y):
		self.x = x
		self.y = y
		self.value += self.direction
		if self.value >= self.max_value:
			self.value = self.max_value
			self.direction *= -1
		elif self.value <= 0:
			self.value = 0
			self.direction*=-1
	
	def draw(self, window):
		pygame.draw.rect(window, (15, 15, 15), (self.x - self.padding, self.y - self.padding, self.width + self.padding * 2, self.height + self.padding * 2))
		y = (self.y + self.height) - (self.height * (self.value / self.max_value))
		pygame.draw.rect(window, self.color, (self.x, y, self.width, self.height * (self.value / self.max_value)))