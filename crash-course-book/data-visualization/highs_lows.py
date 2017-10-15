import csv
import matplotlib.pyplot as plt

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    lows = []
    for row in reader:
        highs.append(int(row[1]))
        lows.append(int(row[3]))

    plt.plot(highs, c="red")
    plt.plot(lows, c="blue")

    plt.title("Daily high temperatures")
    plt.xlabel("Day", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()