import winsound
import time

def userInterface(qTime:int):
    print(f'\n=================================\nWelcome to interview practice! \n=================================\nType 1 to practice a few questions\nType 2 to adjust the response time (current time: {qTime} seconds)\nType 3 to add to the question bank\nType 0 to exit program\n' )
def addQuestion():
    newQ = input("What is the new question you would like to ask? ")
    with open ("interviewQuestions.txt", "a") as questions:
        questions.write(f'{newQ} \n')

def changeTime(qTime):
    print(F'Your current response time is: {qTime} seconds \n')
    qTime = input("Enter the number of seconds you want to have to respond to the question: ")
    return qTime

def printQuestion(questionSet, qTime):
    question = questionSet.pop()
    print(f'\n\n{question}\n\n')

    questionSet.add(question)
    start_time = time.time()
    time.sleep(int(qTime))

    frequency = 2500
    duration = 3000
    winsound.Beep(frequency, duration)
    print("Time's up! \n")
    time.sleep (5)

qTime = 120
questionSet = set()
i = 0
cont = 1
with open ("interviewQuestions.txt") as questions:
    for line in questions.readlines():
        questionSet.add(f'\n {line}')
        i += 1

while cont == 1:
    userInterface(qTime)
    userInput = input("What would you like to do? ")
    print(userInput)
    if int(userInput) == 1:
        printQuestion(questionSet, qTime)
        printQuestion(questionSet, qTime)
        printQuestion(questionSet, qTime)

    elif int(userInput) == 2:
        qTime = changeTime(qTime)

    elif int(userInput) == 3:
        addQuestion()
    elif int(userInput) == 0:
        cont = 0
        print("Exiting program. Have a great day!\n\n")