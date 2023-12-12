# project: interest rate calculator

welcome_message = False

def main():
  # prints welcoming message once
  global welcome_message
  if not welcome_message:
    print("Welcome to the interest rate calculator!\n")
    welcome_message = True
  
  principal = float(input("Enter the loan amount: "))
  apr = float(input("Enter the annual interest rate: "))
  time = int(input("Enter the loan duration in years: "))

  # calculate monthly interest rate
  monthly_interest_rate = apr / 1200
  months = time * 12
  monthly_payment = (principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months)))

  print("\nThe monthly payment for this loan is: $%.2f" % monthly_payment + "\n")

  # loops until user is done
  while True:
    answer = input("Do you want to calculate another loan? (Yes/No): ")
    if answer.strip().lower() in ["yes", "y"]:
      main()
    elif answer.strip().lower() in ["no", "n"]:
      print("Thank you for using the interest rate calculator!")
      break
    else:
      print("Invalid input. Please try again.")

if __name__ == "__main__":
  main()