import matplotlib.pyplot as plt

from random import choice

class RandomWalk():
    def __init__(self, num_steps=5000):
        self.num_steps = num_steps
        self.x_coordinates = [0]
        self.y_coordinates = [0]

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([1,2,3,4,5])
        return direction * distance

    def draw_walk(self):
        while len(self.x_coordinates) < self.num_steps:
            new_x_coordinate = self.x_coordinates[-1] + self.get_step()
            new_y_coordinate = self.y_coordinates[-1] + self.get_step()

            self.x_coordinates.append(new_x_coordinate)
            self.y_coordinates.append(new_y_coordinate)

while True:
    rw = RandomWalk()
    rw.draw_walk()

    plt.title("Draw me like one of your french girls")
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.scatter(
        rw.x_coordinates, 
        rw.y_coordinates, 
        c=range(0, rw.num_steps), 
        cmap=plt.cm.Blues, 
        edgecolors=None, 
        s=2)

    # plt.plot(rw.x_coordinates, rw.y_coordinates, linewidth=1)

    plt.scatter(0, 0, c="green", edgecolors=None, s=30)
    plt.scatter(rw.x_coordinates[-1], rw.y_coordinates[-1], c="red", edgecolors=None, s=30)
    plt.show()

    if input("Make another random walk? (y/n): ") == 'n':
        break