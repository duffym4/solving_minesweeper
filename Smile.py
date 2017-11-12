
class Smile(object): 
    def __init__(self):
        pass
    def draw(self,images,scale,x,y,smileNum):
        images['smile-'+str(smileNum)].blit(x,y)
  
