import random

choices = ["rock", "paper", "scissors"]
while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?:  ").lower()
        print ("your choice is wrong ")

    
    if computer == player:
        print("player: ", player)
        print("computer: ", computer)
        print ("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")

    elif player == "scissors":
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")

    play_again = input("Play again? yes/no: ").lower()
    if play_again != "yes":
        break
print("Bye!")

 

