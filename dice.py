import random

class Dice:
    def __init__(self, sides=6): #give a dice a default value of 6 sides
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
dice = Dice(14)
print(dice.roll())

dice2 = Dice()
print(dice2.roll())