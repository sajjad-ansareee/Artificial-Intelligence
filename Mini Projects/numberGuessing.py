import random
def human_guess():
  number=int((random.random())*100)
  print(number)
  guess=int(input("Guess the number: "))
  moves=1
  while guess!=number:
    # No need to check if the number is equal to guess or not as we will never enter inside the loop if condition holds
    if guess>number:
      print("Too High!")
    else:
      print("Too Low!")
    guess=int(input("Guess again: "))
    moves+=1
  print(f"Guessed correctly! in {moves} guesses.")

def computer_guess():
  # Number guessing but this time computer will guess the number
  # import random
  # Firstly set a random number between 1 and 100 by the user
  number=int(input("Number: "))
  # Firstly the range of our numbers is 1 to 100
  start=1
  end=100
  while True:
    #Now we will not generate the number randomly instead we apply binary search on our range to find the correct number
    guess=int(start+(end-start)/2)
    if guess==number:
      break
    elif guess>number:
      #Our guess is higher so decrease the range from upper portion
      end=guess-1
    else:
      start=guess+1
    print(f"The number guessed by computer is {guess}")
  print(f"Computer correctly guessed {number}")
  
def computer_guess_with_feedback():
  number=int(input("Number: "))
  print(number)
  start, end=1, 100
  while True:
    guess=int(start+(end-start)/2)
    print(f"Guessed number is: {guess}")
    if guess==number:
      break
    feedback=input(f"Is {guess} Too High(h), Too Low(l) than your choice").lower()
    if feedback=='h':
      end=guess-1
    elif feedback=='l':
      start=guess+1
    else:
      print("Invalid input!")
  print(f"Computer correctly guessed {number}")
  
computer_guess_with_feedback()