import random

startstring = "Hello, This Is A Random Number Generator, And A Magic 8 Ball"


def start():
    print(startstring)
    ask_game()


def ask_game():
    ask = input("Do You Want To Do A Magic 8 Ball, Or A Random Number Generator? ")
    if ask == "Random Number Generator":
        rng()
    elif ask == "Magic 8 Ball":
        eight_ball()
    else:
        print("Check Your Spelling")
        ask_game()


def rng():
    int1 = input("What Do You Want The First Number To Be? ")
    int2 = input("What Do You Want The Second Number To Be? ")
    num = random.randint(int(int1), int(int2))
    print(num)
    restart()


def eight_ball():
    input("What Is Your Question? ")
    ans = random.randint(1, 8)
    if ans == 1:
        print("Ask Another Question")
    elif ans == 2:
        print("No")
    elif ans == 3:
        print("Definitely Not")
    elif ans == 4:
        print("Probably Not")
    elif ans == 5:
        print("Maybe")
    elif ans == 6:
        print("Im Pretty Sure")
    elif ans == 7:
        print("Almost Certain")
    elif ans == 8:
        print("Yes.")
    restart()


def restart():
    inp = input("Do You Want To Go Again? Y/N ")
    if inp == "Y":
        ask_game()


start()
