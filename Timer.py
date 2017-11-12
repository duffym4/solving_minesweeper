import datetime
import time
from Number import *
from SingleStepSolver import *


class Timer(object): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.automatic = False
        self.start()
    def start(self):
        self.time = Number(0, self.x, self.y)
        self.running=True
        return self.time.value
    def update(self,dt):
        if self.running:
            self.time.value = min(999,self.time.value+1)
            if self.automatic:
              if SingleStepSolver(self.playerBoard) == "stop":
                self.toggleAutomation(self.playerBoard)
    def toggleAutomation(self, playerBoard):
      self.automatic = not self.automatic
      self.playerBoard = playerBoard
    def stop(self):
        self.running=False
    def draw(self,images,scale):
        self.time.draw(images, scale)
            