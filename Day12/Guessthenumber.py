import random
from Guessthenumberart import logo
easymode = 10
hardmode = 5

def check_answer(guess, answer, turns):

  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You guessed right ! The answer is infact {answer} :D")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return easymode
  else:
    return hardmode

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  #print(f"Answer is {answer} :p") 
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose. :(")
      return
    elif guess != answer:
      print("Guess again.")

game()
