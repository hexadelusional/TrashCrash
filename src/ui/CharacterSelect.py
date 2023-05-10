from ui.MenuCharacterSelectable import MenuCharacterSelectable
import pygame

class CharacterSelect(): 
	def __init__(self, characters):
		self.characters = characters
		self.p1_selection = 0
		self.p2_selection = 1
		self.selectables = []
		for (i, character) in enumerate(self.characters):
			self.selectables.append(MenuCharacterSelectable(character.name.lower(), i, 63 + i * 100, 328))

	def draw(self, window):
		for selectable in self.selectables:
			selectable.draw(window, self.p1_selection, self.p2_selection)

	def handle_input(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				self.p1_selection = (self.p1_selection - 1) % len(self.characters)
			if event.key == pygame.K_d:
				self.p1_selection = (self.p1_selection + 1) % len(self.characters)
			if event.key == pygame.K_j:
				self.p2_selection = (self.p2_selection - 1) % len(self.characters)
			if event.key == pygame.K_l:
				self.p2_selection = (self.p2_selection + 1) % len(self.characters)
