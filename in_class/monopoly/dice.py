import random

class Dice:
    """A pair of dice"""
    sides = 6

    def roll(self):
        """Return a list with two rolls"""
        roll1 = random.randint(1,self.sides)
        roll2 = random.randint(1,self.sides)
        return [roll1, roll2]
