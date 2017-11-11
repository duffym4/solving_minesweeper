
class Tile(object):
    def __init__ (self, x_, y_):
        self.x = x_
        self.y = y_

        self.value = -1
        self.imageKey = "blank"
        
    def activate(self, value):
        self.value = value
        
        if self.value in range(0,9):
            self.imageKey = 'number-' + str(value)
        elif self.value == 9:
            self.imageKey = 'mine'
        elif self.value == 10:
            self.imageKey = 'flag'
        elif self.value == -1:
            self.imageKey = 'blank'

    def draw(self, x0, y0, images):
        images[self.imageKey].blit(x0 + self.x*16, y0 + 16*self.y)



