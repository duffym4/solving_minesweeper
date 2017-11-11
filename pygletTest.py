import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('0',
						  font_name='Times New Roman',
						  font_size=36,
						  x=window.width//2, y=window.height//2,
						  anchor_x='center', anchor_y='center')
image = pyglet.image.load('images/tiles/Closed.png')

@window.event
def on_draw():
	window.clear()
	label.draw()
	image.blit(0, 0)


def update(dt):

	label.text = '5'
    # ...
pyglet.clock.schedule_interval(update, 0.1)
pyglet.app.run()