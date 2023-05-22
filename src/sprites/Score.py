import pygame
pygame.init()
class Score():
	def __init__(self, window_size, position):
		self.score = 0
		self.y = 25
		self.position = position
		self.window_size = window_size
		self.font = pygame.font.Font('assets/grobold.ttf', 32)
		
	def increment(self, amount):
		self.score += amount
		
	def draw(self,window):
		negative = self.score < 0
		score_str = ('-' if negative else '0') + '0' * (7 - len(str(abs(self.score)))) + str(abs(self.score))
		score_text = self.font.render(score_str, True, (255, 255, 255))
		x = 25 if self.position == 'left' else self.window_size[0] - 25 - score_text.get_width()
		window.blit(score_text, (x, self.y))