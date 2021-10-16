import random


def start():
    print("This Is Guess A Number: Python Edition!")
    print("I Will Think Of A Number Between 1 And 5, And You Have To Guess It!")
    aiguessint()


def aiguessint():
    cnumber = random.randint(1, 5)
    playerguessint(cnumber)


def playerguessint(cnumber):
    pnumber = input("What Number Am I Thinking Of? ")
    result(cnumber, pnumber)


def result(cnumber, pnumber):
    if cnumber == int(pnumber):
        print("CORRECT!")
        aiguessint()
    else:
        print("WRONG!")
        aiguessint()


start()
