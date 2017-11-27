import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    # Create 35 question and answer files each
    quizFile = open("./capitals-quiz/quiz_file%s.txt" % (quizNum+1), "w")
    answerFile = open("./capitals-quiz/answer_file%s.txt" % (quizNum+1), "w")

    # Create a header
    quizFile.write("Name:\nDate:\nPeriod:\n\n")
    quizFile.write((" " * 20) + "State Capitols Quiz (Form %s)" % (quizNum+1))
    quizFile.write("\n\n")
    
    # Create 50 different questions for each file, 1 right and 3 wrong answers
    states = list(capitals.keys())
    random.shuffle(states)

    for state in states:
        quizFile.write(state + "?\n")
        for i in range(4):
            quizFile.write("\t" + str(i) + "\n")
        quizFile.write("\n")

    # Log answer for each of the 50 questions

    quizFile.close()
    answerFile.close()