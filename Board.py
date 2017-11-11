import random as rand

class Board(object):
	"""
	Internal representation of the board,
	grid is a list of board rows, where
	'True' represents a mine 
	"""

	def __init__(self,_nrows,_ncols,_mines):
		# Initialize grid
		self.grid = [[False]*_ncols]*_nrows
		# Board data
		self.nrows = _nrows
		self.ncols = _ncols
		self.mines = _mines

		# Place the mines
		for i in range(_mines):
			rowPlacement = rand.randint(0,_nrows-1)
			colPlacement = rand.randint(0,_ncols-1)
			placed = False
			while (not placed):
				if (not self.grid[rowPlacement][colPlacement]):
					self.grid[rowPlacement][colPlacement] = True
					placed = True
				else:
					# if there is already a mine, move it
					if (colPlacement == _ncols-1):
						rowPlacement += 1
						colPlacement = -1
					colPlacement+=1

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
		for x in range(0, self.ncols):
			for y in range(0, self.nrows):
				if self.grid[y][x]:
					print(1, end="")
				else:
					print(0, end="")
			print()
