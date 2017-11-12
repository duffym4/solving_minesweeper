import pyglet
from Board import *
from PlayerBoard import *
from Timer import *
from Smile import *

''' Board Initialization '''

board = Board(30, 16, 10)

''' Window and Scaling '''
spriteSheet = pyglet.image.load('images/sprites.png')
f = int(spriteSheet.width/144)
s = f*16
window = pyglet.window.Window(caption="Hackathon Minesweeper", width=s*(2+board.ncols), height=s*(4+board.nrows))

''' Initializing Classes '''
smile = Smile((window.width-26*f)/2, window.height - 3*s + 13*f)
timer = Timer()
playerBoard = PlayerBoard(board, s, s, timer, smile)

''' Image Initialization '''
images = {}
images['mine'] = pyglet.image.load('images/sprites.png').get_region(x=0, y=s*3+f, width=s, height=s)
images['red_mine'] = pyglet.image.load('images/sprites.png').get_region(x=2*s, y=s*3+f, width=s, height=s)
images['flag'] = pyglet.image.load('images/sprites.png').get_region(x=4*s, y=s*3+f, width=s, height=s)
images['unknown'] = pyglet.image.load('images/sprites.png').get_region(x=3*s, y=s*3+f, width=s, height=s)
images['blank'] = pyglet.image.load('images/sprites.png').get_region(x=5*s, y=s*3+f, width=s, height=s)

for i in range(0, 9):
	images['number-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=s*i, y=s*4+1, width=s, height=s)
for i in range(0, 10):
	images['timer-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=13*i*f, y=26*f, width=13*f, height=23*f)
for i in range(0,5):
	images['smile-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=26*f*i,y=0,width=26*f,height=26*f)

''' Events '''
@window.event
def on_draw():
	window.clear()
	playerBoard.draw(images,f)
	timer.draw(images, f, (3/4)*(window.width-26*f), window.height - 3*s + 13*f)
	smile.draw(images)

@window.event
def on_mouse_release(x, y, button, modifiers):
	playerBoard.mouse(x, y, button, pyglet.window.mouse, f)
	smile.released(x, y, button, pyglet.window.mouse, f)
	if smile.reset:
		resetGame()

@window.event
def on_mouse_press(x, y, button, modifiers):
	smile.pressed(x, y, button, pyglet.window.mouse, f)

''' Reset Game '''
def resetGame():
	smile.reset = False
	board.createBoard()
	playerBoard.createBoard()
	timer.time = 0
	timer.running = True
	
''' Startup '''
pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run() 