import random



def play_game():
#    theirname = input("What is your name?")
#    print("Good luck",theirname)

    with open("words.txt") as test_word:
        words_list = test_word.read()
        words = list(map(str, words_list.split()))
        global the_word, current_guess
        the_word = random.choice(words)
        count = 9
        print("Your word is", len(the_word), "letters long.")   
    display = ["_"] * len(the_word)
    while count > 0:
        current_guess = input("Guess one letter at a time. Make your guess. ")    
        if "_" not in display: 
            print("Congratulations! You won!")
            exit()
        #print([letter if letter in current_guess else "_" for letter in the_word], "you have", count,"guesses left.")
        i = 0
        if current_guess in the_word:
            for letter in the_word:
                if letter == current_guess:
                    print("Good job! That's a letter in the word.")
                    display[i] = letter
                i += 1  
        else:
            count = count - 1
            print("That's not a letter, try again. You have", count, "guesses left")
        print(display)
    print("Sorry, game over. The word was: {}".format(the_word))
    

    #   guesslist.append(current_guess)
    # #    print(guesslist)
    # #    print(''.join(current_guess))

# for letter in the_word:
#             output = []
#             output.append(letter, current_guess)
#             print(output)  
#             def print_word(the_word, current_guess):
#                 output_letters = [print_word.join((letter, current_guess) for letter in the_word)] 
#                 print("".join(output_letters))   
#             print_word(the_word, output)  
            
#now need to take all of the guesses and put them into a new list 

    # guesses=[]
    # their_guess = input("Guess the word one letter at a time")
    # guess_list = their_guess.split()
    # print('guess:', guess_list)

if __name__ == "__main__":
    play_game()

