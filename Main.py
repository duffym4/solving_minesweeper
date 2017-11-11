from Board import *
from PlayerBoard import *
import pyglet
from Timer import *

board = Board(10, 10, 10)
playerBoard = PlayerBoard(board)

for y in range(0, playerBoard.nrows):
	for x in range(0, playerBoard.ncols):
		playerBoard.activate(x, y)

window = pyglet.window.Window()

board.printGrid()


print(board.getCell(5, 5))

timer = Timer()


images = {}
images['mine'] = pyglet.image.load('images/sprites.png').get_region(x=0, y=16*3+1, width=16, height=16)
images['flag'] = pyglet.image.load('images/sprites.png').get_region(x=4*16, y=16*3+1, width=16, height=16)
images['blank'] = pyglet.image.load('images/sprites.png').get_region(x=5*16, y=16*3+1, width=16, height=16)
for i in range(0, 9):
	images['number-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=16*i, y=16*4+1, width=16, height=16)
for i in range(0, 10):
	images['timer-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=13*i, y=26, width=13, height=23)

@window.event
def on_draw():
	window.clear()
	playerBoard.draw(100, 100, images)
	for i in range(0, 9):
		images['number-'+str(i)].blit(16*i, 0)
	for i in range(0, 10):
		images['timer-'+str(i)].blit(13*i, 16)

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		print ('The left mouse button was pressed.')

pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run() 
