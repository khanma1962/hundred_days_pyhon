
# hangman - complete game

import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.\n')

display = []
word_length = len(chosen_word)
for ch in range(word_length):
    display += '_'


end_of_game = False
lives = 6

while not end_of_game:
    print(display, end='\n')
    guess = input("\nPlease input a character : ").lower()
    clear()
    
    if guess in display:
      print(f"\nYou have already guessed {guess}.")

    for idx, ch in enumerate(chosen_word):
        if ch == guess:
            display[idx] = ch

    if(guess not in chosen_word):
        print(f"Sorry. {guess} is not in the word. You lose a life. Number of lives left is {lives}")
        lives -= 1
        # print(f"Number of lives left is {lives}")
        print(f"Current State: {stages[lives]}")
        if  lives == 0:
            print('You lose!!!\n')
            break

    if  ('_' not in display):
        end_of_game = True
        print(f"\nGood Job. The word is ---> {' '.join(display)}\n")
        # print(display, end='\n\n')
        print("You win!!!\n\n")
        break


    




