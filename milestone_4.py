import random

word_list = ["strawberry", "banana", "mango", "coconut", "kiwi"]
print(word_list)

word = random.choice(word_list)
print(word)

class Hangman:
   def __init__(self, word_list, num_lives=5):
      self.word_list = word_list
      self.num_lives = num_lives
      self.word = random.choice(self.word_list)
      self.word_guessed = ["_" for letter in self.word]
      self.num_letters = len(set(self.word))
      self.list_of_guesses = []
    
   def check_guess(self, guess, word):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    self.word_guessed[i] == guess
                else:
                    self.num_lives -= 1 
                    print(f"Sorry, {letter} is not in the word.") 
                    print(f"You have {self.num_lives} lives left.")   
        else:
            print("Incorrect guess")
        self.num_letters -= 1    

        
   def ask_for_input(self):
        while True:
           guess = input("Please enter a letter: ") 
           if guess.isalpha() ==  False:
               print("Invalid letter. Please, enter a single alphabetical character.")
           elif guess in self.list_of_guesses:
               print("You already tried that letter!")
           else:
               Hangman.check_guess(guess, word)
               self.list_of_guesses.append(guess)

           
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()         
            

      






      