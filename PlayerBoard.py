from Tile import *

class PlayerBoard(object):
	"""
	Display available to the player
	"""
	def __init__(self, _board):
		self.grid = []
		self.board = _board
		self.nrows = self.board.nrows
		self.ncols = self.board.ncols
		
		for y in range(0, self.nrows):
			self.grid.append([])
			for x in range(0, self.ncols):
				self.grid[y].append(Tile(x,y))


	def activate(self, x, y):
		self.grid[x][y].activate(self.board.getCell(x,y))

	def draw(self, x0, y0, images):
		for y in range(0, self.nrows):
			for x in range(0, self.ncols):
				self.grid[y][x].draw(x0, y0, images)
