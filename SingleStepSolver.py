#count how many of an input value are in adjacent tiles to the 
#input x and y value
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
			#do not count yourself
			if(i == x and j ==y):
				continue
			if(board.grid[i][j].value == value):
				count += 1
#if a tile has an equal number of adjacent unmarked tiles to its 
#value flag all adjacent tiles
def MarkFlags(x, y, board):
	change = False

	blanks = CountValue(x, y, board, -1)
	if(board.grid[x][y].value == blanks):
		for i in range(x-1, x+1):
			if(i < 0 or i >= rows):
				continue
			for j in range(y-1, y+1):
				if(j < 0 or j > cols):
					continue
				if(i == x and j ==y):
					continue
				if(board.grid[i][j].value == -1):
					board.setMarking(i, j, 2)
					change = True
	return change

#if a tile has an equal number of adjacent flags to its value,
#reveal all other adjacent tiles
def ActivateTiles(x, y, board):
	change = False

	flags = CountValue(x, y, board, 10)
	if(board.grid[x][y].value == flags):
		for i in range(x-1, x+1):
			if(i < 0 or i >= rows):
				continue
			for j in range(y-1, y+1):
				if(j < 0 or j > cols):
					continue
				if(i == x and j ==y):
					continue
				if(board.grid[i][j].value == -1):
					board.activate(i,j)
					change = True
	return change


#reduces a matrix to upper triangular form
def UpperTriangular(matrix):

  rows = len(matrix)
  cols = len(matrix[0])

  for i in range(0,min(rows, cols)):

    #calculate iMax
    iMax = i
    max_val = matrix[i][i]
    for j in range(i+1, rows):
      if(abs(matrix[j][i]) > max_val):
        max_val = abs(matrix[j][i])
        iMax = j

    #swap rows
    for j in range(i, rows+1):
      tmp = matrix[iMax][j]
      matrix[iMax][j] = matrix[i][j]
      matrix[i][j] = tmp

    # Make all rows below this one 0 in current column
    for j in range(i+1, rows):
      c = -matrix[j][i]/matrix[i][i]
      for k in range(i, rows+1):
          if i == k:
              matrix[j][k] = 0
          else:
              matrix[j][k] += c * matrix[i][k]

  return matrix




# def binarySolve(matrix):
# 	for row in matrix:
# 		solution = []*5
# 		upper, lower = (0,0)
# 		for element in row[:-1]:
# 			if element == 1:
# 				upper += 1
# 			else
# 				lower -= 1
# 		if 

def SingleStepSolver(PlayerBoard):

	rows = len(PlayerBoard.grid)
	cols = len(PlayerBoard.grid[0])

	print("help")

	for i in range(0,rows):
		for j in range(0,rows):

			if (PlayerBoard.grid[i][j].value == -1):
				continue

			if(MarkFlags(i,j,PlayerBoard)):
				return
			if(ActivateTiles(i,j,PlayerBoard)):
				return