# project: quiz
# created: 12/10/2023

# question bank as a dict
quiz = {
  "question1" : {
    "question" : "What is the capital of France?",
    "answer" : "Paris"
  },
  "question2": {
    "question": "What is the capital of Germany?",
    "answer" : "Berlin"
  },

  "question3": {
    "question" : "What is the capital of Italy?",
    "answer" : "Rome"
  },
  "question4": {
    "question" : "What is the capital of Spain?",
    "answer" : "Madrid"
  },
  "question5": {
    "question" : "What is the capital of Portugal?",
    "answer" : "Lisbon"
  },
  "question6": {
    "question" : "What is the capital of Switzerland?",
    "answer" : "Bern"
  },
  "question7": {
    "question" : "What is the capital of Austria?",
    "answer" : "Vienna"
  },
}

# initial score
score = 0

# loops through questions
for key, value in quiz.items():
  print(value["question"])
  answer = input("Answer: ")

  # checks if answer is correct
  if answer.lower() == value["answer"].lower():
    print("Correct!")
    score += 1
    print("Your score is " + str(score) + "\n"*2) 
  else:
    print("Incorrect!")
    print("The answer is  " + value["answer"])
    print("Your score is " + str(score) + "\n"*2) 

# prints final score
print("You got a " + str(score) + "/" + str(len(quiz)))
print(str(int(score / len(quiz) * 100)) + "%")
