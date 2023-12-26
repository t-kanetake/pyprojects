# project: site connectivity checker
# created: 12/14/2023

import urllib.request as urllib
from url_normalize import url_normalize

# gets url from user
def main(url):
  print("Checking connectivity...")

  response = urllib.urlopen(url)

  print(f"Connected to {url} successfully!")
  print(f"Response code: {response.getcode()}")


print("Welcome to the site connectiviy checker!" + "\n")
input_url = input("Enter the URL of the website to check: ")
# normalizes url to remove protocol and www
standard_url = url_normalize(input_url)

main(standard_url)
  