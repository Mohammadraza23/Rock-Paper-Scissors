import random

user_score = 0
computer_score = 0


while True:
    print()
    choice = input(" Choose one: Rock, Paper, Scissors: ").lower()

    while choice != "rock" and choice != "paper" and choice != "scissors":
        choice = input("Invalid, try again: ").lower()

    x = random.randint(1, 3)
    if x == 1:
        computer = "rock"

    elif x == 2:
        computer = "paper"

    elif x == 3:
        computer = "scissors"

    print()
    print(" User Choice : ", choice)
    print(" Computer Choice : ", computer)
    print()

    if choice == "rock":
        if computer == "rock":
            print("Tie")
        elif computer == "paper":
            print("You lost")
            computer_score += 1
        elif computer == "scissors":
            print("You won!!")
            user_score += 1

    elif choice == "paper":
        if computer == "paper":
            print("Tie")
        elif computer == "rock":
            print("You won!! ")
            user_score += 1
        elif computer == "scissors":
            print("You lost")
            computer_score += 1

    elif choice == "scissors":
        if computer == "scissor":
            print("Tie")
        elif computer == "rock":
            print("You Lost ")
            computer_score += 1
        elif computer == "paper":
            print("You won!!")
            user_score += 1

    print()
    print(" You have", user_score, "wins")
    print(" The computer has ", computer_score, "wins")
    print()

    play_again = input(" Would you like to play again? (Yes/No) ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Invalid, try again ").lower()

    if play_again == "no":
        break
