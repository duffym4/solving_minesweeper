from Tile import *

class PlayerBoard(object):
	"""
	Display available to the player
	"""
	def __init__(self, board_, x0_, y0_, timer):
		self.grid = []
		self.board = board_
		self.nrows = self.board.nrows
		self.ncols = self.board.ncols
		self.x0 = x0_
		self.y0 = y0_
		self.timer=timer
		for y in range(0, self.nrows):
			self.grid.append([])
			for x in range(0, self.ncols):
				self.grid[y].append(Tile(x,y))

	def activate(self, x, y):
		self.grid[y][x].activate(self.board.getCell(x,y))
		
				
	def draw(self, images):
		for y in range(0, self.nrows):
			for x in range(0, self.ncols):
				self.grid[y][x].draw(self.x0, self.y0, images)

	def mouse(self, x, y, button, mouse):

		gridX = int((x-self.x0)/16)
		gridY = int((y-self.y0)/16)

		if not (gridX in range(0, self.ncols) and gridY in range(0, self.nrows)):
			return

		if button == mouse.LEFT:
			self.activate(gridX, gridY)
			if self.grid[gridY][gridX].value==9:
				self.timer.stop()
				for i in range(0,self.nrows):
					for j in range(0,self.ncols):
						if self.board.getCell(i,j)==9 and self.grid[i][j].value==-1:
							self.activate(i,j)
									
			
		elif button == mouse.RIGHT and self.grid[gridY][gridX].value == -1:
			 if self.grid[gridY][gridX].imageKey == "flag":
			 	self.grid[gridY][gridX].imageKey = "unknown"

			 elif self.grid[gridY][gridX].imageKey == "unknown":
			 	self.grid[gridY][gridX].imageKey = "blank"
			 else:
			 	self.grid[gridY][gridX].imageKey = "flag"
