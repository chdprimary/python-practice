import matplotlib.pyplot

x1 = list(range(1,101))
x1_squared = [x**2 for x in x1]
#matplotlib.pyplot.plot(x1, x1_squared, linewidth=3)

matplotlib.pyplot.scatter(x1,
    x1_squared, 
    c=x1_squared, 
    cmap=matplotlib.pyplot.cm.Blues, 
    edgecolor="none", 
    s=50)

matplotlib.pyplot.axis([0,110,0,11000])
matplotlib.pyplot.title("Square Numbers", fontsize=24)
matplotlib.pyplot.xlabel("Value", fontsize=14)
matplotlib.pyplot.ylabel("Square of Value", fontsize=14)
matplotlib.pyplot.tick_params(axis="both", which="major", labelsize=14)

matplotlib.pyplot.show()
# matplotlib.pyplot.savefig("squares_plot.png", bbox_inches="tight")