class Character():
	def __init__(self, name, image, description, stats, special_skill=None):
		self.name = name
		self.image = image
		self.description = description
		self.stats = stats
		self.special_skill = special_skill