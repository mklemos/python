class Mutstr():

    def __init__(self,st = ""):
        self.str = st

    def change(self,loc,st):
        if loc < len(self.str):
            temp1 = self.str[0:loc]
            temp2 = self.str[loc+1:]
            self.str = temp1 + st + temp2
        if len(self.str) == 0:
            self.str = st

    def get(self):
        return self.str

    def __add__(self,more):
        self.str = self.str + more

    def __setitem__(self,loc,value):
        self.change(loc,value)  # you can call the change method because they do the same things its just a difference in form.
