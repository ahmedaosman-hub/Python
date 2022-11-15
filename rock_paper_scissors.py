import random

#Set a tuple of our options
options = ("rock", "paper", "scissors")

#Sets the game to always running
running = True


while running:
    #Player does not contain a choice yet while computer has chosen
    player = None
    computer = random.choice(options)

    #If player does not choose between our options
    while player not in options:
        player = input("rock, paper, scissors: ")

    #Display the results
    print(f"Player: {player}")
    print(f"Player: {computer}")

    #Determines the results
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    #Request if the user would like to play again
    play_again = input("Would you like to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing!")