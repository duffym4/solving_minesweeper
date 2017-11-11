
class Tile(object):
    def __init__ (self, x_, y_):
        self.x = x_
        self.y = y_

        self.value = -1
        self.imageKey = "blank"

        
    def x(self):
        return self.x
    def y(self):
        return self.y
  
    
    def value(self):
        return value
    def imageKey(self):
        return imageKey
        
        
    def activate(self, value):
        value = value
        
        if value in range(0,9):
            imageKey = 'number-' + value 
        elif value == 9:
            imageKey = 'bomb'
        elif value == 10:
            imageKey = 'flag'
        elif value == -1:
            imageKey = 'blank'
