# Maximilian Lemos
# lab8 problem 3

class Circle():
    count = 0

    def __init__(self, r = 1):
        if r >= 0:
            self.radius = r
        else:
            self.radius = -1 * r
        Circle.count = Circle.count + 1

    def storeradius(self,r):
        if r >= 0:
            self.radius = r
        else:
            self.radius = -1 * r

    def calcarea(self):
        return 3.14 * self.radius ** 2

    def calccir(self):
        return 2 * 3.14 * self.radius

    def returnradius(self):
        return self.radius

class Cylinder(Circle):
    import math
    def __init__(self, h = 1, r = 1):
        self.height = h
        self.radius = r
        Circle.count = Circle.count + 1

    def storeheight(self, h):
        self.height = h
        
    def calcvolume(self):
        vol = 3.1415 * (self.radius**2) * self.height
        return vol
    
    def calcarea(self):
        ar = (2 * 3.1415 * self.radius * self.height) + (2 * 3.1415 * (self.radius**2))
        return ar

        
##from circleclass1 import *
##one = Cylinder()
##one.storeradius(10)
##one.storeheight(6)
##one.calccir()
##one.calcarea()
##one.calcvolume()

