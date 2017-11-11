import datetime
import time

class Timer(object): 
    def __init__(self):
        self.start()
    def start(self):
        self.time = 0
        return self.time   
    def update(self,dt):
        self.time = min(999,self.time+1)
    def draw(self,images,x,y):
        i=0
        images["timer-"+str(int(self.time%10))].blit(x,y)
        
        images["timer-"+str(int(self.time/10%10))].blit(x-13,y)
        images["timer-"+str(int(self.time/100%100))].blit(x-26,y)  
            