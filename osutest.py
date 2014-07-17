#!/usr/bin/python
import random

osiLayers = {
    "Layer 1: ": "physical",
    "Layer 2: ": "data link",
    "Layer 3: ": "network",
    "Layer 4: ": "transport",
    "Layer 5: ": "session",
    "Layer 6: ": "presentation",
    "Layer 7: ": "application"
}

tcpipLayers = {
    "Layer 1: ": "network interface",
    "Layer 2: ": "internet",
    "Layer 3: ": "transport",
    "Layer 4: ": "application"
}

score = 0


def runTest(test):
    global score
    while True:
        questionList = list(test.keys())
        questionList = random.choice(questionList)
        question = questionList
        lAnswer = test[question]
        answer = input("What is the name of %s \n" % question).lower()
        if answer == lAnswer:
            userC = input('Correct...Next question incoming press enter to continue. "c" to change testes, "x" to exit \n\n').lower()
            score += 1
            print('Score: ', score)

        else:
            while answer != lAnswer:
                score -= 1
                print('Score: ',score)
                answer = input("Wrong...Please try again.\n").lower()

            userC = input('Correct...Next question incoming press enter to continue. "c" to change testes, "x" to exit \n\n').lower()
            score += 1
            print('Score: ',score)
        if userC == 'c':
            userTest()
        if userC == 'x':
            exit(0)


def userTest():

    global osiLayers
    global tcpipLayers

    userChoice = input("Choose what model you wish to study\n").lower()
    if userChoice == 'osi':
        test = osiLayers
    if userChoice == 'tcp':
        test = tcpipLayers
    runTest(test)

userTest()
