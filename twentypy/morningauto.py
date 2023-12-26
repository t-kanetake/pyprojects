# project: morning message automator
# created: 12/15/2023

import requests
import schedule
import time

# set up the API endpoint and parameters
def send_message():
  resp = requests.post('https://textbelt.com/text', {
    'phone': '7252211276',
    'message': 'Hey. Good morning.',
    'key': 'textbelt',
  })
  print(resp.json())

# schedule the message to be sent every morning at 6:00 AM
schedule.every().day.at("06:00").do(send_message)

# run the scheduler indefinitely
while True:
  schedule.run_pending()
  time.sleep(1)