


# class Word():
#   def__init__(self, chosen_word):
    # this method will split the word up into a list of dictionaries with 2 attributes:
    # the letter/character, and a boolean representing whether or not it has been guessed

  # ...other methods here... (refer back to JS hangman for ideas -- may not translate exactly, but
  # should be close enough)


# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of


# a loop here that will cause game to play and be exited when user either wins or loses
# see below for tips on how to structure this loop

import random
choices = ['javascript', 'python', 'postgresql', 'mongoose']


class Word:
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word

word = Word(random.choice(choices))


def start_game():
    print('It time for hangman, ready to play?')
start_game()
print ("Your word is ")

def show_word():
    tries = 8
    guess = "_" * len(word.chosen_word)
    letters_used = []

    print (guess)

    while "_" in guess and tries > 0:
        player_guess = input("Guess a letter")
        if player_guess in word.chosen_word:
            tries -= 1
            print(f"YES! tries left: {tries}")
            letter = (word.chosen_word.index(player_guess))
            new_guess = guess[:letter] + player_guess + guess[letter + 1:]
            guess = new_guess
            print(guess)
            letters_used.append(player_guess)
            print(f"Letters used: {letters_used}")
        else:
            tries -= 1
            print(f"Nice try! That's not a letter! Try again! Tries left: {tries}")
            letters_used.append(player_guess)
            print(f"Letters used: {letters_used}")
        if "_" in guess:
            end_result = "Whomp Whomp, nice try loser!"
        else:
            end_result = "*Que you are the champion!*"
    else: 
        print(f"GAME OVER!! {end_result}")


show_word()