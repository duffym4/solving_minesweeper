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