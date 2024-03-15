# project: word counter
# created 3/15/24

import csv
import string

# input function
print("welcome! tell me what's on your mind today or quit by pressing E")

while True:
    user_response = input("what's on your mind today?\n")

    if user_response == "E":
        print("Program ended.")
        break
    
    length_of_msg = (len(user_response.split()))

    print(f"oh nice, you just told me what's on your mind in {length_of_msg} words!")


# file function

translator = str.maketrans('', '', string.punctuation)

word_count = {}
text = open('test.txt').read()

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])