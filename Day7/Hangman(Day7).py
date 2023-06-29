import random
display=[]
from Hangman_words import word_list
chosenword=random.choice(word_list)
word_length=len(chosenword)
from Hangman_art import logo
print(logo)
print(f"Answer lol: {chosenword}")
end_game=False
lives=6
for i in range(0,len(chosenword)):
    display.append("_")
print(display) 
while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosenword[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosenword:
        print(f"You've guessed {guess} and that's not in the word. You lost a life! >w< ")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win. :D  ")
    from Hangman_art import stages
    print(stages[lives])

