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
import shutil
import random
import re
import pygal
import logging

NUM_RANDOM_TEXT_FILES = 100
SPACE_CHAR_FREQUENCY = 10

def runProgram(iteration, numIterations, userRegex):
    # Create directory
    os.mkdir('practice-project1')
    os.chdir('practice-project1')

    numeralASCII = list(map(chr, range(48, 58)))
    upperCaseASCII = list(map(chr, range(65, 91)))
    lowerCaseASCII = list(map(chr, range(97, 123)))
    possibleChars = numeralASCII + upperCaseASCII + lowerCaseASCII + ['\n'] + [' '] * SPACE_CHAR_FREQUENCY

    # Create files
    for i in range(NUM_RANDOM_TEXT_FILES):
        fileobj = open('textfile%s.txt' % (i+1), 'w')
        for j in range(1000):
            fileobj.write(str(random.choice(possibleChars)))
        fileobj.close()

    # Find regex matches
    userRegexObj = re.compile(userRegex)
    totalMatches = 0
    for i in range(NUM_RANDOM_TEXT_FILES):
        fileobj = open('textfile%s.txt' % (i+1), 'r')
        for line in fileobj.readlines():
            matches = userRegexObj.findall(line)
            totalMatches += len(matches)
        fileobj.close()

    # Delete directory, files
    os.chdir('..')
    shutil.rmtree('practice-project1', ignore_errors=True)

    logging.debug('(%s/%s): %s TRM over %s 1KB files' % (str(iteration+1), str(numIterations), str(totalMatches), str(NUM_RANDOM_TEXT_FILES)))
    return totalMatches

def main():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Starting...')

    numIterations = input('How many times would you like to run the program? ')
    userRegex = input('What regular expression would you like to search for? ')

    barchart = pygal.Bar()
    barchart.title = 'TRE Frequency (' + numIterations + ' iterations) of ' + userRegex
    domain = [0] * 10
    for i in range(int(numIterations)):
        totalMatches = runProgram(i, numIterations, userRegex)
        try:
            domain[totalMatches] += 1
        except IndexError:
            while len(domain) <= totalMatches:
                domain.append(0)
            domain[totalMatches] += 1

    barchart.add('TRE (Total Regex Matches)', domain)
    barchart.x_labels = range(0, len(domain))
    barchart.render_to_file('plot.svg')

    logging.debug('Done.')

main()