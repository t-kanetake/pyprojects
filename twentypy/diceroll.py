# project: dice roll emulator
# created: 12/14/2023

import random

def roll_dice():

  # a list of ascii dice faces
  dice_dictionary = {
      1: (
          "┌─────────┐",
          "│         │",
          "│    ●    │",
          "│         │",
          "└─────────┘",
      ),
      2: (
          "┌─────────┐",
          "│  ●      │",
          "│         │",
          "│      ●  │",
          "└─────────┘",
      ),
      3: (
          "┌─────────┐",
          "│  ●      │",
          "│    ●    │",
          "│      ●  │",
          "└─────────┘",
      ),
      4: (
          "┌─────────┐",
          "│  ●   ●  │",
          "│         │",
          "│  ●   ●  │",
          "└─────────┘",
      ),
      5: (
          "┌─────────┐",
          "│  ●   ●  │",
          "│    ●    │",
          "│  ●   ●  │",
          "└─────────┘",
      ),
      6: (
          "┌─────────┐",
          "│  ●   ●  │",
          "│  ●   ●  │",
          "│  ●   ●  │",
          "└─────────┘",
      ),
  }

  # asks for input and rolls dice if complies
  roll = input("Roll the dice? (Yes/No): ")
  while roll.strip().lower() in ["Yes".strip().lower(), "y".strip().lower()]:
    print("Rolling the dice..." + "\n")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"You rolled a {dice1} and a {dice2}")
    print("\n".join(dice_dictionary[dice1]))
    print("\n".join(dice_dictionary[dice2]))

    roll = input("Roll the dice again? (Yes/No): ")

  # if user does not want to roll dice, program ends and catches invalid inputs
  if roll.strip().lower() in ["No".strip().lower(), "n".strip().lower()]:
    print("Thanks for playing!")
  else:
    print("Invalid input. Please try again.")