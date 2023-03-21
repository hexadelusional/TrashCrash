import pygame

from sprites.Particle import Particle

class Player(pygame.sprite.Sprite):
	SPRITE_SIZE = (32, 32)
	def __init__(self, skin, x, y):
		super().__init__()
		self.skin = skin
		self.rect = pygame.Rect(0, 0, 64, 64)
		self.rect.x = x
		self.rect.y = y
		self.image = pygame.Surface(Player.SPRITE_SIZE)
		self.image.set_alpha(255)
		self.particles = []
		self.can_double_jump = True
		self.vel_x = 0
		self.vel_y = 0
		self.acc_x = 0
		self.acc_y = 0.5 # Gravity factor
		self.animation_speed = 8
		self.mirror = False
		self.animations = {
			'idle': pygame.image.load(f'assets/images/player/idle/{self.skin}.png'),
			'run': pygame.image.load(f'assets/images/player/run/{self.skin}.png'),
			'jump': pygame.image.load(f'assets/images/player/jump/{self.skin}.png'),
		}
		# Amount of frames in each animation
		self.animation_durations = {
			'idle': 4,
			'run': 6,
			'jump': 8,
		}
		self.current_animation = 'idle'
		self.animation_frame = 0

	def apply_gravity(self):
		self.vel_y += self.acc_y

	def update(self, platforms):
		self.apply_gravity()
		for particle in self.particles:
			particle.update()
			if particle.is_finished():
				self.particles.remove(particle)
		self.rect.x += self.vel_x
		self.collide(platforms, direction='x')
		self.rect.y += self.vel_y
		self.collide(platforms, direction='y')
		if self.is_on_ground(platforms):
			self.can_double_jump = True
			if self.current_animation == 'jump':
				self.set_animation('idle')
		self.animate()

	def draw(self, window):
		scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
		if self.mirror:
			scaled_image = pygame.transform.flip(scaled_image, True, False)
		window.blit(scaled_image, self.rect, (0, 0, self.rect.width, self.rect.height))
		for particle in self.particles:
			particle.draw(window)


	def animate(self):
		sequence = self.animations[self.current_animation]
		self.image.fill((0, 0, 0, 0))
		self.image.blit(sequence, (0, 0), (self.animation_frame // self.animation_speed * self.SPRITE_SIZE[0], 0, self.SPRITE_SIZE[0], self.SPRITE_SIZE[1]))
		self.animation_frame += 1
		if self.animation_frame == self.animation_durations[self.current_animation] * self.animation_speed:
			self.animation_frame = 0

	def set_animation(self, animation_name):
		self.current_animation = animation_name
		self.animation_frame = 0

	def collide(self, platforms, direction):
		for platform in platforms:
			if platform == self:
				continue
			if pygame.sprite.collide_rect(self, platform):
				if direction == 'x':
					if self.vel_x > 0:
						self.rect.right = platform.rect.left
					elif self.vel_x < 0:
						self.rect.left = platform.rect.right
					self.vel_x = 0
					self.set_animation('idle')
				if direction == 'y':
					if self.vel_y > 0:
						self.rect.bottom = platform.rect.top
					elif self.vel_y < 0:
						self.rect.top = platform.rect.bottom
					self.vel_y = 0

	def is_on_ground(self, platforms):
		self.rect.y += 1
		for platform in platforms:
			if platform == self:
				continue
			if pygame.sprite.collide_rect(self, platform):
				self.rect.y -= 1
				return True
		self.rect.y -= 1
		return False

	def jump(self, platforms):
		if self.is_on_ground(platforms):
			self.vel_y = -10
			#self.set_animation('jump')
		elif self.can_double_jump:
			self.vel_y = -10
			self.can_double_jump = False
			self.particles.append(Particle('jump', self.rect.x, self.rect.y, 64, 64))
			#self.set_animation('jump')


	def move_left(self, platforms):
		self.vel_x = -8
		self.mirror = True
		if self.is_on_ground(platforms):
			self.particles.append(Particle('run', self.rect.x, self.rect.y, 64, 64, True))
		self.set_animation('run')

	def move_right(self, platforms):
		self.vel_x = 8
		self.mirror = False
		if self.is_on_ground(platforms):
			self.particles.append(Particle('run', self.rect.x, self.rect.y, 64, 64))
		self.set_animation('run')

	def stop(self):
		self.vel_x = 0
		self.set_animation('idle')
