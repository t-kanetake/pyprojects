# project: calculator (calculator only supports integers)

# adds two values and prints the result
def add(a, b):
  answer = a + b
  print(f"{a} + {b} = {answer} \n")

# subtracts two values and prints the result
def subtract(a, b):
  answer = a - b
  print(f"{a} - {b} = {answer} \n")

# multiplies two values and prints the result
def multiply(a, b):
  answer = a * b
  print(f"{a} * {b} = {answer} \n")

# divides two values and prints the result; does not support zero
def divide(a, b):
  try:
    answer = a / b
    print(f"{a} / {b} = {answer} \n")
  except ZeroDivisionError:
      print("You can't divide by 0. \n")


# ask user for operator choice
while True:
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")
  
  # ask user for operator choice (2)
  choice = input("Input your choice: ")
  
  # asks user for two numbers then calls function
  if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    add(a, b)
  elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    subtract(a, b)
  elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    multiply(a, b)
  elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    divide(a, b)
  elif choice == "e" or choice == "E":
    print("Program ended")
    quit()