
#class to represent 
class Button(object): 
	def __init__(self, x, y, name):
		#state is 0 when pressed in, and 1 otherwise
		self.state = 1
		self.x = x
		self.y = y
		self.name = name

		#set to true when the button is pressed
		self.bang = False


	def draw(self,images):
		images[self.name+"-"+str(self.state)].blit(self.x,self.y)

	#checks to see if this button was clicked on
	def pressed(self, x, y, button, mouse, f):
		if self.overlap(x, y, f):
			self.state = 0

	#function is called when the mouse clicks as releases on this button
	def released(self, x, y, button, mouse, f):
		if self.overlap(x, y, f):
			self.bang = True
			if self.name=="play":
				self.name = "pause"
			elif self.name=="pause":
				self.name = "play"

		self.state = 1

	#returns if the mouse is over the button or not
	def overlap(self, x, y, f):
		if x > self.x and x < self.x + 26*f and y > self.y and y < self.y + 26*f:
			return True
		return False

