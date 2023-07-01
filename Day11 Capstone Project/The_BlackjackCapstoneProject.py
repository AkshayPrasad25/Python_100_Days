import random
from Blackjackart import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Calculates the scores of user and computer"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compares user scores with computer scores"""
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose :("
  if user_score == computer_score:
    return "Draw :/"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack :O"
  elif user_score == 0:
    return "Win with a Blackjack :D"
  elif user_score > 21:
    return "You went over. You lose :("
  elif computer_score > 21:
    return "Opponent went over. You win :D"
  elif user_score > computer_score:
    return "You win :D"
  else:
    return "You lose :("

def play_game():
  """Actual Gameplay"""
  print(logo)
  user_cards = []
  computer_cards = []
  endgame = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not endgame:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      endgame = True
    else:
      userdeals = input("Do you want to hit or stand? Type 'y' to get another card, type 'n' to stand: ").lower()
      if userdeals == "y":
        user_cards.append(deal_card())
      else:
        endgame = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your cards in hand: {user_cards}, final score: {user_score}")
  print(f"Computers cards in hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  
  play_game()
