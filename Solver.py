<<<<<<< HEAD



def CountValue(x, y, board, value):
	rows = board.nrows
	cols = board.ncols

	count = 0
	for i in range(x-1, x+1):
		if(i < 0 or i >= rows):
			continue
		for j in range(y-1, y+1):
			if(j < 0 or j > cols):
				continue
			if(board.grid[i][j].value == value):
				count += 1

def MarkFlags(x, y, board):
	blanks = CountValue(x, y, board, -1)
	if(board.grid[x][y].value == blanks):
		for i in range(x-1, x+1):
			if(i < 0 or i >= rows):
				continue
			for j in range(y-1, y+1):
				if(j < 0 or j > cols):
					continue
				if(board.grid[i][j].value == -1)
					board.setMarking(i, j, 2)

def ActivateTiles(x, y, board):
	flags = CountValue(x, y, board, 10)
	if(board.grid[x][y].value == flags):
		for i in range(x-1, x+1):
			if(i < 0 or i >= rows):
				continue
			for j in range(y-1, y+1):
				if(j < 0 or j > cols):
					continue
				if(board.grid[i][j].value == -1)
					board.activate(i,j)


def binarySolve(matrix):
	for row in matrix:
		solution = []*5
		upper, lower = (0,0)
		for element in row[:-1]:
			if element == 1:
				upper += 1
			else
				lower -= 1
		if 
>>>>>>> 4ae552e3c1ffb9b84acab730e06829898cec0ce3
