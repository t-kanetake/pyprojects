# project: leap year evaluator
# created: 12/14/2023

# conditions to check if a year is a leap year
def is_leap_year(year):
  if int(year) % 4 == 0:
    if int(year) % 100 == 0:
      if int(year) % 400 == 0:
        print("\nIt is a leap year.")
      else:
        print("\nIt is not a leap year.")
    else:
      print("\nIt is a leap year.")
  else:
    print("\nIt is not a leap year.")

# asks and checks for valid leap year
while True:
  try:
    input_year = str(int(input("Enter a year: ")))
  except ValueError:
    print("Invalid input. Please enter a valid year.")
    continue

  if len(input_year.strip()) == 4 and input_year.strip().isdigit():
    is_leap_year(str(int(input_year)))
  else:
    print("Please enter a valid year.")
    continue

  # asks if user wants to continue
  answer = input("\nWould you like to check another year? (Yes/No) ")
  if answer.strip().lower() in ["yes", "y"]:
    continue
  elif answer.strip().lower() in ["no", "n"]:
    quit("Program ended")
  else:
    print("Please enter a valid answer.")