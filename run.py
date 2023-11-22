import random

#the game moves
player_move = input("Make your move (rock, paper, scissors):")
moves = ["rock", "paper", "scissors"]
computer_move = random.choice(moves)
print(f"\nYour choice {player_move}, computers choice {computer_move}.\n")