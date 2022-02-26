import random


def play_game():
#    theirname = input("What is your name?")
#    print("Good luck",theirname)
  
  with open("test-word.txt") as test_word:
        words_list = test_word.read()
        words = list(map(str, words_list.split()))
        global the_word 
        the_word = random.choice(words)
        count = 8
        print("Your word is", len(the_word), "letters long.")   
  while count > 0:
      guesses = input("Guess one letter at a time. Make your guess:") 
      count = count - 1
      if count < 1:
                print("Sorry, game over")
                exit()
      print([letter if letter in guesses else "_" for letter in the_word])




        # def display_letter(letter, guesses):
        #     if letter in guesses:
        #         return letter
        #     else:
        #         return "_" 
        # #
        # for letter in the_word:
        #     output = []
        #     output.append(display_letter(letter, guesses))
        #     print(output)  
        #     def print_word(the_word, guesses):
        #         output_letters = [display_letter(letter, guesses) for letter in the_word] 
        #         print("".join(output_letters))   
        #     print_word(the_word, output)  
            
#now need to take all of the guesses and put them into a new list 

    # guesses=[]
    # their_guess = input("Guess the word one letter at a time")
    # guess_list = their_guess.split()
    # print('guess:', guess_list)

if __name__ == "__main__":
    play_game()
