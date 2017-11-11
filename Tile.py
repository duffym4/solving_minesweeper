import pyglet
import os

class Tile(object):
    def __init__ (self, x_, y_, value_):
        self.x = x_
        self.y = y_
        self.value = value_
        self.revealed = False
        
    def x(self):
        return self.x
    def y(self):
        return self.y
    def revealed(self):
        return self.revealed    
    
    def value(self):
        if not self.revealed:
            return -1
        else:
            return self.value
        
    def drawTile(self):
        #pyglet.resource.path = ['cd /cygdrive/c/Users/ansela3/My Documents/GitHub/hackathon/images/tiles']
        #pyglet.resource.reindex()  
        
        image = pyglet.image.load('Closed.png')
        '''
        if not revealed:
            image = pyglet.resource.image('closed.png')
        else:
            if value == 0:
                image = pyglet.resource.image('0.png')'''
                
        image.blit(0, 0)
        
        
  
        

if __name__ == "__main__": 
    
    window = pyglet.window.Window()
    window.clear()
    
    a = Tile(0,0,0)
    a.drawTile()
    
    pyglet.app.run()
        