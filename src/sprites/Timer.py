import time

import pygame

fill_font = pygame.font.Font('assets/digital.ttf', 36)

class Timer:
	def __init__(self, seconds):
		self.seconds = seconds
		self.last_time = None

	def update(self):
		self.seconds-=1
	
	def draw(self, window):
		rounded = int(self.seconds)
		minutes = rounded // 60
		seconds = (rounded - minutes * 60) % 60
		seconds_str = f'0{seconds}' if seconds < 10 else f'{seconds}'
		text = fill_font.render(f'{minutes}:{seconds_str}', True, (0,0,0))
		width = text.get_width()
		window.blit(text, (640 - width // 2, 30))