class VisualBoard(object):
	"""
	Display available to the player
	"""
	def __init__(self, _board):
		self.grid = []
		self.board = _board
		for y in range(0, self.nrows):
			self.grid.append([])
			for x in range(0, self.ncols):
				self.grid[y].append(Tile(x,y,-1))

	def updateTiles(self):
		for i in range(self.board.rows):
			for j in range(self.board.cols):
