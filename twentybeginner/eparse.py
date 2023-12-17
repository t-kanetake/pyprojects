# project: email parser
# created: 12/10/2023

def main():
  print("Welcome to the email slicer." + "\n")
  
  email_input = input("Enter your email address: ")

  # splits the email address into user, domain, tld
  (username, domain) = email_input.split("@")
  (domain, tld) = domain.split(".")

  print("Username:", username)
  print("Domain:", domain)
  print("Top Level Domain:", tld)

if __name__ == "__main__":
  main()

# runs the main function
while True:
  main()
