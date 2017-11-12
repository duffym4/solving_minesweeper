
class Smile(object): 
	def __init__(self):
		self.state = 1
	def draw(self,images,scale,x,y,smileNum):
		images['smile-'+str(self.state)].blit(x,y)
	def pressed(self):
		if self.state == 1:
			self.state = 2
	def released(self):
		if self.state == 2:
			self.state = 1
	def win(self):
		self.state=4
	def lose(self):
		self.state=3