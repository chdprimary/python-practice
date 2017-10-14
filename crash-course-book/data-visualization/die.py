import random
import pygal

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

die_1 = Die()
die_2 = Die(10)

results = []
for i in range(50000):
    results.append(die_1.roll() + die_2.roll())

# print(results)

# side_tallies = [0] * (die_1.num_sides+1)
# for result in results:
#     side_tallies[result] += 1

max_result = die_1.num_sides + die_2.num_sides
side_tallies = []
for i in range(2, max_result+1):
    tally = results.count(i)
    side_tallies.append(tally)

# for i in range(1, len(side_tallies)):
#     print("Number of " + str(i) + "s: " + str(side_tallies[i]))

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = range(2, max_result+1)
hist.x_title = "Die Value"
hist.y_title = "Quantity"

hist.add("D6 + D6", side_tallies)
hist.render_to_file("d6_plus_d10_visual.svg")

# sum_of_tallies = sum(side_tallies)
# num_possible_values = len(side_tallies) - 1

# print("AVG: " + str(sum_of_tallies / num_possible_values))