# Guess the number that computer has randomly generated.

import random as rand


def guess(x):
    name = input("Enter your name to begin the game....")
    trye = 6
    random_number = rand.randint(1, (x-1))
    guess = 0
    while (guess != random_number):
        try:
            if (trye != 0):
                print()
                guess = int(
                    input(f"Computer has randomly generated the number between 0 -{x} guess it.."))

                if (guess < 50 and guess > 0):
                    trye -= 1
                    if random_number > guess:
                        print(f" Sorry try again >> Too low  << You have {
                              trye} guess left..")
                    elif random_number < guess:
                        print(f" Sorry try again >> Too High << You have {
                              trye} guess left..")
                    else:
                        print(f"Congratulations {
                              name} you guess the correct answer that is {guess} !! (: ")
                        break
                else:
                    print(f"{name}, you dumb bro does {
                          guess} comes between 0 and 50 ? SMH")
            else:
                print(f"{name} you lose the game you fricking loser    >_<      ")

                print(f" The random number was {random_number}")

                break
        except:
            print("Enter the nummerical number not string.")


guess(50)
