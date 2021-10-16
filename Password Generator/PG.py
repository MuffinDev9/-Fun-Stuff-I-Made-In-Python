import random


def start():
    print("This Is A Password Generator, But In Python!")
    wn()


def wn():
    q = input("Do You Want To Have A Word Password, Or A Number Password? ")
    if q == "Word":
        with open("Text", "r") as file:
            data = file.read()
            words = data.split()

            word_pos1 = random.randint(0, len(words) - 1)
            print("Word:", words[word_pos1])
    elif q == "Number":
        askn = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
        print(askn)


start()
