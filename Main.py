import pyglet
from Board import *
from PlayerBoard import *
from Timer import *
from Smile import *
board = Board(30, 16, 10)
timer = Timer()

spriteSheet = pyglet.image.load('images/sprites.png')
f = int(spriteSheet.width/144)
s = f*16
window = pyglet.window.Window(caption="Hackathon Minesweeper", width=s*(2+board.ncols), height=s*(4+board.nrows))

playerBoard = PlayerBoard(board, s, s, timer)
smile=Smile()
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
@window.event
def on_draw():
	window.clear()
	playerBoard.draw(images,f)
	timer.draw(images,f,400,400)
	images['smile-1'].blit(100,100)

@window.event
def on_mouse_press(x, y, button, modifiers):
	playerBoard.mouse(x, y, button, pyglet.window.mouse, f)

pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run() 
