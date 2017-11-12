from Tile import *

class PlayerBoard(object):
	"""
	Display available to the player
	"""
	def __init__(self, board_, x0_, y0_, timer_, smile_, flagCounter_):
		self.grid = []
		self.board = board_
		self.nrows = self.board.nrows
		self.ncols = self.board.ncols
		self.mines=self.board.mines
		self.x0 = x0_
		self.y0 = y0_
		self.timer = timer_
		self.smile = smile_
		self.flagCounter = flagCounter_
		self.createBoard()

	''' reset all values for starting the game, and create a blank board '''
	def createBoard(self):
		self.boardCounter=0
		self.gameOver = False
		self.gameWon = False
		self.grid = []
		for y in range(0, self.nrows):
			self.grid.append([])
			for x in range(0, self.ncols):
				self.grid[y].append(Tile(x, y, self.flagCounter))
		
	''' called when a tile is overturned, either by clicking, a hint, or by the recursive unfolding of tiles which touch no bombs '''
	def activate(self, x, y, userClicked=False):

		''' ensure the tile is one which may be pressed '''
		if self.grid[y][x].value >= 0:
			return

		''' activate the individual tile object '''
		self.grid[y][x].activate(self.board.getCell(x,y))

		''' increase the board counter (used to check whether the board is complete) '''
		self.boardCounter+=1

		''' if this function was called directly, not recursively, check win/loss conditions '''
		if userClicked:
			self.checkwin()
			if self.grid[y][x].value==9:
				self.loseGame(x, y)

		''' if this reveals a tile touching no bombs, recursively unfold the surrounding tiles '''
		if self.grid[y][x].value == 0:
			for x0 in range(-1, 2):
				for y0 in range (-1, 2):
					if (y + y0) in range (0, self.nrows) and (x + x0) in range(0, self.ncols):
						if self.grid[y+y0][x+x0].value == -1:
							self.activate(x+x0, y+y0)

	''' check win conditions '''
	def checkwin(self):
		if self.boardCounter==self.nrows*self.ncols-self.mines:
			self.smile.win()
			self.gameWon = True
			self.timer.stop()
			
	''' draw each tile object '''
	def draw(self, images, scale):
		for y in range(0, self.nrows):
			for x in range(0, self.ncols):
				self.grid[y][x].draw(self.x0, self.y0, images, scale)

	''' set marking to 1=blank, 2=flag, 3=unkown '''
	def setMarking(self, x, y, mark):
		if self.grid[y][x].value < 0:
			self.grid[y][x].value = -2
			self.grid[y][x].updateImages()

	''' attempt to reveal a bomb (called after the player loses, used to show remaining bombs) '''
	def revealBomb(self, x, y, flag):
		self.grid[y][x].value = 9
		self.grid[y][x].updateImages()
		if flag:
			self.grid[y][x].imageKey = "mine-1"

	''' called when mouse is released '''
	def mouse(self, x, y, button, mouse, f):

		if self.gameOver or self.gameWon:
			return

		''' get the tile that the mouse is hovering '''
		gridX = int((x-self.x0)/(16*f))
		gridY = int((y-self.y0)/(16*f))

		if not (gridX in range(0, self.ncols) and gridY in range(0, self.nrows)):
			return

		if button == mouse.LEFT:
			self.activate(gridX, gridY, userClicked=True)

		elif button == mouse.RIGHT and self.grid[gridY][gridX].value < 0:
			self.grid[gridY][gridX].rotateMarking()
		
	''' react to a loss by revealing bombs and setting states / stopping timers '''
	def loseGame(self, x, y):
		self.gameOver = True
		self.smile.state = 3
		self.grid[y][x].imageKey = "mine-2"
		self.timer.stop()
		for i in range(0,self.nrows):
			for j in range(0,self.ncols):
				if self.board.getCell(j,i)==9 and self.grid[i][j].value < 0:
					self.revealBomb(j, i, self.grid[i][j].value < -1)