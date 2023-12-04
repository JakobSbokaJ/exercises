import random

class Die():

    def __init__(self,numSides=6):
        self.numSides = numSides

    def roll_die(self):
        print(f"Landed on {random.randint(1,self.numSides)}")

mydie = Die(12)
for i in range(10):
    mydie.roll_die()