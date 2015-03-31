class Circle():
        count = 0
        def __init__(self):
                self.radius = 1
                Circle.count = Circle.count + 1
        def store_radius(self,r):
                if r >= 0:
                        self.radius = r
                else:
                        self.radius = -1 * r
        def return_radius(self):
                return self.radius
        def calc_area(self):
                return 3.14 * self.radius ** 2
        def calc_cir(self):
                return 2 * 3.14 * self.radius
