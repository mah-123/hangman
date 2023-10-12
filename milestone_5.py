from random import choice


class Hangman:
    '''
    The class hangman contains parameters word_list, num_list and num_lives
    to use to create the game for hangman.
    
    
    attributes:
        self.word_list: random word of list used for guessing the word
        self.num_list: list of unique letters in the word
        self.num_lives: number of lives the person has from 5 until to 0 when the game ends (counter)
        self.num_letters: Keeps an account of letters left in the word_guessed
        self.word: the random word chosen by the word_list to be guessed
        self.word_guessed: Keeps a count of number of words used to guess already
        self.list_of_guess: number of word that had been guessed to be collected on an empty list
        to keep track of. 
    '''
    
    def __init__(self, word_list, num_lives = 5):
        '''
        To check the class hangman please type help(hangman) for more info 
        on the class hangman.
        '''
        
        self.word = choice(word_list)
        self.word_guessed = ["_"]* len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx in range(len(self.word)): 
                if self.word[idx] == guess :
                    self.word_guessed[idx] = guess
                    self.num_letters -=1
            print(f"{self.word_guessed}")
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")    
    '''
    This is a function that uses to check if a letter is in the certain word.
    If there is a letter in this function, it should replace the "_" with the correct guessed letter
    in the right order.

    return:
        print statement of the if the letter is in or not
        self.word_guessed is iterated each time to replace the actual value/character from the "_"
        else if wrong letter is guessed would have num_lives deducted by 1 and prints the lives remaining.
    '''
    
    def ask_for_input(self):
        guess = str(input("Please enter in a single character letter:"))
        if guess.isalpha() == False or len(guess) > 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


#  function that would start the game and initialise the hangman class
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    #list of words used for the guessing game
    list_of_word = ["apple", "banana", "kiwi", "lychee", "mango"]
    play_game(list_of_word)