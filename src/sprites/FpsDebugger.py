import pygame

class FpsDebugger():
	def __init__(self):
		self.font = pygame.font.SysFont('Arial', 20)
		self.track = []
		self.text = self.font.render('0', True, (0,0,0))

	def update(self, clock):
		fps = clock.get_fps()
		self.track.append(fps)
		if len(self.track) > 100:
			self.track.pop(0)
		self.text = self.font.render(f'{fps:.2f}', True, (0,0,0))
		self.text_rect = self.text.get_rect()

	def draw(self, window):
		window.blit(self.text, self.text_rect)
		# Make a small fps graph
		graph_height = 75
		pygame.draw.rect(window, (255, 255, 255), (self.text_rect.x, self.text_rect.y + self.text_rect.height + 10, 100, graph_height), 1)
		for i, fps in enumerate(self.track):
			pygame.draw.line(window, 
		    (255, 255, 255), 
			(self.text_rect.x + i, self.text_rect.y + self.text_rect.height + 10 + graph_height), 
			(self.text_rect.x + i, self.text_rect.y + self.text_rect.height + 10 + graph_height - (fps / 60 * graph_height)), 
		1)