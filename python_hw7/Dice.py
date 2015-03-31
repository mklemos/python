# Lab 7 problem 3
# Maximilian Lemos

import random
class Dice():
    def __init__(self, sides = 6):
        self.sides = sides
        if self.sides < 4:
            self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)


