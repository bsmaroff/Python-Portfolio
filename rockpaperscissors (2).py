#Benjamin Smaroff
#1/6/25
#Rock Paper Scissors
#Initalize
import random
wins = 0
losses = 0
ties = 0
#Functions
def rpsgame():
    global wins
    global losses
    global ties
    print("Welcome to Rock, Paper, Scissors")
    while True:
        print("Please select either rock, paper, or scissors")
        player = input("Selection: ")
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("Computer selected Rock")
        if computer == 2:
            computer = "paper"
            print("Computer selected Paper")
        if computer == 3:
            computer = "scissors"
            print("Computer selected Scissors")

        if player == computer:
            print("You tied")
            ties = ties + 1
        elif player == "rock" and computer == "scissors":
            print("Congrats, you won!")
            wins = wins + 1
        elif player == "scissors" and computer == "paper":
            print("Congrats, you won!")
            wins = wins + 1
        elif player == "paper" and computer == "rock":
            print("Congrats, you won!")
            wins = wins + 1
        elif player == "rock" and computer == "paper":
            print("You lost")
            losses = losses + 1
        elif player == "scissors" and computer == "rock":
            print("You lost")
            losses = losses + 1
        else:
            print("You lostt")
            losses = losses + 1

        print(str(wins) + " wins, " + str(ties) + " ties, " + str(losses) + " losses")

        play = input("Would you like to play again?")
        if play == "no":
            print("Thanks for Playing")
            break
#Main
rpsgame()
