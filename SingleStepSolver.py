
#count how many of an unmarked tiles and flags are adjacent tiles to the 
#input x and y value
def getBombOptions(x0, y0, board):
	rows = board.nrows
	cols = board.ncols
	value = -1

	options = []
	flagCount = 0

	for x in range(x0-1, x0+2):
		for y in range(y0-1, y0+2):
			#do not count self
			if x != x0 or y != y0:
				#make sure we are in range of the board
				if x in range(0, cols) and y in range(0, rows):
					if board.grid[y][x].value == value:
						options.append([x, y])
					elif board.grid[y][x].value == -2:
						flagCount += 1

	return options, flagCount


#mark tiles with flags next to x, y input if trivial solution possible
#also build the ranges list
def MarkFlags(x, y, board, ranges):
	options, count = getBombOptions(x, y, board)
	if len(options) > 0:
		ranges.append([[x, y], options, count])
		#mark a tile from options list if the tile value = num unmarked tiles + num flags
		if(board.grid[y][x].value == count+len(options)):
			board.setMarking(options[0][0], options[0][1], 2)
			return True
	return False


#reveal tiles next to x, y input if trivial solution possible
def ActivateTiles(x, y, board):
	options, count = getBombOptions(x, y, board)
	#reveal an adjacent unmarked tile if the tile value equals the number of adjacent flags
	if(board.grid[y][x].value == count and len(options) > 0):
		board.activate(options[0][0], options[0][1], automated=True)
		return True
	return False


#return true if the two positions are adjacent
def isTouching(x1, y1, x2, y2):
	return abs(x1-x2)<2 and abs(y1-y2)<2

#returns the number of adjacent unmarked flags for a tile
def minesLeft(x, y, playerBoard, flags):
	return playerBoard.grid[y][x].value - flags

#places a single flag or reveals a single tile
def SingleStepSolver(playerBoard):

	rows = len(playerBoard.grid)
	cols = len(playerBoard.grid[0])

	#ranges stores a list of ranges that mines could be placed in
	#ranges[i][0] returns a tuple of ranges[i] position
	#ranges[i][1] returns all possible positions for mines adjacent to ranges[i][0]
	#ranges[i][2] returns the number of flags adjacent to ranges[i][0]
	ranges = []

	#look for trivial solutions
	for i in range(0, rows):
		for j in range(0, cols):
			#skip tile if it is not yet revealed
			if (playerBoard.grid[i][j].value in range(-3, 1)):
				continue
			if(MarkFlags(j, i, playerBoard, ranges)):
				return
			if(ActivateTiles(j, i, playerBoard)):
				return

	#use ranges that mines can be in to calculate solutions
	for i in range(0, len(ranges)):
		iPosition = ranges[i][0]
		iOptions = ranges[i][1]
		iFlags = ranges[i][2]
		#compare the ranges[i] to all elements in ranges
		for j in range(len(ranges)):
			#skip self
			if(i == j):
				continue

			jPosition = ranges[j][0]
			jOptions = ranges[j][1]
			jFlags = ranges[j][2]

			#count the number of ranges that ranges[i] and ranges[j] share all values of
			shared = 0
			notSharedRange = iOptions.copy()
			for space in jOptions:
				if isTouching(space[0], space[1], iPosition[0], iPosition[1]):
					shared+=1
					notSharedRange.remove(space)

			#the minimum number of mines that ranges[i] and ranges[j] share = NumSharedAdjacentPositions - NumPossibleJMinePositions + NumMinesUnrevieled 
			mineCount = shared - len(jOptions) + minesLeft(jPosition[0], jPosition[1], playerBoard, jFlags)

			#if we know the ranges where all adjacent remaining mines are, reveal an adjacent tile
			if(mineCount == minesLeft(iPosition[0], iPosition[1], playerBoard, iFlags)):
				for space in notSharedRange:
					playerBoard.activate(space[0], space[1], automated=True)
					return

			#if we know the minimum number of mines is in an overlap and that 
			#the number of tiles out of the overlap is equal to the number of mines out of the overlap flag one of the tiles out of the overlap
			if min(min(minesLeft(jPosition[0], jPosition[1], playerBoard, jFlags), minesLeft(iPosition[0], iPosition[1], playerBoard, iFlags)), shared) == mineCount:
				if(mineCount == minesLeft(iPosition[0], iPosition[1], playerBoard, iFlags) - len(notSharedRange) and mineCount>0):
					for space in notSharedRange:
						playerBoard.setMarking(space[0], space[1], 2)
						return