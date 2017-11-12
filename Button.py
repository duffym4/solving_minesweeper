
class Button(object): 
	def __init__(self, x, y, name):
		self.state = 1
		self.x = x
		self.y = y
		self.name = name
		self.bang = False

	def draw(self,images):
		images[self.name+"-"+str(self.state)].blit(self.x,self.y)

	def pressed(self, x, y, button, mouse, f):
		if self.overlap(x, y, f):
			self.state = 0

	def released(self, x, y, button, mouse, f):
		if self.overlap(x, y, f):
			self.bang = True
			if self.name=="play":
				self.name = "pause"
			elif self.name=="pause":
				self.name = "play"

		self.state = 1

	def overlap(self, x, y, f):
		if x > self.x and x < self.x + 26*f and y > self.y and y < self.y + 26*f:
			return True
		return False

