import random

from pyparsing import Word

def play_game():
#    theirname = input("What is your name?")
#    print("Good luck",theirname)

    with open("test-word.txt") as test_word:
        words_list = test_word.read()
        words = list(map(str, words_list.split()))
        global the_word 
        the_word = random.choice(words)
        print("Your word is", len(the_word), "letters long.")
        guesses = []
        guesses = input("Guess one letter at a time. Make your guess:")
        # this worked a little bit: print
        print([letter if letter in guesses else "_" for letter in the_word])
        guesses = input("Guess one letter at a time. Make your guess:")


    # guesses=[]
    # their_guess = input("Guess the word one letter at a time")
    # guess_list = their_guess.split()
    # print('guess:', guess_list)

if __name__ == "__main__":
    play_game()
