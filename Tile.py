
class Tile(object):
<<<<<<< HEAD
    def __init__ (self, x_, y_):
        self.x = x_
        self.y = y_

        self.value = -1
        self.imageKey = "blank"

=======
    def __init__ (self, x_, y_, value_):
        x = x_
        y = y_
        value = value_
        revealed = False
>>>>>>> 2689aac5a6ecd517f19a175c68c1b33646c958ec
        
    def x(self):
        return x
    def y(self):
<<<<<<< HEAD
        return self.y
  
    
    def value(self):
        return value
    def imageKey(self):
        return imageKey
        
        
    def activate(self, value):
        value = value
=======
        return y
    def revealed(self):
        return revealed    
    
    def value(self):
        if not revealed:
            return -1
        else:
            return value
        
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
  
>>>>>>> 2689aac5a6ecd517f19a175c68c1b33646c958ec
        
        if value in range(0,9):
            imageKey = 'number-' + value 
        elif value == 9:
            imageKey = 'bomb'
        elif value == 10:
            imageKey = 'flag'
        elif value == -1:
            imageKey = 'blank'
