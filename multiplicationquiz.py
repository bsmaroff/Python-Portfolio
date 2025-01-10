#Benjamin Smaroff
#1/8/25
#Multiplication Quiz


#Intialize
import random
correct = 0
incorrect = 0
#Functions
def question_1():
    global correct
    global incorrect
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    total = num1*num2
    answer = int(input("What is " + str(num1) + " times " + str(num2)))
    if answer == total:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect")
        incorrect = incorrect + 1
def question_2():
    global correct
    global incorrect
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    total = num1*num2
    answer = int(input("What is " + str(num1) + " times " + str(num2)))
    if answer == total:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect")
        incorrect = incorrect + 1
def question_3():
    global correct
    global incorrect
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    total = num1*num2
    answer = int(input("What is " + str(num1) + " times " + str(num2)))
    if answer == total:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect")
        incorrect = incorrect + 1
def question_4():
    global correct
    global incorrect
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    total = num1*num2
    answer = int(input("What is " + str(num1) + " times " + str(num2)))
    if answer == total:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect")
        incorrect = incorrect + 1
def question_5():
    global correct
    global incorrect
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    total = num1*num2
    answer = int(input("What is " + str(num1) + " times " + str(num2)))
    if answer == total:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect")
        incorrect = incorrect + 1
def quiz():
    print("Welcome to Multiplication Practice")
    print("Answer each question to improve your skills")
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    print(str(correct) + " out of 5 correct")
#Main
quiz()





