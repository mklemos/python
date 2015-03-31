## Maximilian Lemos
## Lab8 problem 1, 2
##
##
## +  __add__(self, <value>)
## *  __mul__(self, <value>)
## ** __pow__(self, <value>)
## len(<value>) __len__(self)
## <var>[<loc>]=<value> __setitem__(self, <loc>, <value>)
## del <var>[<loc>] __delitem__(self, <loc>)

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
        if loc < len(self.str):
            temp1 = self.str[0:loc]
            temp2 = self.str[loc+1:]
            self.str = temp1 + value + temp2
        if len(self.str) == 0:
            self.str = value

    def __mul__(self, times):
        self.str = self.str * times

    def __len__(self):
        return len(self.str)

    def __delitem__(self, index):
            self.str = self.str[:index] + self.str[index+1:]


##    def __delitem__(self, index):
##            counter = 0
##            self.str = self.str[index:index+1]
    
##    def __delitem__(self, index):
##       if 'g' in self.str:
##           self.str = self.str[:index] + self.str[index+1:]
##       if 'y' in self.str:
##           self.str = self.str[:index] + self.str[index+1:]
##       if 'b' in self.str:
##           self.str = self.str[:index] + self.str[index+1:]

##    def __delitem__(self, index):
##        g = 'g'
##        y = 'y'
##        b = 'b'
##        for g in self.str[index]:
##            self.str = self.str[:index] + self.str[index+3:]

## Problem ONE 
## >>> from mutstring import *
## >>> one = Mutstr("trythis")
## >>> len(one)
## 7
## >>> one * 3
## >>> one.get()
## 'trythistrythistrythis'

## Problem TWO
## >>> from mutstring import *
## >>> one = Mutstr('oogyboogy')
## >>> del one[2]
## >>> one.get()
## 'oooogy'

## >>> from mutstring import *
## >>> one = Mutstr('oogyboogy')
## >>> del one[4]
## >>> one.get()
## 'oogyoogy'
## >>> del one[3]
## >>> one.get()
## 'oogoogy'
## >>> del one[2]
## >>> one.get()
## 'oooogy'


