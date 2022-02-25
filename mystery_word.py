import random

from pyparsing import Word

def play_game():
#    theirname = input("What is your name?")
#    print("Good luck",theirname)

    with open("test-word.txt") as test_word:
        words_list = test_word.read()
        words = list(map(str, words_list.split()))
        print("Your word is", len(random.choice(words)), "letters long.")



    # guesses=[]
    # their_guess = input("Guess the word one letter at a time")
    # guess_list = their_guess.split()
    # print('guess:', guess_list)

if __name__ == "__main__":
    play_game()
