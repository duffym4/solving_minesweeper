import datetime
import time

class Timer(object): 
    def __init__(self):
        self.start()
    def start(self):
            self.time = 0
            return self.time   
    def update(self,dt):
        self.time += dt