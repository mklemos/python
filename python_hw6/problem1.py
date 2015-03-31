# Lab 6 problem 1
# Maximilian Lemos

import random

def dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a,b

print("Roll one: ", dice())
print("Roll two: ", dice())
print("Roll three: ", dice())

if __name__=="__main__":
	dice()
	


