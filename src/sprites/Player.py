import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load('assets/images/player/idle/0.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.width = 64
		self.rect.height = 128
		self.can_double_jump = True
		self.vel_x = 0
		self.vel_y = 0
		self.acc_x = 0
		self.acc_y = 0.5 # Gravity factor
		self.animations = {
			'idle': [pygame.image.load(f'assets/images/player/idle/{i}.png') for i in range(4)],
			'walk': [pygame.image.load(f'assets/images/player/walk/{i}.png') for i in range(4)],
			'jump': [pygame.image.load(f'assets/images/player/jump/{i}.png') for i in range(4)]
		}
		self.current_animation = 'idle'
		self.animation_frame = 0

	def apply_gravity(self):
		self.vel_y += self.acc_y

	def update(self, platforms):
		self.apply_gravity()

		self.rect.x += self.vel_x
		self.collide(platforms, direction="x")
		self.rect.y += self.vel_y
		self.collide(platforms, direction="y")
		if self.is_on_ground(platforms):
			self.can_double_jump = True
		self.animate()

	def draw(self, window):
		scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
		if self.vel_x < 0:
			scaled_image = pygame.transform.flip(scaled_image, True, False)
		window.blit(scaled_image, self.rect, (0, 0, self.rect.width, self.rect.height))


	def animate(self):
		animation_sequence = self.animations[self.current_animation]
		self.image = animation_sequence[self.animation_frame // 12] # 4 is the animation speed
		self.animation_frame += 1
		if self.animation_frame >= len(animation_sequence) * 12:
			self.animation_frame = 0

	def set_animation(self, animation_name):
		if self.current_animation != animation_name:
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
			self.set_animation('jump')
		elif self.can_double_jump:
			self.vel_y = -10
			self.can_double_jump = False
			self.set_animation('jump')


	def move_left(self):
		self.vel_x = -8
		self.set_animation('walk')

	def move_right(self):
		self.vel_x = 8
		self.set_animation('walk')

	def stop(self):
		self.vel_x = 0
		self.set_animation('idle')
