
class Smile(object): 

	def __init__(self, x, y):
		self.state = 1
		self.x = x
		self.y = y
		self.reset = False

	''' draws the appropriate smile image '''
	def draw(self,images):
		images['smile-'+str(self.state)].blit(self.x,self.y)

	''' show the button pressed down when clicked '''
	def mouse(self, x, y, button, mouse, f):
		if x > self.x and x < self.x + 26*f and y > self.y and y < self.y + 26*f:
			self.state = 0

	''' mouse pressed '''
	def pressed(self, x, y, button, mouse, f):
		if self.overlap(x, y, f):
			self.state = 0
		elif self.state == 1:
			self.state = 2

	''' mouse released '''
	def released(self, x, y, button, mouse, f):
		if self.state == 0 and self.overlap(x, y, f):
			self.reset = True
		if self.state == 2 or self.state == 0:
			self.state = 1

	''' win/lose functions for readability when setting smile state '''
	def win(self):
		self.state=4

	def lose(self):
		self.state=3

	''' checks for mouse over smile '''
	def overlap(self, x, y, f):
		if x > self.x and x < self.x + 26*f and y > self.y and y < self.y + 26*f:
			return True
		return False

