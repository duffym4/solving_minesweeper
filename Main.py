from Board import *
from Timer import *
from Tile import *

board = Board(10, 10, 10)

board.printGrid()


print(board.getCell(5, 5))

timer = Timer()

tile = Tile(100, 100)
tile2 = Tile(150, 100)

images = {}
images['bomb'] = pyglet.image.load('images/sprites.png').get_region(x=0, y=16*3, width=16, height=16)
images['flag'] = pyglet.image.load('images/sprites.png').get_region(x=4*16, y=16*3, width=16, height=16)
images['blank'] = pyglet.image.load('images/sprites.png').get_region(x=5*16, y=16*3, width=16, height=16)
for i in range(0, 9):
	images['number-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=16*i, y=16*4+1, width=16, height=16)

@window.event
def on_draw():
	window.clear()
	timer.label.draw()
	tile.draw(images)
	for i in range(0, 9):
		images['number-'+str(i)].blit(16*i, 0)


pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run() 