import os
import pygal
from collections import defaultdict

path = "./helloworld.txt"
fileObj = open(path)
contents = fileObj.read()
fileObj.close()

barchart = pygal.Bar()
barchart.title = "Frequency of Letters in Text File"
barchart.x_title = 'Letter'
barchart.y_title = 'Frequency'

alphaDict = defaultdict(int)

for char in contents:
    if char.isalpha():
        alphaDict[char.lower()] += 1

for k, v in sorted(alphaDict.items()):
    barchart.add(k, v)

barchart.render_to_file("letter_frequency_multi_variable.svg")