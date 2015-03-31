# Lab 7 problem 3
# Maximilian Lemos

from Dice import *

die1 = Dice()
die2 = Dice(4)
die3 = Dice(12)


one = die1.roll()
two = die2.roll()
three = die3.roll()
total = one + two + three

print("Roll one: ", one)
print("Roll two: ", two)
print("Roll three: ", three)
print("Sum of all Rolls: ", total)

