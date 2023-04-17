import pygame
from sprites.Gauge import Gauge
from sprites.Arrow import Arrow
from sprites.Particle import Particle
from sprites.Projectile import Projectile

class Player(pygame.sprite.Sprite):
	SPRITE_SIZE = (32, 32)
	def __init__(self, skin, id, x, y):
		super().__init__()
		self.skin = skin
		self.id = id
		self.rect = pygame.Rect(x, y, 64, 64)
		self.image = pygame.Surface(Player.SPRITE_SIZE)
		self.image.set_alpha(255)
		self.vel_x = 0
		self.vel_y = 0
		self.acc_y = 0.5 # Gravity factor
		self.can_double_jump = True
		self.mirror = False
		self.throwing = False
		self.animation_speed = 8
		self.particles = []
		self.gauge = Gauge(self.rect.x, self.rect.y)
		self.arrow = Arrow(self.rect.x, self.rect.y, self.id)
		self.animations = {
			'idle': pygame.image.load(f'assets/images/player/idle/{self.skin}.png'),
			'run': pygame.image.load(f'assets/images/player/run/{self.skin}.png'),
			'jump': pygame.image.load(f'assets/images/player/jump/{self.skin}.png'),
			'pre_throw': pygame.image.load(f'assets/images/player/throw/{self.skin}.png'),
			'throw': pygame.image.load(f'assets/images/player/throw/{self.skin}.png')
		}
		# Amount of frames in each animation
		self.animation_frames = {
			'idle': 4,
			'run': 6,
			'jump': 8,
			'pre_throw': 2,
			'throw': 4
		}
		self.current_animation = 'idle'
		self.current_frame = 0

	def apply_gravity(self):
		self.vel_y += self.acc_y

	def update(self, platforms):
		self.apply_gravity()
		gauge_x = self.rect.x + self.rect.width + 5 if self.mirror else self.rect.x - 5
		arrow_x = self.rect.x + self.rect.width - 5 if self.mirror else self.rect.x + 5
		self.gauge.update(gauge_x, self.rect.y)
		self.arrow.update(arrow_x, self.rect.y-30)
		for particle in self.particles:
			particle.update()
			if particle.is_finished():
				self.particles.remove(particle)
		if not self.throwing:
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
		if self.throwing:
			self.gauge.draw(window)
			self.arrow.draw(window)


	def animate(self):
		sequence = self.animations[self.current_animation]
		self.image.fill((0, 0, 0, 0))
		self.image.blit(sequence, (0, 0), (self.current_frame // self.animation_speed * self.SPRITE_SIZE[0], 0, self.SPRITE_SIZE[0], self.SPRITE_SIZE[1]))
		self.current_frame += 1
		if self.current_frame == self.animation_frames[self.current_animation] * self.animation_speed:
			if self.current_animation == 'throw':
				self.set_animation('idle')
			self.current_frame = 0

	def set_animation(self, animation_name, speed = 8):
		self.current_animation = animation_name
		self.animation_speed = speed
		self.current_frame = 0

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
		if self.throwing:
			return
		if self.is_on_ground(platforms):
			self.vel_y = -10
		elif self.can_double_jump:
			self.vel_y = -10
			self.can_double_jump = False
			self.particles.append(Particle('jump', self.rect.x, self.rect.y, 64, 64))


	def move(self, platforms, direction):
		if self.throwing:
			return
		self.vel_x = 8 * (-1 if direction == 'left' else 1)
		self.mirror = direction == 'left'
		if self.is_on_ground(platforms):
			self.particles.append(Particle('run', self.rect.x, self.rect.y, 64, 64, self.mirror))
		self.set_animation('run')

	def stop(self, direction):
		if self.throwing:
			return
		if direction == 'left' and self.vel_x < 0 or direction == 'right' and self.vel_x > 0:
			self.vel_x = 0
			self.set_animation('idle')
		if self.vel_x == 0:
			self.set_animation('idle')

	def throw(self, platforms):
		#part for the particle
		if not self.is_on_ground(platforms):
			return
		if not self.throwing:
			self.stop('left')
			self.stop('right')
			self.throwing = True
			self.set_animation('pre_throw', 24)
		else:
			self.throwing = False
			self.set_animation('throw')
			vel_x = (4 + 5 * self.gauge.value / 100) * (-1 if self.mirror else 1)
			vel_y = -5 - 15 * self.gauge.value / 100
			Projectile(self.rect.x, self.rect.y, vel_x, vel_y)
		#part for the arrow



