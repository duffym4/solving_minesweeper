
import random as rand

class Board(object):
	"""
	Internal representation of the board,
	grid is a list of board rows, where
	'True' represents a mine 
	"""
	def __init__(self,nrows,ncols,mines):
		# Initialize grid
		self.grid = [[False]*ncols]*nrows
		self.nrows = nrows
		self.ncols = ncols
		i = 0
		while (i<mines):
			rowPlacement = rand.randint(0,nrows-1)
			colPlacement = rand.randint(0,ncols-1)
			if (not self.grid[rowPlacement][colPlacement]):
				self.grid[rowPlacement][colPlacement] = True
				i+=1

	def getCell(self, x, y):
		if self.grid[y] and self.grid[y][x]:
			return 9
		bombs = 0
		for x0 in range(-1, 2):
			for y0 in range (-1, 2):
				if (y + y0) in range (0, self.nrows) and (x + x0) in range(0, self.ncols):
					bombs+=1
		return bombs

	def printGrid(self):
		print(self.grid)
