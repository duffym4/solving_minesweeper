import random as rand

class Board(object):
	"""
	Internal representation of the board,
	grid is a list of board rows, where
	'True' represents a mine 
	"""

	def __init__(self,_ncols,_nrows,_mines):
		self.nrows = _nrows
		self.ncols = _ncols
		self.mines = _mines
		self.createBoard()

	#create a grid to represent all of the tiles
	#randomly place mines throughout the grid
	def createBoard(self):
		#Initialize grid as a 2d list of lists
		self.grid = []
		for y in range(0, self.nrows):
			self.grid.append([])
			#initialize all values as false
			for x in range(0, self.ncols):
				self.grid[y].append(False)

		#randomly place self.mines number of mines throughout the grid
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

	#return the number of adjacent mines to this tile or 9 if it is a mine
	def getCell(self, x, y):
		if self.grid[y][x]:
			return 9
		mines = 0
		for x0 in range(-1, 2):
			for y0 in range (-1, 2):
				if (y + y0) in range (0, self.nrows) and (x + x0) in range(0, self.ncols):
					if self.grid[y+y0][x+x0]:
						mines+=1
		return mines
