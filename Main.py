import pyglet
from Board import *
from PlayerBoard import *
from Timer import *
from Smile import *
from SingleStepSolver import *

''' Board Initialization '''
board = Board(30, 16, 99)

''' Window and Scaling '''
spriteSheet = pyglet.image.load('images/sprites.png')
f = int(spriteSheet.width/144) # The factor by which sprites are scaled up
s = f*16					   # The size of a tile, given the scaling factor
window = pyglet.window.Window(caption="Hackathon Minesweeper", width=s*(2+board.ncols), height=s*(4+board.nrows))

''' Initializing Classes '''
smile = Smile((window.width-26*f)/2, window.height - 3*s + 13*f)
timer = Timer((3/4)*(window.width-26*f), window.height - 3*s + 13*f)
flagCounter = Number(board.mines, (1/4)*(window.width-26*f), window.height - 3*s + 13*f)
playerBoard = PlayerBoard(board, s, s, timer, smile, flagCounter)

''' Image Initialization '''
images = {}
images['flag'] = pyglet.image.load('images/sprites.png').get_region(x=4*s, y=s*3+f, width=s, height=s)
images['unknown'] = pyglet.image.load('images/sprites.png').get_region(x=3*s, y=s*3+f, width=s, height=s)
images['blank'] = pyglet.image.load('images/sprites.png').get_region(x=5*s, y=s*3+f, width=s, height=s)

for i in range(0, 3):
	images['mine-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=s*i, y=s*3+f, width=s, height=s)
for i in range(0, 9):
	images['number-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=s*i, y=s*4+1, width=s, height=s)
for i in range(0, 11):
	images['timer-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=13*i*f, y=26*f, width=13*f, height=23*f)
for i in range(0, 5):
	images['smile-'+str(i)] = pyglet.image.load('images/sprites.png').get_region(x=26*f*i,y=0,width=26*f,height=26*f)


''' Events '''
@window.event
def on_draw():
	window.clear()
	playerBoard.draw(images, f)
	timer.draw(images, f)
	smile.draw(images)
	flagCounter.draw(images, f)

@window.event
def on_mouse_release(x, y, button, modifiers):
	playerBoard.mouse(x, y, button, pyglet.window.mouse, f)
	smile.released(x, y, button, pyglet.window.mouse, f)
	if smile.reset:
		resetGame()

@window.event
def on_mouse_press(x, y, button, modifiers):
	smile.pressed(x, y, button, pyglet.window.mouse, f)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.H:
    	SingleStepSolver(playerBoard)
    elif symbol == pyglet.window.key.P:
    	timer.toggleAutomation(playerBoard)

''' Reset Game '''
def resetGame():
	smile.reset = False
	board.createBoard()
	playerBoard.createBoard()
	timer.time.value = 0
	timer.running = True
	flagCounter.value = board.mines
	
''' Startup '''
pyglet.clock.schedule_interval(timer.update, .05)
pyglet.app.run() 