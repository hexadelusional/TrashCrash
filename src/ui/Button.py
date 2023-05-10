import pygame

class Button(): 
	def __init__(self, x, y, text, action=None, width=None, font_size=32):
		self.x = x
		self.y = y
		self.text = text
		self.color = pygame.Color(52, 195, 235)
		self.text_color = pygame.Color(255, 255, 255)
		self.action = action
		self.font = pygame.font.Font('assets/grobold.ttf', font_size)
		self.text_render = self.font.render(self.text, True, self.text_color)
		self.text_rect = self.text_render.get_rect()
		if width is not None:
			self.text_rect.center = (self.x + (width / 2), self.y + 30)
		else:
			self.text_rect.topleft = (self.x + 10, self.y + 10)
		self.rect = pygame.Rect(self.x, self.y, width or self.text_rect.width + 20, self.text_rect.height + 20)

	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect, border_radius=10)
		window.blit(self.text_render, self.text_rect)

	def update(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				if self.action is not None:
					self.action()
		if event.type == pygame.MOUSEMOTION:
			if self.rect.collidepoint(event.pos):
				self.color = pygame.Color(255, 255, 255)
				self.text_color = pygame.Color(52, 195, 235)
				self.text_render = self.font.render(self.text, True, self.text_color)
			else:
				self.color = pygame.Color(52, 195, 235)
				self.text_color = pygame.Color(255, 255, 255)
				self.text_render = self.font.render(self.text, True, self.text_color)