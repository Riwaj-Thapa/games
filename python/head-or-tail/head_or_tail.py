#  Coin flip best of five....
import random as rand
name = input("Enter you name to play the game...")
win = 0
lose = 0
while (True):
    chose = input(f"Choose 'Head' or 'Tail' ....")

    if (chose == "Head" or chose == "Tail"):
        computer = rand.randint(1, 2)
        answer = ""
        if (computer == 1):
            answer = "Head"
        else:
            answer = "Tail"

        if (chose == answer):
            print(f"You choose {chose} and coin flipped {answer}")
            win += 1
            print(f" Win: {win} and lose: {lose}")
        else:
            print(f"You choose {chose} and coin flipped {answer}")
            lose += 1
            print(f" Win: {win} and lose: {lose}")

        if (win >= 3 or lose >= 3):
            if (win > lose):
                print(f"Congratulation {name} you win the best of five with {
                      win} wins and {lose} loses.")
                break
            else:
                print(f" Sorry {name} you lose the best of five with {
                      win} wins and {lose} loses. Try again !! ")

                break
    else:
        print(f" Type either 'Head' or 'Tail' there is no other options.....")
