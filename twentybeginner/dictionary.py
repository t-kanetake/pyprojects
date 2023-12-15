# project: word dictionary
# created: 12/14/2023

from PyDictionary import PyDictionary

# initializes an instance of dictionary
dictionary = PyDictionary()

# prints welcome message once
welcome_message = False

def main():
  global welcome_message
  if not welcome_message:
    print("Welcome to the Dictionary!")
    welcome_message = True

  # asks for word and gives meaning if input is valid
  user_word = input("\nEnter a word to look up: ").lower().strip()
  if user_word == "":
    print("Please enter a word")
    main()
  else:
    meaning = dictionary.meaning(user_word)
    if meaning:
      print(meaning)
    else:
      print("\nNo definition found for the word.")

  # asks if user wants to look up another word
  while True:
      answer = input("\nDo you want to look up another word? (Yes/No): ")
      if answer.strip().lower() in ["yes", "y"]:
        main()
      elif answer.strip().lower() in ["no", "n"]:
        print("Thank you for using this dictionary!")
        quit()
      else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
  main()