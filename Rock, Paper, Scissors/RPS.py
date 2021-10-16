import random


def start():
    print("Welcome To Rock, Paper, Scissors: Python Edition!")
    aidecision()


def playerdecision(cspeech):
    pspeech = input("Will You Do Rock, Paper, Or Scissors? ")
    result(cspeech, pspeech)


def aidecision():
    cspeech = random.randint(1, 3)
    playerdecision(cspeech)


def result(cspeech, pspeech):
    if pspeech == "Rock":
        if cspeech == 1:
            print("Tie!")
            aidecision()
        elif cspeech == 2:
            print("Paper Beats Rock, So You Lose!")
            aidecision()
        elif cspeech == 3:
            print("Rock Beats Scissors, So You Win!")
            aidecision()
    elif pspeech == "Paper":
        if cspeech == 1:
            print("Paper Beats Rock, So You Win!")
            aidecision()
        elif cspeech == 2:
            print("Tie!")
            aidecision()
        elif cspeech == 3:
            print("Scissors Beats Paper, So You Lose!")
            aidecision()
    elif pspeech == "Scissors":
        if cspeech == 1:
            print("Rock Beats Scissors, So You Lose!")
            aidecision()
        elif cspeech == 2:
            print("Scissors Beats Paper, So You Win!")
            aidecision()
        elif cspeech == 3:
            print("Tie!!")
            aidecision()
    else:
        print("You Might Have Spelled That Wrong, Try Again.")
        aidecision()


start()
