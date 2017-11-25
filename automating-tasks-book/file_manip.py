import os
import re

def searchForE(text):
    eRegex = re.compile("(e)", re.IGNORECASE)
    groups = eRegex.findall(text)
    # print(groups, end="")
    # print(" " + str(len(groups)))

filepath = "./helloworld.txt"
fileobj = open(filepath, 'r')

print("|", end="")
lineLength = 1
for line in fileobj.readlines():
    for char in line:
        if char == "\n":
            print(" ", end="")
        else:
            print(char, end="")
        lineLength = lineLength + 1
        if lineLength == 20:
            print("|")
            print("|", end="")
            lineLength = 1
    # print(line.strip(), end="")
    # searchForE(line)

fileobj.close()