import pygame
pygame.mixer.init()
class Mixer():
	def __init__(self):
		self.music = None
		self.sounds = {}

	def import_sound(self, name, path):
		self.sounds[name] = pygame.mixer.Sound(path)
	
	def play_sound(self, name):
		self.sounds[name].play()
	
	def play_music(self, name, path, fade=0):
		self.music = name
		pygame.mixer.music.load(path)
		pygame.mixer.music.play(-1, fade_ms=fade)
	
	def stop_music(self):
		pygame.mixer.music.stop()
		self.music = None

	def set_volume(self, volume):
		pygame.mixer.music.set_volume(volume)


main_mixer = Mixer()
main_mixer.import_sound('jump1', 'assets/sfx/jump_01.wav')
main_mixer.sounds['jump1'].set_volume(0.5)
main_mixer.import_sound('jump2', 'assets/sfx/jump_02.wav')