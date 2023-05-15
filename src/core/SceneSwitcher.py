import pygame

from sprites.FpsDebugger import FpsDebugger

class SceneSwitcher():
	def __init__(self, window):
		self.window = window
		self.scenes = dict()
		self.current_scene = None
		self.paused = False
		self.clock = pygame.time.Clock()
		self.fps = FpsDebugger()
			
	def add_scene(self, scene_name, scene):
		scene.switcher = self
		self.scenes[scene_name] = scene
	
	def switch_to(self, scene_name, *args, **kwargs):
		self.current_scene = self.scenes[scene_name]
		self.current_scene.on_enter(*args, **kwargs)

	def loop(self, *args, **kwargs):
		if self.current_scene == None:
			return
		if self.paused:
			return
		self.current_scene.loop(self.window, *args, **kwargs)
		#self.fps.update(self.clock)
		#self.fps.draw(self.window)
		pygame.display.flip()
		self.clock.tick(60)