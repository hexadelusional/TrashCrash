import pygame

particles = {
	'run': {
		'sprite': pygame.image.load('assets/images/particles/run.png'),
		'frames': 6
	},
	'jump': {
		'sprite': pygame.image.load('assets/images/particles/jump.png'),
		'frames': 5
	},
}

class Particle:
	SPRITE_SIZE = (32, 32)
	def __init__(self, name, x, y, w, h, mirror=False):
		self.name = name
		self.x = x
		self.y = y
		self.mirror = mirror
		self.frame = 0
		self.sprite = particles[name]['sprite']
		self.frames = particles[name]['frames']
		self.width = w
		self.height = h
		self.speed = 2
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def update(self):
		if self.frame < self.frames * self.speed:
			self.frame += 1

	def draw(self, window):
		image = pygame.transform.scale(self.sprite.subsurface(self.frame // self.speed * Particle.SPRITE_SIZE[0], 0, Particle.SPRITE_SIZE[0], Particle.SPRITE_SIZE[1]), (self.width, self.height))
		if self.mirror:
			image = pygame.transform.flip(image, True, False)
		window.blit(image, (self.x, self.y))
	
	def is_finished(self):
		return self.frame == self.frames * self.speed
