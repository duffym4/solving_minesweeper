
class PlayerBoard(object):
	"""
	Display available to the player
	"""
	def __init__(self, _board):
		self.grid = []
		self.board = _board
		
		for i in range(0, self.nrows):
			self.grid.append([])
			for j in range(0, self.ncols):
				self.grid[i][j] = Tile(x,y)
			end
		end


	def activate(x,y):
		self.grid[x][y].activate(self.board.getcell(x,y))

