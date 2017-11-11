import random as rand
class Board(object):
	"""
	Internal representation of the board,
	grid is a list of board rows, where
	'True' represents a mine 
	"""
    def __init__(self,nrows,ncols,mines):
    	# Initialize grid
        grid = [[False]*ncols]*nrows
        i = 0
        while (i<mines):
        	rowPlacement = rand.randint(0,rows-1)
        	colPlacement = rand.randint(0,cols-1)
        	if (!grid[rowPlacement][colPlacement]):
        		grid[rowPlacement][colPlacement] = True
        		i+=1