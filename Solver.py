def checkBounds(row,col,playerBoard):
	rowCheck = (0<= row) and (len(playerBoard)>row)
	colCheck = (0<= col) and (len(playerBoard[0])>col)
	return (rowCheck and colCheck)

 def findSolvableRegion(playerBoard):
	variables = []
	columns = []
	b = []
	for row in range(len(playerBoard)):
		for col in range(len(playerBoard[0])):
			if (playerBoard[row][col] == -1):
				for x in range(-1,2):
					for y in range(-1,2):
						if (checkBounds(row+x,col+y,playerBoards)):
							if (0<playerBoard[row+x][col+y] and playerBoard[row+x][col+y]<9):
								variables.append((row,col))
	for var in variables:
		column = []
		for x in range(-1,2):
			for y in range(-1,2):
				column.append()
	if (0<playerBoard[row][col] and playerBoard[row][col]<9):
		equation = []
		if (row+x in range(len(playerBoard)) and col+y in range(len(playerBoard[0]))):
			if (not (x==0 and y==0)):
				equation.append((-1 == playerBoard[row+x][col+y])*1)
				variable = (row+x,col+y)
				else:
					equation.append(0)
					equation.append(playerBoard[row][col])
					augmentedMatrix.append(equation)
	return record,augmentedMatrix

		
def Gaussian(matrix):

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
				if(board.grid[i][j].value == -1)
					board.setMarking(i, j, 2)

#if a tile has an equal number of adjacent flags to its value,
#reveal all other adjacent tiles
def ActivateTiles(x, y, board):
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
				if(board.grid[i][j].value == -1)
					board.activate(i,j)

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


def binarySolve(matrix):
	"""
	Augmented Row Reduced matrix as input
	returns the vector answer to Ax=b
	x_i=-1 if the result is underdetermined 
	"""
	solution = [-1]*(len(matrix[0])-1)
	for row in matrix:
		upper, lower = (0,0)
		for element in row[:len(matrix[0])-1]:
			if element == 1:
				upper += 1
			elif element == -1:
				lower -= 1
		if (row[-1] == upper):
			for i in range(len(matrix[0])-1):
				if row[i] == 1:
					solution[i] = 1
				elif row[i] == -1:
					solution[i] = 0
		if (row[-1] == lower):
			for i in range(len(matrix[0])-1):
				if row[i] == 1:
					solution[i] = 0
				elif row[i] == -1:
					solution[i] = 1
	return solution
A = [[0,1,-1],[0,1,-1],[0,1,1]]
Q = findSolvableRegion(A)
print(Q[1])

