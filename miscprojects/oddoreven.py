# project: odd or even
# created: 3/15/24

# welcome msg
print("Welcome! Think of a number between 1 and 1000. To quit, press E.")

# project loop
while True:
    user_response = (input("What number are you thinking?\n"))

    # exit loop
    if user_response == "E":
        print("Program ended.")
        break

    # odd/even logic
    if int(user_response) % 2 == 0:
        print("That's an even number! Have another?")
    elif int(user_response) % 2 != 0:
        print("That's an odd number! Have another?")