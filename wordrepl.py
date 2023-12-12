# project: word replacer

# function for replacing word in statement in variable str
def main():
  # enter statement here
  str = ""
  word_to_replace = input("Enter the word to replace: ")
  word_replacement = input("Enter the word replacement: ")
  print(str.replace(word_to_replace, word_replacement))


if __name__ == "__main__":
  main()