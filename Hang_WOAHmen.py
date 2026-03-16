import random
from logging import PlaceHolder

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
placeholder = ""
display = ""
is_game_over = False
while not is_game_over:
    guess = input("make your guess: ").lower()


for letter in chosen_word:
    placeholder += "_"
    if letter == guess:
        display += letter
    else:
        display += "_"
print(placeholder)
print(display)
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# TODO-1: - Use a while loop to let the user guess again.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.