# project: random password generator
# created: 12/10/2023

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&")

def generate_password():
  password_length = int(input("How long would you like your password to be? "))

  random.shuffle(characters)
  
  password = []

  for _ in range(password_length):
    password.append(random.choice(characters))

  random.shuffle(password)

  password = "".join(password)

  print(password)

def ask():
  option = input("Do you want to generate a password? (Yes/No): ")
 
  if option.strip().lower() in ["yes", "y"]:
    generate_password()
  elif option.strip().lower() in ["no", "n"]:
    print("Program ended")
    quit()
  else:
    print("Invalid input. Please try again.")
    ask()

if __name__ == "__main__":
  ask()
