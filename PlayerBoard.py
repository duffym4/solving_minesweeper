from Tile import *

class PlayerBoard(object):
	"""
	Display available to the player
	"""
	def __init__(self, board_, x0_, y0_, timer_, smile_):
		self.grid = []
		self.board = board_
		self.nrows = self.board.nrows
		self.ncols = self.board.ncols
		self.mines=self.board.mines
		self.x0 = x0_
		self.y0 = y0_
		self.timer = timer_
		self.smile = smile_
		
		self.createBoard()

	def createBoard(self):
		self.boardCounter=0
		self.gameOver = False
		self.grid = []
		for y in range(0, self.nrows):
			self.grid.append([])
			for x in range(0, self.ncols):
				self.grid[y].append(Tile(x,y))
		

	def activate(self, x, y):
		self.grid[y][x].activate(self.board.getCell(x,y))

		self.boardCounter+=1

		if self.grid[y][x].value == 0:
			for x0 in range(-1, 2):
				for y0 in range (-1, 2):
					if (y + y0) in range (0, self.nrows) and (x + x0) in range(0, self.ncols):
						if self.grid[y+y0][x+x0].value == -1:
							self.activate(x+x0, y+y0)
	def checkwin(self):
		if self.boardCounter==self.nrows*self.ncols-self.mines:
			self.smile.win()
			
	def draw(self, images, scale):
		for y in range(0, self.nrows):
			for x in range(0, self.ncols):
				self.grid[y][x].draw(self.x0, self.y0, images, scale)

	def mouse(self, x, y, button, mouse, f):

		if self.gameOver:
			return

		gridX = int((x-self.x0)/(16*f))
		gridY = int((y-self.y0)/(16*f))

		if not (gridX in range(0, self.ncols) and gridY in range(0, self.nrows)):
			return

		if button == mouse.LEFT:
			self.activate(gridX, gridY)
			self.checkwin()
			if self.grid[gridY][gridX].value==9:
				self.gameOver = True
				self.smile.state = 3
				self.grid[gridY][gridX].imageKey = "red_mine"
				self.timer.stop()
				for i in range(0,self.nrows):
					for j in range(0,self.ncols):
						if self.board.getCell(j,i)==9 and self.grid[i][j].value==-1:
							self.activate(j,i)
									

		elif button == mouse.RIGHT and self.grid[gridY][gridX].value < 0:
			self.grid[gridY][gridX].rotateMarking()
		
		