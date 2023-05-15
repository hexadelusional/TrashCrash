import pygame
from random import randint

class Sound():
    def __init__(self):
        pygame.mixer.music.load(f'assets/music/ingame.mp3')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(loops=-1)
        self.footstep_sound = pygame.mixer.Sound('assets/sfx/footstep.wav')
        self.jump1 = pygame.mixer.Sound('assets/sfx/jump_01.wav')
        self.jump2 = pygame.mixer.Sound('assets/sfx/jump_02.wav')
        self.sound_volume()
        
    def sound_volume(self):
        self.footstep_sound.set_volume(0.15)
        self.jump1.set_volume(0.05)
        self.jump2.set_volume(0.05)