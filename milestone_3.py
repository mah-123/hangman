from random import choice

word_list = ["apple", "banana", "kiwi", "lychee", "mango"]

# functions to see if user enters in a valid character
def ask_for_input(guess):
    while(True):
        if(guess.isalpha() == True & len(guess) == 1):
            print("Valid input for guess!")
            break
        else:
            guess = input("Invalid letter. Please, enter a single alphabetical character:")
    check_guess(guess)

#functions to check the guess word to see if the the word_list by random includes the specific letter.
def check_guess(guess):
    guess.lower()
    if(guess in choice(word_list)):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

letter = str(input("Enter in a single char letter:"))
ask_for_input(letter)
