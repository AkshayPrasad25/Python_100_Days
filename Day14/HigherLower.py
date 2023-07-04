from HigherLowerData import data
import random
from HigherLowerArt import logo, vs

def getinsta():
  return random.choice(data)

def dispdata(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, a2_followers):
  if a_followers > a2_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = getinsta()
  account_b = getinsta()

  while game_should_continue:
    account_a = account_b
    account_b = getinsta()

    while account_a == account_b:
      account_b = getinsta()

    print(f"Compare A: {dispdata(account_a)}.")
    print(vs)
    print(f"Against B: {dispdata(account_b)}.")
    guess = input("Who do you think has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    a2_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, a2_follower_count)
    print(logo)
    if is_correct:
      score += 1
      print(f"Perfect! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Oppsie wrong answer:(  Final score: {score}")

game()