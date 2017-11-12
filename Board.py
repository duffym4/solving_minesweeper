import random as rand

class Board(object):
	"""
	Internal representation of the board,
	grid is a list of board rows, where
	'True' represents a mine 
	"""

	def __init__(self,_ncols,_nrows,_mines):
		# Board data
		self.nrows = _nrows
		self.ncols = _ncols
		self.mines = _mines
		self.createBoard()

	def createBoard(self):
		# Initialize grid
		self.grid = []
		for y in range(0, self.nrows):
			self.grid.append([])
			for x in range(0, self.ncols):
				self.grid[y].append(False)

		# Place the mines
		for i in range(self.mines):
			rowPlacement = rand.randint(0,self.nrows-1)
			colPlacement = rand.randint(0,self.ncols-1)
			placed = False
			while (not placed):
				if (not self.grid[rowPlacement][colPlacement]):
					self.grid[rowPlacement][colPlacement] = True
					placed = True
				else:
					# if there is already a mine, move it
					if (colPlacement >= self.ncols-1):
						rowPlacement += 1
						if (rowPlacement > self.nrows-1):
							rowPlacement = 0
						colPlacement = -1
					colPlacement += 1

	def getCell(self, x, y):
		if self.grid[y][x]:
			return 9
		bombs = 0
		for x0 in range(-1, 2):
			for y0 in range (-1, 2):
				if (y + y0) in range (0, self.nrows) and (x + x0) in range(0, self.ncols):
					if self.grid[y+y0][x+x0]:
						bombs+=1
		return bombs

	def printGrid(self):
		for y in range(0, self.nrows):
			for x in range(0, self.ncols):
				if self.grid[y][x]:
					print(1, end="")
				else:
					print(0, end="")
			print()