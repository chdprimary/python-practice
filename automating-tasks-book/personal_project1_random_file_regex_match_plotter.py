# Create a program that does the following:
#   Takes, from the user, the number of times N to run the program
#   Takes, from the user, a regular expression R
#   N times, the program will:
#       Create a directory under the current directory
#       Create 100 files each with 1 KB of randomly generated characters inside this directory
#       Search each of the 100 files for the regular expression, keeping track of the number of matches
#       Append the total number of matches to a list
#       Destroy the directory
#   Display a bar chart which plots the number of times we've gotten each number of total matches (i.e.
#   the domain will be the total number of matches per iteration and the range will be the number, over
#   all iterations, that we've received a particular total match number).
#
#   Ok go.

import os
import random
import shutil
import re
import pygal

numIterations = input('How many times would you like to run the program? ')
userRegex = input('What regular expression would you like to search for? ')

def runProgram():
    # Create directory
    os.mkdir('practice-project1')
    os.chdir('practice-project1')

    numeralASCII = list(map(chr, range(48, 58)))
    upperCaseASCII = list(map(chr, range(65, 91)))
    lowerCaseASCII = list(map(chr, range(97, 123)))
    possibleChars = numeralASCII + upperCaseASCII + lowerCaseASCII + ['\n'] + [' '] * 10 # move spaceNum to var

    # Create files
    for i in range(100):
        fileobj = open('textfile%s.txt' % (i+1), 'w')
        for j in range(1000):
            fileobj.write(str(random.choice(possibleChars)))
        fileobj.close()

    # Find regex matches
    userRegexObj = re.compile(userRegex)
    totalMatches = 0
    for i in range(100):
        fileobj = open('textfile%s.txt' % (i+1), 'r')
        for line in fileobj.readlines():
            matches = userRegexObj.findall(line)
            totalMatches += len(matches)
        fileobj.close()

    # Delete directory, files
    os.chdir('..')
    shutil.rmtree('practice-project1', ignore_errors=True)

    return totalMatches

barchart = pygal.Bar()
domain = [0] * 1000
for i in range(int(numIterations)):
    totalMatches = runProgram()
    domain[totalMatches] += 1

barchart.add('Total Matches', domain)
barchart.render_to_file('plot.svg')