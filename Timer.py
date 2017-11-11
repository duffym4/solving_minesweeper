import datetime
import time
import pyglet
window = pyglet.window.Window()
class Timer(object): 
    def __init__(self):
        self.label = pyglet.text.Label('0',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
        self.start()
    def start(self):
            self.time = 0
            return self.time   
    def update(self,dt):
        self.time += dt
        self.label.text = str(int(self.time))
