import pygame
from random import randint

class Sound():
    def __init__(self): 
        self.music= pygame.mixer_music.load(f"assets/sounds/game_music/0.mp3")
        self.music_volume=pygame.mixer.music.set_volume(0.25)
        self.music_play=pygame.mixer.music.play(loops=-1)
        self.footstep_sound=pygame.mixer.Sound("assets/sounds/footstep.wav")
        #self.footstep_sound_play=pygame.mixer.music.play(loops=-1)
        self.jump1=pygame.mixer.Sound("assets/sounds/jump_01.wav")
        self.jump2=pygame.mixer.Sound("assets/sounds/jump_02.wav")
        self.sound_volume()
        
    def sound_volume(self):
        self.footstep_sound.set_volume(0.15)
        self.jump1.set_volume(0.05)
        self.jump2.set_volume(0.05)