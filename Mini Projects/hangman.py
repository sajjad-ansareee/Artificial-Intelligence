# understanding of basic python data structures


# Hangman
import random
word_list = [
  'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon',
  'computer', 'keyboard', 'mouse', 'monitor', 'printer', 'laptop',
  'python', 'java', 'javascript', 'html', 'css', 'react', 'angular',
  'elephant', 'giraffe', 'kangaroo', 'penguin', 'dolphin', 'butterfly',
  'basketball', 'football', 'soccer', 'tennis', 'baseball', 'volleyball',
  'guitar', 'piano', 'violin', 'drums', 'trumpet', 'saxophone'
]
word_list=random.choice(word_list).lower()
print(word_list)
# Remove duplicates
word=set(word_list)
print(word)
print("You have 8 lives to correctly guess the word!")
lives=0
# Have a set for storing the used letters
used=set()
# Check for the remaining chances and the list has become empty or not
while lives!=8 and word:
  for i in word_list:
    # We have the letter still in word mean not guessed until now
    if i in word:
      print('-', end='')
    else:
      print(i, end='')
    print(' ', end='')
  print()
  guess=input("Your guess(a-z): ")
  #print(f"Guessed: {guess}")
  # We have to maintain a check so the user do not input the same alphabet twice or more
  #Already guessed
  if guess in used:
    print(f"You have already found: {guess} correctly")
  # Check if the guess letter in our word
  elif guess in word:
    word.remove(guess)
    used.add(guess)
  # The guessed letter was not in our word
  else:
    print("Wrong Guess!")
  lives+=1
if lives==8:
  print("You lost!")
else:
  print("You Won!")
