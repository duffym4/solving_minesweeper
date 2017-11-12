class Number(object): 

    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def draw(self,images,scale):

        ''' determine the absolute value, integer value of the game timing '''
        i = abs(int(self.value))

        ''' print the two LSBs '''
        images["timer-"+str(int(i%10))].blit(self.x, self.y)
        images["timer-"+str(int(i/10%10))].blit(self.x-13*scale,self.y)

        ''' negative sign or MSB '''
        if self.value < 0:
            images["timer-10"].blit(self.x-26*scale,self.y) 
        else:
            images["timer-"+str(int(i/100%100))].blit(self.x-26*scale,self.y)  
            