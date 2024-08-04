# Rock Paper Scissor game best of five...
from random import randint

win = 0
lose = 0
draw = 0
name = input("Enter the name to start the game...")


def rock():
    global win, lose, draw
    if computerr == "Rock" and choose == "Rock":
        print(final, " Draw.")
        draw += 1
    if computerr == "Rock" and choose == "Paper":
        print(final, " You Win.")
        win += 1
    if computerr == "Rock" and choose == "Scissor":
        print(final, " You loss.")
        lose += 1


def paper():
    global win, lose, draw
    if computerr == "Paper" and choose == "Rock":
        print(final, " You loss.")
        lose += 1
    if computerr == "Paper" and choose == "Paper":
        print(final, " Draw.")
        draw += 1
    if computerr == "Paper" and choose == "Scissor":
        print(final, " You Win.")
        win += 1


def scissor():
    global win, lose, draw
    if computerr == "Scissor" and choose == "Rock":
        print(final, " You Win.")
        win += 1
    if computerr == "Scissor" and choose == "Paper":
        print(final, " You loss.")
        lose += 1
    if computerr == "Scissor" and choose == "Scissor":
        print(final,  " Draw.")
        draw += 1


while True:
    choose = input("Choose Rock, Paper or Scissor by typing correctly ")
    if (choose == "Rock" or choose == "Paper" or choose == "Scissor"):
        computerrr = randint(1, 9)
        computerr = ""

        if (computerrr > 6 and computerrr <= 9):
            computerr = "Rock"
        if computerrr > 3 and computerrr <= 6:
            computerr = "Scissor"
        if computerrr >= 1 and computerrr <= 3:
            computerr = "Paper"

        final = " You choose: " + choose + " and Computer chooses: " + computerr + " so"

        if computerr:
            if computerr == choose:
                print(final, " Draw.")
                draw += 1
            elif (computerr == "Rock" and choose == "Scissor") or (computerr == "Paper" and choose == "Rock") or (computerr == "Scissor" and choose == "Paper"):
                print(final, " You loss.")
                lose += 1
            else:
                print(final, " You Win.")
                win += 1

            print(f"Score {win} wins, {lose} loses and {draw} draws")

        if win >= 3 or lose >= 3:
            if win > lose:
                print(f"Congratulation {name} you win the best of five game with {
                      win} wins, {lose} loses and {draw} draws.")
            else:
                print(f"Sorry {name} you lose the best of five game with {
                      win} wins, {lose} loses and {draw} draws.")
            break
    else:
        print("Type either 'Rock' , 'Paper' or 'Scissor' there are no other options..")
