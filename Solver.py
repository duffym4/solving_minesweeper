def findSolvableRegion(playerBoard):
	equation = []
	variables = []
	for row in range(len(playerBoard)):
		for col in range(len(playerBoard[0])):
			if (playerBoard[row][col] == -1):
				variables.append((row,col))

	points = []
	for var in variables:
		for x in range(-1,2):
			for y in range(-1,2):
				
	return equation

		
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

A = [[-1,1,0],[1,1,0],[0,0,0]]
Q = findSolvableRegion(A)
print(Q)