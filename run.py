import random

#the game with loop function
while True:
    player_move = input("Make your move (rock, paper, scissors):")
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    print(f"\nYour choice {player_move}, computers choice {computer_move}.\n")
#determines winner
    if player_move == computer_move:
        print(f"It's a tie! Both chose {player_move}")
    elif player_move == "rock":
        if computer_move == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose...")
    elif player_move == "scissors":
        if computer_move == "paper":
            print("Scissors beat paper! You win!")
        else:
            print("Rock beats scissors! You lose...")
    elif player_move == "paper":
        if computer_move == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beat paper! You lose...")
#question for player to continue och quit game
    do_over = input("One more time? (yes/no):")
    if do_over.lower() == "no":
        break
    if do_over.lower() == "yes":
        continue
    else:
        print("Make a valid choice! (yes/no)")
        break


