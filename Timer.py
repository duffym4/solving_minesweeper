import datetime
import time
from Number import *
from SingleStepSolver import *
from Button import *


class Timer(object): 
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.f = f
        self.runButton = Button(self.x - 26*self.f, self.y, "play")
        self.helpButton = Button(self.x + 2*26*self.f, self.y, "help")
        self.automatic = False
        self.start()

    ''' reset timer and set running to true '''
    def start(self):
        self.time = Number(0, self.x, self.y)
        self.running=True
        return self.time.value

    ''' only update when timer should be running .. '''
    def update(self,dt):
        if self.running:

            ''' if the runbutton was pressed, toggle automatic '''
            if self.runButton.bang:
              self.automatic = not self.automatic
              self.runButton.bang = False


            ''' if the helpbutton was pressed, display hint '''
            if self.helpButton.bang:
              SingleStepSolver(self.playerBoard)
              self.helpButton.bang = False

            ''' increment timer, call a new hint if automatic mode is on '''
            self.time.value = min(999,self.time.value+.05)
            if self.automatic:
              if SingleStepSolver(self.playerBoard) == "stop":
                self.automatic = False

    def stop(self):
        self.running=False

    ''' pass mouse queues to buttons '''
    def pressed(self, x, y, button, mouse, f):
      self.runButton.pressed(x, y, button, mouse, f)
      self.helpButton.pressed(x, y, button, mouse, f)

    def released(self, x, y, button, mouse, f):
      self.runButton.released(x, y, button, mouse, f)
      self.helpButton.released(x, y, button, mouse, f)

    ''' draw all included objects '''
    def draw(self,images):
        self.time.draw(images, self.f)
        self.runButton.draw(images)
        self.helpButton.draw(images)
            