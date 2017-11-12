
class Smile(object): 
	def __init__(self):
		self.state = 1
	def draw(self,images,scale,x,y,smileNum):
		images['smile-'+str(self.state)].blit(x,y)
	def pressed(self):
		self.state = 2
	def released(self):
		self.state = 1
