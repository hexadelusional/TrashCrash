import pygame

BIN_DIMENSIONS = (80, 80)
IMAGES = {
	'blue': pygame.transform.scale(pygame.image.load('assets/images/bins/blue.png'), BIN_DIMENSIONS),
	'red': pygame.transform.scale(pygame.image.load('assets/images/bins/red.png'), BIN_DIMENSIONS),
	'yellow': pygame.transform.scale(pygame.image.load('assets/images/bins/yellow.png'), BIN_DIMENSIONS)
}

class Bin(pygame.sprite.Sprite):
	def __init__(self, x, y, color, scores_toward):
		super().__init__()
		self.color = color
		self.image = IMAGES[color]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.scores_toward = scores_toward # Tells which player benefits from the point scored in this bin
		self.rect.y = y
	   
	def draw(self, window):
		window.blit(self.image, self.rect, (0, 0, self.rect.width, self.rect.height))

	def collide_with_projectile(self, projectile):
		# Check whether the projectile is colliding with the bin from the top
		is_colliding_from_top = projectile.rect.bottom >= self.rect.top \
			and projectile.rect.bottom <= self.rect.top + 10 \
			and projectile.rect.centerx >= self.rect.left \
			and projectile.rect.centerx <= self.rect.right

		if not is_colliding_from_top:
			return 0
		if projectile.trash.bin == self.color:
			return 116
		else:
			return 58
				