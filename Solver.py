


def CountValue(x, y, board, value):
	rows = board.nrows
	cols = board.ncols

	count = 0
	for i in range(x-1, x+1):
		if(i < 0 or i >= rows):
			continue
		for j in range(y-1, y+1):
			if(j < 0 or j > cols):
				if(board.grid[i][j].value == value):
					count += 1

def MarkFlags(x, y, board):
	blanks = CountValue(x, y, board, -1)
	if(board.grid[x][y].value == blanks):

def ActivateTiles(x, y, board):
	flags = CountValue(x, y, board, 10)
	if(board.grid[x][y].value == flags):