import random

class Board(object):
    def __init__(self,dimension):
        Board = []
        

    def getCell(self, x, y)
    	bombs = 0
    	for x0 in range(-1, 2):
    		for y0 in range (-1, 2):
    			if abs(x0) + abs(y0) == 1:
    				if Grid[y + y0] and Grid[y + y0][x + x0]:
    					bombs+=1
    	return bombs
