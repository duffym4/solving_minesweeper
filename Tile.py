
#Representation of a single tile on the board
class Tile(object):
    def __init__ (self, x_, y_, flagCounter_):
        self.x = x_
        self.y = y_
        self.flagCounter = flagCounter_

        self.value = -1
        self.imageKey = "blank"
    
    #changes a tile's value and as a result its imageKey
    def activate(self, value):
        self.value = value
        self.updateImages()

    #change the imageKey to its corisponding value
    def updateImages(self):
        if self.imageKey == 'flag':
            self.flagCounter.value+=1

        if self.value in range(0,9):
            self.imageKey = 'number-' + str(self.value)
        elif self.value == 9:
            self.imageKey = 'mine-0'
        elif self.value == -2:
            self.imageKey = 'flag'
        elif self.value == -3:
            self.imageKey = 'unknown'
        elif self.value == -1:
            self.imageKey = 'blank'

        if self.imageKey == 'flag':
            self.flagCounter.value-=1

    #cycle value between unmarked, flag and question mark
    def rotateMarking(self):
        self.value -= 1
        if self.value == -4:
            self.value = -1
        self.updateImages()

    #draw the tile according to its imageKey
    def draw(self, x0, y0, images, scale):
        images[self.imageKey].blit(x0 + self.x*16*scale, y0 + 16*scale*self.y)



