
class Tile(object):
    def __init__ (self, x_, y_):
        self.x = x_
        self.y = y_

        self.value = -1
        self.imageKey = "blank"
        
    def activate(self, value):
        self.value = value
        
        if self.value in range(0,9):
            self.imageKey = 'number-' + value 
        elif self.value == 9:
            self.imageKey = 'bomb'
        elif self.value == 10:
            self.imageKey = 'flag'
        elif self.value == -1:
            self.imageKey = 'blank'

    def draw(self, images):
        images[self.imageKey].blit(self.x, self.y)



