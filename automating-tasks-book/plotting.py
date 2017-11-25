import os
import pygal
from collections import defaultdict

path = "./helloworld.txt"
fileObj = open(path)
contents = fileObj.read()
fileObj.close()

barchart = pygal.Bar()
alphaDict = defaultdict(int)

for char in contents:
    if char.isalpha():
        alphaDict[char.lower()] += 1

for k, v in sorted(alphaDict.items()):
    barchart.add(k, v)
    # print(str(k) + ": " + str(v))

barchart.render_to_file("plotting.svg")