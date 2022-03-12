import random

class Dice:
    def roll(self):
        first=random.randint(1,6)
        secnd=random.randint(1,6)
        return first,secnd # this is acts like tuple ..

dice=Dice()
print(f"\n    Rolling two dice at the same time : ")
print(dice.roll())