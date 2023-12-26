# project: rock, paper, scissors game
# created: 12/14/2023

import random

# lists exit as false so the game can run, score is kept here, and possible exit calls from user
exit = False
exit_calls = ["exit", "done", "quit", "q", "e", "stop", "close", "end"]
user_points = 0
computer_points = 0

# asks for user choice and determines computer choice
while not exit:
  options = ["rock", "paper", "scissors", "r", "p", "s"]
  user_choice = input("\nChoose rock, paper, scissors, or exit: ").lower().strip()
  computer_choice = random.choice(options)

  # if user chooses exit, game ends with score listed
  if user_choice in exit_calls and (user_points >= 0 or computer_points >= 0):
    print("\nThanks for playing!")
    print(f"You scored {user_points} points and the computer scored {computer_points} points.")
    exit = True

  # lists all possible outcomes and modifies score accordingly
  if user_choice == "rock" or user_choice == "r":
    if computer_choice == "rock" or computer_choice == "r":
      print("\nYour choice was rock, the computer chose rock.")
      print("It's a tie!")
    elif computer_choice == "paper" or computer_choice == "p":
      print("\nYour choice was rock, the computer chose paper.")
      print("The computer wins! Paper covers rock.")
      computer_points += 1
    elif computer_choice == "scissors" or computer_choice == "s":
      print("\nYour choice was rock, the computer chose scissors.")
      print("You win! Rock smashes scissors.")
      user_points += 1

  elif user_choice == "paper" or user_choice == "p":
    if computer_choice == "rock" or computer_choice == "r":
      print("\nYour choice was paper, the computer chose rock.")
      print("You win! Paper covers rock.")
      user_points += 1
    elif computer_choice == "paper" or computer_choice == "p":
      print("\nYour choice was paper, the computer chose paper.")
      print("It's a tie!")
    elif computer_choice == "scissors" or computer_choice == "s":
      print("\nYour choice was paper, the computer chose scissors.")
      print("The computer wins! Scissors cuts paper.")
      computer_points += 1

  elif user_choice == "scissors" or user_choice == "s":
    if computer_choice == "rock" or computer_choice == "r":
      print("\nYour choice was scissors, the computer chose rock.")
      print("The computer wins! Rock smashes scissors.")
      computer_points += 1
    elif computer_choice == "paper" or computer_choice == "p":
      print("\nYour choice was scissors, the computer chose paper.")
      print("You win! Scissors cuts paper.")
      user_points += 1
    elif computer_choice == "scissors" or computer_choice == "s":
      print("\nYour choice was scissors, the computer chose scissors.")
      print("It's a tie!")
  elif user_choice not in options and user_choice not in exit_calls:
    print("\nInvalid input, please try again.")