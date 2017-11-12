#count how many of an input value are in adjacent tiles to the 
#input x and y value
def getBombOptions(x0, y0, board, value):
	rows = board.nrows
	cols = board.ncols

	options = []
	flagCount = 0

	for x in range(x0-1, x0+2):
		for y in range(y0-1, y0+2):
			if x != x0 or y != y0:
				if x in range(0, cols) and y in range(0, rows):
					if board.grid[y][x].value == value:
						options.append([x, y])
					elif board.grid[y][x].value == -2:
						flagCount += 1

	return options, flagCount
#if a tile has an equal number of adjacent unmarked tiles to its 
#value flag all adjacent tiles
def MarkFlags(x, y, board):
	options, count = getBombOptions(x, y, board, -1)
	print(options)
	print(count)
	if(board.grid[y][x].value == count+len(options) and len(options) > 0):
		print("Marked!")
		board.setMarking(options[0][0], options[0][1], 2)
		return True
	return False

def isTouching(x1, y1, x2, y2):
	return abs(x1-x2)<2 and abs(y1-y2)<2
	
#if a tile has an equal number of adjacent flags to its value,
#reveal all other adjacent tiles
def ActivateTiles(x, y, board):

	options, count = getBombOptions(x, y, board, -1)
	if(board.grid[y][x].value == count and len(options) > 0):
		board.activate(options[0][0], options[0][1], automated=True)
		return True
	return False

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

def SingleStepSolver(playerBoard):

	rows = len(playerBoard.grid)
	cols = len(playerBoard.grid[0])

	print("help")

	for y in range(0, rows):
		for x in range(0, cols):

			print(playerBoard.grid[y][x].value)
			if (playerBoard.grid[y][x].value in range(-1, 1)):
				continue

			if(MarkFlags(x, y, playerBoard)):
				return
			if(ActivateTiles(x, y, playerBoard)):
				return