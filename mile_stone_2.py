from random import choice

#list of word to be randomly picked by importing choice
word_list = ["apple", "banana", "kiwi", "lychee", "mango"]

#assigning the word var to the randomly chosen list of fruits
word = choice(word_list)

#print statement to see the random word_list assigned to word
print(word)

#Using the input format as a str to take a certain
guess = str(input("Enter in a single char letter:"))


#conditional statement to see if the guess is within the right frame
# else prints an error message for incorrect input
if(guess.isalpha() == True & len(guess) == 1):
    print("Valid input for guess!")
else:
    print("Oops! That is not a valid input.")
    
