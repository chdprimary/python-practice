import random

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

die = Die(8)

results = []
for i in range(1,101):
    results.append(die.roll())

side_tallies = [0] * (die.num_sides+1)
for result in results:
    side_tallies[result] += 1

print(results)

for i in range(0, len(side_tallies)):
    print("Number of " + str(i) + "s: " + str(side_tallies[i]))