import pyglet

window = pyglet.window.Window()
@window.event
def on_draw():
	window.clear()
	timer.label.draw()
	playerBoard.draw(100, 100, images)
	for i in range(0, 9):
		images['number-'+str(i)].blit(16*i, 0)
	for i in range(0, 10):
		images['timer-'+str(i)].blit(13*i, 16)

@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		print ('The left mouse button was pressed.')