import pygame
from sprites.Gauge import Gauge
from sprites.Arrow import Arrow
from sprites.Particle import Particle
from sprites.Projectile import Projectile
from core.Sound import Sound
from sprites.Score import Score

WINDOW_SIZE = (1280, 720)
PLAYER_ANIMATIONS = {}
def get_animation_frames(skin, animation):
	if animation == 'pre_throw':
		animation = 'throw'
	if f'{skin}_{animation}' not in PLAYER_ANIMATIONS:
		PLAYER_ANIMATIONS[f'{skin}_{animation}'] = pygame.image.load(f'assets/images/player/{animation}/{skin}.png')
	return PLAYER_ANIMATIONS[f'{skin}_{animation}']

# Amount of frames in each animation
ANIMATION_FRAMES = {
	'idle': 4,
	'run': 6,
	'jump': 8,
	'pre_throw': 2,
	'throw': 4
}

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
		self.score = Score(WINDOW_SIZE, 'left' if self.id == 1 else 'right')
		self.mirror = False
		self.has_trash = False
		self.held_trash = None
		self.throwing = False
		self.animation_speed = 8
		self.particles = []
		self.gauge = Gauge(self.rect.x, self.rect.y)
		self.arrow = Arrow(self.rect.x, self.rect.y, self.id)
		self.current_animation = 'idle'
		self.current_frame = 0
		self.music = Sound() #we have to define the sound here to implement other sounds as jump1, jump2

	def apply_gravity(self):
		self.vel_y += self.acc_y

	def update(self, platforms):
		self.apply_gravity()
		gauge_x = self.rect.x + self.rect.width + 5 if self.mirror else self.rect.x - 5
		arrow_x = self.rect.x + self.rect.width + 5 if self.mirror else self.rect.x - 5
		self.gauge.update(gauge_x, self.rect.y)
		self.arrow.update(arrow_x, self.rect.y)
		if self.rect.y > 720:
			self.rect.y = 0
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
			self.arrow.draw(window, self.mirror)

	def draw_inventory(self, window):
		x = 50 if self.id == 1 else (1280 - 100)
		SIZE = 50
		dimmed_rect = pygame.Surface((SIZE - 3, SIZE - 3))
		dimmed_rect.set_alpha(100)
		dimmed_rect.fill((0, 0, 0))
		window.blit(dimmed_rect, (x + 2, 100 + 2))
		pygame.draw.rect(window, (255, 255, 255), (x, 100, SIZE, SIZE), width=3, border_radius=5)

		if self.has_trash:
			w_ratio = 40 / self.held_trash.rect.width
			h_ratio = 40 / self.held_trash.rect.height
			ratio = min(w_ratio, h_ratio)
			scaled_image = pygame.transform.scale(self.held_trash.image, (int(self.held_trash.rect.width * ratio), int(self.held_trash.rect.height * ratio)))
			window.blit(scaled_image, (x + 5, 105))
			text = pygame.font.SysFont('Arial', 12).render(str(self.held_trash.name), True, (255, 255, 255))
			window.blit(text, (x + 25 - text.get_width() / 2, 155))

	def animate(self):
		sequence = get_animation_frames(self.skin, self.current_animation)
		self.image.fill((0, 0, 0, 0))
		self.image.blit(sequence, (0, 0), (self.current_frame // self.animation_speed * self.SPRITE_SIZE[0], 0, self.SPRITE_SIZE[0], self.SPRITE_SIZE[1]))
		self.current_frame += 1
		if self.current_frame == ANIMATION_FRAMES[self.current_animation] * self.animation_speed:
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
					if self.vel_y > 0 and self.rect.bottom >= platform.rect.top :
						self.rect.bottom = platform.rect.top
					
					elif self.vel_y < 0 :
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
			self.music.jump1.play() #sound of 1st jump
			self.vel_y = -10
		elif self.can_double_jump:
			self.music.jump2.play()
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
			self.music.footstep_sound.play()
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
		if not self.is_on_ground(platforms):
			return
		if not self.throwing and self.has_trash :
			self.stop('left')
			self.stop('right')
			self.throwing = True
			self.set_animation('pre_throw', 24)
		elif self.throwing and self.has_trash:
			self.has_trash = False
			self.throwing = False
			self.set_animation('throw')
			Projectile(self.rect.x, self.rect.y, self.id, self.gauge.value, self.arrow.angle, self.mirror, self.held_trash)
		else :
			return
			

	def pick_trash(self, trash, trash_list, trash_group) :
		if not self.has_trash :
			self.has_trash = True
			self.held_trash = trash
			trash_list.remove(trash)
			trash_group.remove(trash)


		