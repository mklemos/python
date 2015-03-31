class Parallel():
        count = 0
        def __init__(self, l=0, w=0, ang=0):
                self.length = l  #this should have a check to make sure positiv)
                self.width = w
                self.angle = ang
                Parallel.count = Parallel.count + 1
        def perimeter(self):
                print("par-perim")
                return 2 * self.length + 2 * self.width
        def area(self):
                import math #while in a method you cannot use the from math import form
                rad = self.angle * math.pi/180
                height = math.sin(rad)*self.width
                ar = height * self.length
                print("par-area")
                return ar
class Rectangle(Parallel):
        def __init__(self, l=0, w=0):
                self.length=l
                self.width=w
                Parallel.count += 1
        def area(self):
                print("rec-area")
                return self.length * self.width
class Rhombus(Parallel):
        def __init__(self, side = 0, ang = 0):
                self.width = side
                self.length = side
                self.angle = ang
                Parallel.count += 1
        def perimeter(self):
                print("Rhom-perim")
                return 4 * self.length
class Square(Rectangle, Rhombus):
        def __init__(self, side = 0):
                self.length = side
                self.width = side
                Parallel.count += 1
