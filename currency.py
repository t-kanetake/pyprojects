# project: usd and gbp converter
# created: 12/14/2023

# lines 4-10 are to print welcome message once
welcome_message = False

def main():
  global welcome_message
  if not welcome_message:
    print("Welcome to the USD to GBP converter!" + "\n")
    welcome_message = True

  # asks for dollar input and converts to pounds
  dollars = eval(input("Enter the amount in dollars: "))
  pounds = convert_to_pounds(dollars)

  # prints the converted amount
  print(dollars, "dollars is", pounds, "pounds.")

  # asks if user would like to continue with the program
  while True:
    choice = input("Do you want to convert again? (Yes/No): ")
    if choice.lower().strip() in ["yes", "y"]:
      main()
    elif choice.lower().strip() in ["no", "n"]:
      quit()
    else:
      print("Invalid input. Please try again.")

# converts dollars to pounds
convert_to_pounds = lambda dollars: dollars * 0.78

if __name__ == "__main__":
  main()