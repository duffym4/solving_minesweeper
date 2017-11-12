import datetime
import time
from Number import *


class Timer(object): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start()
    def start(self):
        self.time = Number(0, self.x, self.y)
        self.running=True
        return self.time.value
    def update(self,dt):
        if self.running:
            self.time.value = min(999,self.time.value+1)
    def stop(self):
        self.running=False
    def draw(self,images,scale):
        self.time.draw(images, scale)
            