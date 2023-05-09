class Scene(): 
	def __init__(self, on_enter: callable, loop: callable):
		self.on_enter = lambda *args, **kwargs: on_enter(self, *args, **kwargs)
		self.loop = lambda *args, **kwargs: loop(self, *args, **kwargs)